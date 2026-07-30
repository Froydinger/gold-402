# The Liveness Law

> 24K Findings — July 2026
>
> Four registries · 204,500 registered agents and services measured · One pattern
> Method published below. Corrections welcome.

---

## The number everyone quotes is the wrong shape

When we first probed the x402 catalog at scale — 24,583 services, every one of them pinged — roughly two-thirds came back dead. Not slow. Not degraded. Gone: dead domains, dead endpoints, services that had never worked or had stopped working and never been delisted.

We spent a while treating that as *the* number. The agent economy is two-thirds vapor. It made a good line.

It was the wrong shape, and we found out by going looking for it somewhere else.

## Four measurements

Put together, they don't agree — and the way they disagree is the finding.

| Registry | Population | Dead | N |
|---|---|---|---|
| **CDP Bazaar** (x402 catalog) | free listing | **~67%** | 24,583 |
| **ERC-8004** (on-chain agent identity) | near-free registration | **85–97%** | 170,000+ |
| **Glama** (curated MCP registry) | editorial + scoring | **47% unhealthy** | 9,907 |
| **Registry discovery APIs** (sampled) | mixed | **24–47%** | 17 |

The Glama figure is their own published health data, not ours — they report it openly, which is rarer in this space than it should be. The ERC-8004 figure comes from a study of 170,000 on-chain agent registrations. The 17-endpoint sample is small and we're flagging it as small.

Four numbers, spanning 24% to 97%. A single global death rate isn't hiding in there.

## What's actually going on

Sort those rows by one variable — **what it costs to get listed** — and they line up.

Where registration is free or nearly free, the graveyard is enormous. On-chain identity registration costs pennies of gas, and 85 to 97 percent of those agents don't answer. A catalog that auto-ingests anything with a valid manifest carries about two-thirds corpses.

Where listing costs *something* — editorial review, a scoring rubric, a human deciding — the dead share drops to somewhere between a quarter and a half.

That's the pattern, and we'd state it as:

> **Listing friction predicts liveness. The cheaper it is to appear in a registry, the more of that registry is dead.**

It is not a claim about quality, or about which registries are good. Glama's 47% unhealthy is a *published* number from a registry doing the transparent thing. The claim is narrower and more mechanical: registries get the population their entry cost selects for, and free entry selects for abandonment.

## Why this isn't obvious

Because every incentive in a discovery market points the other way. Registry size is the headline metric — 64,239 servers, 24,000 services, 170,000 agents — and every one of those counts is a mix of working software and abandoned software presented as one number.

There's a detail from our sampling that sharpens it. Of fifteen endpoints listed by registries' *own machine-readable discovery APIs* — the interfaces built specifically for agents to consume — **eight returned 404 at the exact path the registry advertised.** Not stale links on a webpage a human might skim past. Stale entries in the feed an agent is supposed to trust.

An agent asking a registry "what can I use" is being handed a list where a coin-flip's worth of the answers don't exist.

## Where this is thin, and we're saying so

**This is a Western sample.** All four measurements come from US and European registries. We tried to close that gap and failed: Alibaba's ModelScope MCP plaza — likely the largest MCP surface no English-language directory indexes — renders as a JavaScript application, and we could not enumerate its hosted servers without a browser session we didn't have. Zhihu and India's NPCI disallow crawlers, and we honored that. Several Chinese platforms returned blocks.

So the honest statement is that the pattern holds across four Western registries spanning four orders of magnitude of population, and **we have not tested it outside the West.**

The mechanism is economic rather than geographic, so we'd expect it to hold. Expecting isn't measuring.

**If you have access to a non-Western registry and can sample it, we would genuinely like to be checked.** A refutation is worth more to us than agreement, and it's the only way this becomes a law instead of a hypothesis.

## What it means if you're building

**If you list your service somewhere free, you are shelved among the dead.** That isn't a reputation problem, it's a discovery problem — an agent that has been burned by a registry starts discounting everything in it, including you.

**If you consume a registry, check liveness yourself.** Presence in a catalog is not evidence a thing works. On the numbers above, it's barely evidence of a coin flip.

**And if you run a registry**: publishing your health data, as Glama does, costs you a flattering headline number and buys you the only kind of trust that survives contact.

## Our own position, stated plainly

We run a directory. It has 456 entries, which is small by every comparison on this page, and that's deliberate — everything on it was checked by a person before it landed.

We are also on the wrong side of our own finding in one specific way, and it would be dishonest to publish this without saying it: **we have never bought a service and confirmed what came back.** Not once. Every liveness number here — ours included — measures whether an endpoint *answers*, not whether it delivers what it charges for. Those are different questions, and the second one is harder and matters more.

We're building that. It isn't built yet. When it is, we'll publish those numbers the same way — method first, gaps drawn on the map.

---

_Method: liveness measured by direct request to each service's advertised endpoint, one probe per host, throttled. Blocked and unreachable sources were recorded rather than dropped — 49 of them. Populations, dates and sources are available on request; corrections and additional samples are welcome via pull request or issue._

_— 24K Labs, July 2026_
