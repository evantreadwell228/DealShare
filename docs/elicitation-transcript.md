# Elicitation Session 1 – Transcript

**Format:** simulated, unstructured client interview (see [`process.md`](process.md))
**Developer / analyst:** Evan
**Client:** "Dana Reyes," founder (played by an LLM, Claude)
**Product:** community-driven deal-sharing website (working name: DealShare)

Client turns are labeled **T1–T6**. The `source` field of each requirement in the backlog cites these labels.

---

### Setup (developer's brief to the LLM)

> I need you to play as a client for me, a software developer, doing requirements gathering. The idea you have is for a website that allows users to centralize online shopping by sharing deals from many websites. The inspiration is something like YouTube; if you set out to create a site for "tutorials", manually providing them as the site owner would be a monumental task and ultimately a pretty poor execution without being an expert in many things. YouTube, by being a place where many people with experience can share their own tutorials, can be far more effective than an individual or organization would. Instead of manually scraping websites for vague notions of similar products, allow users to self manage through their own experiences.

---

### T1 – Client pitch

**Dana:** Hey, thanks for meeting with me. I'll give you the pitch and then you can grill me.

So, online shopping is a mess. If I want a good price on, say, a standing desk, I've got Amazon open, Walmart, Best Buy, some random brand site, a coupon site that's half expired codes, a Reddit thread from two years ago... it's exhausting. And the "deal aggregator" sites out there are mostly bots scraping prices. They'll show you a "similar" product that isn't actually similar, or a deal that died last Tuesday.

My idea is basically YouTube, but for deals. YouTube didn't hire a million experts to make tutorials. It gave people who actually know stuff a place to share it. I want the same thing for shopping. Real people who found a great deal post it, other people find it, and the community keeps it honest. Good deals rise, dead or junk deals sink.

I want it to be *the* place you check before you buy anything. Clean, fast, trustworthy. And I want it to feel like a community, not a coupon dump. I've got funding, so I'm not trying to cut corners. I'd rather build it right.

That's the vision. Where do you want to start?

---

**Evan:** Alright, as a user content centered platform I'm thinking the first thing we should sync on is exactly how you want users to be presented with content, and how users can create content. Is each post a self contained piece of data or do you imagine some kind of user managed linking between similar posts, or something different entirely?

### T2 – Post structure and discovery

**Dana:** Good question, and honestly it's something I've gone back and forth on.

My first instinct was that each post is just its own thing. Someone finds a deal, pastes the link, puts in the price and the store, maybe writes a sentence like "this is $80 off, I've had mine for a year and it's great." Done. Posting has to be dead simple. If it takes more than about 30 seconds, nobody will do it.

But here's what bugs me. Say a monitor goes on sale at Best Buy. Within an hour, five different people post the same deal. Now my front page is five copies of one monitor, and that's exactly the cluttered coupon-site feel I hate. And sometimes the same monitor is cheaper at Newegg, and someone posts *that*, but it shows up as a separate thing and nobody sees the two side by side.

So I guess what I'm picturing is that posts are individual, but they collect under the *product*. You'd have a page for "that monitor," and on it you'd see all the deals people have posted for it, from different stores and at different times, with the best one at the top. I don't know if users link them themselves or the site figures it out. You tell me what's realistic. I just know I don't want duplicates and I don't want people missing a better price that's sitting right there.

As for how people *see* content, there's a main feed of what's hot right now, which is the YouTube home page idea. Then categories like electronics, home, clothing and so on, plus search. And I'd like people to follow categories or other users they trust. If someone always finds great camping gear deals, I want to see their stuff.

Oh, and it'd be really cool if you could see the price history on those product pages, like "this was $300 in March, now it's $220." Is that hard?

---

**Evan:** Alright, a basic social media-esque or Amazon-like home page makes perfect sense and probably doesn't need an expansion on for now. As for the post structure, the product collection definitely makes the most sense, but the duplicate pages problem might still occur depending on how that collecting works. Do you imagine users ever manually inputting some kind of product signifier, or would you want the website to do that entirely automatically somehow? As for the price history page, that probably wouldn't be out of scope, but is a little specific for where we are so let's save that for later.

