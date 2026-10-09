#!/usr/bin/env python3
"""Validate backlog/requirements.yaml and generate backlog/BACKLOG.md.

Checks:
  - IDs are unique
  - every depends_on / parent reference exists
  - every blocked_by reference exists in docs/open-questions.md
  - the dependency graph has no cycles

Usage: python3 tools/build_backlog.py
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "backlog" / "requirements.yaml"
OUT = ROOT / "backlog" / "BACKLOG.md"
OQ_DOC = ROOT / "docs" / "open-questions.md"

PRIORITY_ORDER = {"must": 0, "should": 1, "could": 2, "wont": 3}


def fail(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def validate(reqs, oq_ids):
    ids = [r["id"] for r in reqs]
    dupes = [i for i, n in Counter(ids).items() if n > 1]
    if dupes:
        fail(f"duplicate IDs: {dupes}")
    known = set(ids)
    for r in reqs:
        for d in r.get("depends_on", []):
            if d not in known:
                fail(f"{r['id']} depends on unknown {d}")
        if r.get("parent") and r["parent"] not in known:
            fail(f"{r['id']} has unknown parent {r['parent']}")
        for q in r.get("blocked_by", []):
            if q not in oq_ids:
                fail(f"{r['id']} blocked by unknown {q}")

    # cycle check (DFS)
    graph = {r["id"]: r.get("depends_on", []) for r in reqs}
    state = {}

    def visit(n, path):
        if state.get(n) == 1:
            fail("dependency cycle: " + " -> ".join(path + [n]))
        if state.get(n) == 2:
            return
        state[n] = 1
        for m in graph[n]:
            visit(m, path + [n])
        state[n] = 2

    for n in graph:
        visit(n, [])


def mermaid(reqs, epics):
    lines = ["```mermaid", "flowchart LR"]
    by_epic = defaultdict(list)
    for r in reqs:
        by_epic[r["epic"]].append(r)
    for code, rs in by_epic.items():
        lines.append(f'  subgraph {code}["{epics[code]}"]')
        for r in rs:
            label = r["title"].replace('"', "'")
            lines.append(f'    {r["id"].replace("-", "_")}["{r["id"]}<br/>{label}"]')
        lines.append("  end")
    for r in reqs:
        for d in r.get("depends_on", []):
            lines.append(f'  {d.replace("-", "_")} --> {r["id"].replace("-", "_")}')
    lines.append("```")
    return "\n".join(lines)


def main():
    data = yaml.safe_load(SRC.read_text())
    epics, reqs = data["epics"], data["requirements"]
    oq_ids = set(re.findall(r"\|\s*(OQ-\d+)\s*\|", OQ_DOC.read_text()))
    validate(reqs, oq_ids)

    dependents = defaultdict(list)
    for r in reqs:
        for d in r.get("depends_on", []):
            dependents[d].append(r["id"])

    counts = Counter(r["priority"] for r in reqs)
    status = Counter(r["status"] for r in reqs)
    out = [
        "# DealShare Requirements Backlog",
        "",
        "> **Generated** from `requirements.yaml` by `tools/build_backlog.py`. Edit the YAML, not this file.",
        "",
        f"**{len(reqs)} requirements** "
        f"({sum(r['type'] == 'functional' for r in reqs)} functional, "
        f"{sum(r['type'] == 'nonfunctional' for r in reqs)} nonfunctional) · "
        + " · ".join(f"{k}: {counts[k]}" for k in PRIORITY_ORDER if counts[k])
        + " · "
        + " · ".join(f"{k}: {v}" for k, v in sorted(status.items())),
        "",
        "Source references (T1–T6) point to client turns in "
        "[`docs/elicitation-transcript.md`](../docs/elicitation-transcript.md). "
        "Open questions (OQ-xx) are in [`docs/open-questions.md`](../docs/open-questions.md).",
        "",
        "## Summary",
        "",
        "| ID | Title | Type | Level | Priority | Status | Risk | Depends on | Blocked by |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in sorted(reqs, key=lambda r: (r["epic"] == "NFR", PRIORITY_ORDER[r["priority"]], r["id"])):
        level = r["level"] + (f" ↳ {r['parent']}" if r.get("parent") else "")
        out.append(
            f"| [{r['id']}](#{r['id'].lower()}) | {r['title']} | {r['type'][:4]}. | {level} | "
            f"{r['priority']} | {r['status']} | {r['risk']} | "
            f"{', '.join(r.get('depends_on', [])) or '—'} | {', '.join(r.get('blocked_by', [])) or '—'} |"
        )

    out += ["", "## Dependency graph", "", "An arrow A → B means B depends on A.", "", mermaid(reqs, epics), ""]

    out += ["## Highest-risk requirements", "",
            "These have high expected volatility or implementation risk. Track their change frequency and prioritize testing them.", ""]
    for r in reqs:
        if r["risk"] == "high":
            out.append(f"- **{r['id']}** {r['title']}")
    out.append("")

    out += ["## Details by epic", ""]
    for code, name in epics.items():
        rs = [r for r in reqs if r["epic"] == code]
        if not rs:
            continue
        out += [f"### {name}", ""]
        for r in rs:
            out += [
                f"#### {r['id']}",
                f"**{r['title']}**",
                "",
                f"*{r['story']}*",
                "",
                f"- **Type / category:** {r['type']} / {r['category']}",
                f"- **Level:** {r['level']}" + (f" (refines {r['parent']})" if r.get("parent") else ""),
                f"- **Priority:** {r['priority']} · **Status:** {r['status']} · **Risk:** {r['risk']}",
                f"- **Source:** {r['source']}",
                f"- **Depends on:** {', '.join(r.get('depends_on', [])) or 'none'}",
                f"- **Required by:** {', '.join(dependents.get(r['id'], [])) or 'none'}",
            ]
            if r.get("blocked_by"):
                out.append(f"- **Blocked by:** {', '.join(r['blocked_by'])}")
            out += ["- **Acceptance criteria:**"] + [f"  - {a}" for a in r["acceptance"]] + [""]

    OUT.write_text("\n".join(out))
    print(f"OK: {len(reqs)} requirements validated -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