### T3 – Product identification and variants

**Dana:** Fair enough, we'll park price history. I just didn't want it to fall off the list.

On the product question, I *really* don't want users typing in model numbers or SKUs. My mom would never do that, and she's exactly who I want posting a great deal on a vacuum. If the post form has a field like "Enter product UPC," I've already lost half my users.

So in a perfect world it's automatic. You paste the link, and the site knows it's the LG 27-inch whatever and files it under that product. But I'm not naive, I know it won't be right every time. So maybe the site takes its best guess and asks the user. You paste the link and it says "Looks like this is the *LG 27GP850*, is that right?" They click yes, or they pick from a couple of other suggestions, or they say "no, this is something new." That's one click, not data entry.

And when it still gets it wrong, the community should be able to fix it. Wikipedia-style: someone flags "these two product pages are the same thing," and they get merged. Or the opposite: "this deal got lumped in with the wrong product," and it gets moved. I don't know who should have the power to do that, whether it's everyone, trusted users, or just moderators. That's probably a bigger conversation.

One thing that's going to get messy, and I've seen this on other sites: variants. Same monitor, but one is refurbished. Same shoes in a different color. Same laptop with 16 gigs of RAM instead of 32. Are those the same product or not? Because if a refurbished deal sits at the top of the page as "best price," people will feel tricked. I don't have a clean answer. I just know that matters to me.

---

**Evan:** So the site needs a way to read through the product listing and parse out some signifying ID automatically for a potentially unlimited number of different products on unlimited sites, that would probably be the most significant undertaking for the whole project. If you're certain that's what you want, let's focus on working that out for the rest of this meeting. The variants question ties somewhat into that, I could see a system of providing multiple pages of listings under one parent product for each variant, but how the website distinguishes those from each other will be important. Taking a step back first, I need to get a better picture of the business processes. Are you aware of the ability/legality of any website to scrape info from a link? What challenges might we face there?

### T4 – Data acquisition, legality, business model

**Dana:** Okay, "most significant undertaking" makes me a little nervous, so let me be clearer about what I'm actually set on. What I care about is that *posting* stays effortless and *duplicates* stay rare. Full automation for every site on the internet isn't a requirement. If the site can figure out the product for the big stores and has to ask the user for a name or a photo on some random boutique site, I can live with that. So yes, let's dig into it, but treat full automation as the goal, not something we can't ship without.

On scraping, I'm not technical and I'm definitely not a lawyer, so take this with a grain of salt. Here's what I know.

When you paste a link into iMessage or Slack, it pulls up a little preview with a title and picture, right? So *some* of that info is clearly meant to be read by other sites. I assume that's the easy part.

The big stores are where it gets complicated. I know Amazon in particular hates bots. A friend of mine ran a price-tracking side project and they kept blocking him. I've also heard you're "allowed" to scrape public pages in the U.S. after some court case involving LinkedIn, but that a site's terms of service can still say no, and you can still get blocked or sued. I honestly don't know where the line is. Before we launch I'd want an actual lawyer to sign off on whatever we do. I don't want to build the whole thing on something that gets pulled out from under us.

And here's something I should've brought up earlier, because it matters. **The way this site makes money is affiliate links.** When someone clicks through to a deal and buys, we get a small commission. That's the whole business model, at least at first. No ads cluttering the page, no charging users. So we'll be signing up for affiliate programs with Amazon, Walmart, Best Buy, and others anyway. I've heard some of those programs give you official access to product info, including prices, pictures and product IDs, and that might be the cleaner route for the big stores instead of scraping. But I've also heard they have strict rules about how you display prices, like how old a price is allowed to be. I don't know the details.

So the challenges as I see them are:
- some stores actively block this,
- the legal gray area,
- every store's page is built differently,
- and prices change constantly, so even if we read the page correctly, the deal might be dead tomorrow.

That last one ties back to the "dead deals" thing I complained about at the start. I want expired deals to stop showing up as if they're live.

Does that help? What else do you need to know about how the business runs?

---

**Evan:** We can work with that, it probably wouldn't be a good idea to base the entire functionality off an expensive bot that might get blocked by half the relevant sites the moment your site gets popular. Automation where possible, with an affiliate system aiming to pose you as a collaborator to the sites being linked to instead of a competitor. Got it. Does the poster also make a portion of the commission, like with YouTube? I imagine this would motivate users to not only join but put effort into making their posts, potentially reducing the reliance on the automation.

### T5 – Poster revenue share and abuse risks

**Dana:** Yes, you've got it. I want us to be a partner to the stores, not a bot they're trying to block.

The revenue share is something I really want, and also something I'm a little scared of. Let me explain both sides.

**Why I want it:** you're exactly right, it's the YouTube effect. If people can earn something, the good ones will put real effort in: write a proper description, add their own photos, say "I own this, here's what's good and bad about it." That's the stuff that makes us better than a bot. It also gives people a reason to choose us over posting on Reddit for free.

**Why it scares me:** the moment there's money in it, people will game it.
- Sellers and brands will make accounts and "share deals" on their own products.
- People will post fake or inflated deals, like "70% off!" on something that was never really full price.
- People will spam every product they can find just to fish for commissions.
- And remember the duplicates problem? If five people post the same monitor deal and there's money involved, **who gets credit?** The first poster? The one with the best write-up? That will cause fights. I'm sure of it.

So where I've landed for now, and tell me if it's dumb:
- **Not everyone gets paid on day one.** New users earn reputation, something like points or a trust level, from upvotes and accurate posts.
- Once someone has a track record, they unlock the revenue share. YouTube does something similar, where you need a certain number of subscribers before you can monetize.
- If someone's posting junk, they lose that status.
- People who are actually affiliated with the brand or store they're posting about have to say so, and that should show on the post.

I don't know what the split should be. Probably smaller than YouTube's, since our margins on commissions are thin. I also don't know whether the stores' affiliate programs even *allow* us to pass part of the commission on to users. That's another one for the lawyer list.

And paying people means collecting payout info, tax forms, minimum payout amounts... I assume there are services that handle that, so we don't have to build it ourselves? I really don't want us holding people's bank info if we can avoid it.

---

**Evan:** The specifics of financial data storage are not something we should worry about too much today, but we'll note that you want to directly hold as little of that responsibility as possible. I think we've got a good enough idea to start prototyping and work from there. We've got a system that should allow users to create posts, asking as little information as is necessary (fill in only when the bot can't figure it out), that post will be categorized under a master post for the particular product, with separate tabs for different variants, and we've pinned a price history viewer as a desired feature. Users can shop, search and filter on a home screen in a way analogous to a merge between Amazon and YouTube. All of this needs to be built with a store/user affiliate system in mind. Do you feel good about this meeting or are there any other concerns about the basic functions you'd like to bring up?

### T6 – Wrap-up: items missing from the summary

**Dana:** I feel really good about this. You pushed back in the right places, and I came in thinking "automatic" and I'm leaving with something realistic. Your summary is right, but a few things I care about didn't make it in, and I'd hate for them to drop off:

1. **Dead deals.** This was my number one complaint about other sites. When a deal expires or the price goes back up, it needs to stop looking live. That could be the system checking, users clicking "this deal is dead," or both.
2. **Voting and reputation.** Upvotes and downvotes are how good deals rise. They also feed the trust levels that unlock the revenue share, so I don't see this as a side feature.
3. **Community cleanup.** Flagging duplicates, merging product pages, moving a deal to the right product or variant. We still haven't decided *who* gets to do that.
4. **Honesty rules.** People affiliated with a brand have to disclose it, and refurbished or open-box deals can't pass as "best price" on the new product.
5. **Credit for duplicate posts.** Once money is involved, we need a rule for who gets credit when five people post the same deal.

One thing we never talked about: half my friends shop on their phones. I assume this works great on mobile? I don't need an app on day one, but the site can't be painful on a phone.

Other than that, I'm happy. Send me the notes and let's see a prototype.
