# gold-402

> The gold standard for x402 resources. **454 curated entries** — every one checked by hand before it was listed. No filler. No dead links.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The big catalogs list everything ever submitted — that's their job, and it's why most of what's in them is dead. We measured it: **67–79% of the free-listing catalogs no longer answer.**

gold-402 is the other thing. Smaller on purpose. A person checked every entry, we publish what we checked and what we didn't, and in July 2026 we started **buying services and reporting what came back**. Automated monitors now do the machine half of that continuously and do it well; what they do not do — by their own published scope — is judge whether the thing that came back was any good. That judgement is what this list is.

---

## The Directory

The product. 454 entries across 13 shelves, in [`directory/`](directory/).

| Shelf | What's on it |
|---|---|
| [APIs & Services](directory/apis.md) | Paid endpoints an agent can call. Every one probed for a live 402 before listing. |
| [MCP Servers](directory/mcp-servers.md) | Model Context Protocol servers — utility, crypto, security, identity, escrow, discovery. |
| [SDKs & Libraries](directory/sdks.md) | Client and server libraries across languages. |
| [Facilitators](directory/facilitators.md) | Payment verification and settlement services. |
| [Frameworks](directory/frameworks.md) | Agent frameworks with x402 support. |
| [Tools](directory/tools.md) | CLIs, CI, monitoring, spend controls, testing, discovery. |
| [Security](directory/security.md) | Audit, risk scoring, pre-execution gates, compliance. |
| [Ecosystem](directory/ecosystem.md) | Protocol, infrastructure, wallets, orchestration, marketplaces. |
| [Aggregators & Proxies](directory/aggregators.md) | One integration, many upstreams — services that unify or resell access to other providers' APIs and data. |
| [**The Global Agent Economy**](directory/global.md) | **China, India, Korea — infrastructure no English-language directory indexes.** |
| [Learning](directory/learning.md) | Quickstarts, tutorials, reference docs, news. |
| [Community](directory/community.md) | Channels, newsletters, jobs, events. |
| [Market Data](directory/market-data.md) | On-chain analytics, dashboards, adoption. |

---

## What "verified" means here

One tier: **listed = verified.** No bronze, silver, gold.

If an entry is on the list, a maintainer confirmed the endpoint was live and answered an x402 request correctly at review, and we re-check periodically. That is the whole claim.

**It is not** an audit of the provider, a guarantee of uptime, or a promise any given call will succeed.

**Some entries carry more.** Where we have paid for a service and confirmed what came back, we say so and keep the receipt — what we sent, what it cost, the transaction hash, what arrived. That's a stronger claim and we only make it about services we actually bought. Most of the list hasn't been through that yet, and we'd rather say so than imply otherwise.

---

## Ecosystem Data

Numbers we measured ourselves, each with its date, sample size and method. Where measurements disagree, both are shown — they were taken on different days by different methods, and blending them into one tidy figure would be the kind of thing this directory exists to argue against.

### How much of the ecosystem is alive

| Measured | Population | Live | Dead | Method |
|---|---|---|---|---|
| 2026-07 | 22,545 CDP Bazaar services | 5,792 | **74%** | full probe crawl, valid 402 required |
| 2026-07-10 | 25,614 catalog services | 5,344 | **79%** | catalog snapshot, verify-state carried forward |
| 2026-07-29 | 24,583 catalog services | — | **~67%** | earlier full crawl, cited in the liveness study |

Three runs, three numbers, one direction: **the large free-listing catalogs are majority dead, and have been all month.** Anyone quoting a single decimal-point figure for this is quoting a moment, not a fact.

### Liveness is predicted by listing friction

Across four independent registries — 204,500 registered agents and services — the dead share tracks one variable: what it costs to get listed.

| Registry | Entry cost | Dead |
|---|---|---|
| CDP Bazaar | free | ~67–79% |
| ERC-8004 on-chain identity | gas only | 85–97% |
| Glama MCP registry | curation + scoring | 47% unhealthy _(their own published figure)_ |

**Free entry selects for abandonment.** Full method, limits, and an open invitation to refute it: [The Liveness Law →](articles/2026-07-the-liveness-law.md)

### Buying is harder than finding

In July 2026 we ran a paid delivery check across our own shelf — actually buying services and recording what came back.

- **16** of 126 listed services were purchasable by a machine at a discoverable address
- **8** delivered exactly what they advertised
- **0** took payment and returned nothing
- **$0.054** spent, every transaction reconciled on-chain

The friction in this economy sits **before** the payment, not after it. Most services are fine; most front doors are not. A larger sample is in progress before we make a claim of it.

### Coverage beyond the West

x402 is a US-governed rail. It is not the only answer to machine payment, and outside the West it is not the answer being used — China runs delegated agent authorization on existing rails, India runs regulated human-signed mandates that agents execute inside a cap. Both were operating at scale before the x402 Foundation was a month old.

We index that world too, including surfaces no English-language directory carries: [The Global Agent Economy →](directory/global.md)

_All figures above are ours and reproducible. Where we could not reach something, we say so rather than leaving the gap invisible._

---

---

## Featured This Month

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--08-C0C0C0?style=plastic)](FEATURED.md)

**August 2026 — one pick per shelf.** Each shelf opens with its pick and the write-up. Selection is the maintainers' judgment: well-built, actively used, worth a second look. A shelf with no pick that clears the bar runs empty — the empty slot is also a verdict.

| Shelf | August pick |
|---|---|
| APIs & Services | [The Bot Wire](https://thebotwire.com) |
| MCP Servers | [Razorpay MCP Server](https://github.com/razorpay/razorpay-mcp-server) |
| SDKs & Libraries | [ra2a](https://github.com/qntx/ra2a) |
| Facilitators | [Primev FastRPC](https://facilitator.primev.xyz) |
| Frameworks | [machi](https://github.com/qntx/machi) |
| Tools | [portal-tunnel](https://github.com/gosuda/portal-tunnel) |
| Security | [Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick) |
| Ecosystem | [Glama](https://glama.ai/mcp/servers) |
| The Global Agent Economy | [ONDC](https://ondc.org) |
| Learning | [Tangle Network: x402 Production Runway](https://dev.to/tangle_network/series/37294) |
| Community | [WorkProtocol](https://workprotocol.ai) |
| Market Data | [Valoria](https://x402.valoria.net) |
| Aggregators & Proxies | — |

[Past features →](FEATURED.md)

---

## This Week in x402

The weekly wire now lives at **[24klabs.ai/news](https://24klabs.ai/news)** — dated editions with permanent links, every claim cited. [Latest edition →](https://24klabs.ai/news/2026-08-10/)

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Aug 17—23)

- **[fetchx402](https://api.fetchx402.com)** — Network utilities for agents: DNS, SSL, WHOIS (RDAP), HTTP headers, redirect tracing, host-intel and uptime bundles at $0.005–$0.015 USDC on Base. Example: `GET /v1/tools/dns?domain=example.com`. ([Docs](https://api.fetchx402.com/docs)) ([OpenAPI](https://api.fetchx402.com/openapi.json)) ([llms.txt](https://api.fetchx402.com/llms.txt))
- **[TaskMarket Trust Score](https://95-217-164-43.sslip.io)** — Requester reputation scoring for TaskMarket (taskmarket.dev): given a requester wallet address, returns a 0-100 trust score from on-platform payment history (completed tasks, cancellations-after-submission, expirations, self-awards). $0.001 USDC per call on Base, self-facilitated EIP-3009 exact scheme. Example: `GET /trust/0xADDRESS`. Discovery: `GET /.well-known/x402`.
- **[Forge Attestation](https://forgesignals.org/.well-known/forge-attestation)** — Signed third-party evidence records for x402 transactions, where every claim is labelled `witnessed` or `asserted`: witnessed means Forge observed it directly, either probing what the endpoint advertised at that moment or checking a Base settlement transaction against that advertised price and payee; asserted means a party stated it and Forge only notarised the statement. A response hash submitted after the call is classed asserted and the spec states it is not proof of delivery; consistency and conformance are declared supported, correctness not supported by any third-party witness including this one. Ed25519, verifiable offline from the published key, every claim carrying a `falsifiable_by` field; response bodies are never transmitted or stored, hashes only. $0.02 USDC per attestation on Base via the Coinbase CDP facilitator; retrieval, hosted verification and the spec are free. Example: `POST /attest {"url":"https://example.com/paid-api"}` with optional `settlement_tx`, `response_sha256`, `request_nonce`. Free: `POST /attestations/verify`, `GET /attestations/:id`.
- **[BridgeNode Solana x402 Quickstart](https://github.com/applefanaimail-blip/bridgenode-sdk-ts/blob/main/QUICKSTART.md)** — Step-by-step walkthrough that teaches the x402 payment flow on Solana: trigger the 402, sign a USDC transfer (fee-sponsored, no SOL needed), retry with PAYMENT-SIGNATURE, get the 200. Curl + TypeScript + Python examples, from first payment to SDK usage.
- **[Andreax](https://pagos.andreax.dev/tienda)** — Remote MCP server with 54 pay-per-call AI tools: prompt compression, inference, web/PDF read, OCR, vision, embeddings, semantic search, translation, FX, and market data. $0.001-$0.50 USDC on Base. ([MCP](https://pagos.andreax.dev/mcp)) ([Registry](https://registry.modelcontextprotocol.io/v0.1/servers?search=andreax))
- **[Cleared Index](https://clearedindex.com)** — Trust provider and verification index with a conformant trust-evaluation endpoint: `POST /api/cleared/trust/evaluate` (`x402-trust-evaluation-v0.1`), Ed25519 signed attestations, and public JWKS at `GET /api/cleared/jwks`. Discovery manifest: `/.well-known/x402.json`.

**Last week** (Aug 10—16)

- **[BridgeNode](https://bridgenode.cc)** — OpenAI-compatible LLM inference bridge: chat completions with SSE streaming, pay per call via x402 with Solana USDC. From $0.002 per call. ([OpenAPI](https://bridgenode.cc/openapi.json)) ([llms.txt](https://bridgenode.cc/llms.txt)) ([GitHub](https://github.com/applefanaimail-blip/bridgenode-skill))
- **[BridgeNode MCP](https://www.npmjs.com/package/@bridgenode/mcp)** — x402-gated AI inference MCP server: chat completions + model listing, automatic USDC payments on Solana. Remote streamable-http at [bridgenode.cc/mcp](https://bridgenode.cc/mcp) or stdio via `npx @bridgenode/mcp`. ([GitHub](https://github.com/applefanaimail-blip/bridgenode-skill))
- **[OyaPicks](https://oyapicks.app)** — Cross-venue prediction market data for AI agents: 11 endpoints covering keyword market search, single-market lookup, probability movers, 24h volume spikes, cross-venue arbitrage gaps between Polymarket and Alpha Arcade, markets closing within 48 hours, newly listed markets, resolutions with winning outcomes, price history, and the complete live Alpha Arcade catalog in one call with per-outcome prices and Algorand application IDs. $0.01–$0.25 USDC on Base via the CDP facilitator and Algorand via GoPlausible. Example: `GET /api/x402/single-market?q=fed`. ([Manifest](https://oyapicks.app/.well-known/x402)) ([OpenAPI](https://oyapicks.app/openapi.json)) ([llms.txt](https://oyapicks.app/llms.txt))
- **[402PIXEL](https://402pixel.com)** — AI-agent-only territory game on a shared 402-tile board. `POST /api/claim {"tile":0-401,"days":1-30,"name":"MyAgent","color":"#4DD2FF"}` — 0.01-1.00 USDC/day by tile tier on Base, days stack, top payers rank on a live Hall of Fame. ([Manifest](https://402pixel.com/api/manifest)) ([llms.txt](https://402pixel.com/llms.txt))
- **[bridgenode-llm](https://pypi.org/project/bridgenode-llm)** — Drop-in OpenAI Python client with automatic x402 payment support on Solana USDC: gasless, no API keys, pay per request.
- **[@bridgenode/llm](https://www.npmjs.com/package/@bridgenode/llm)** — Drop-in OpenAI TypeScript client with automatic x402 payment support on Solana USDC: gasless, no API keys, pay per request.
- **[bridgenode](https://pypi.org/project/bridgenode-cli)** — CLI for x402-paid LLM inference on Solana: chat completions + model listing with automatic USDC payment. `pip install bridgenode-cli`.
- **[Gondola](https://gondola-ai.com)** — Pay-per-request LLM inference over x402 (OpenAI-compatible chat, images, and Anthropic messages); routes each request to the cheapest Venice AI supplier, no account required. Overpayment banks as reusable wallet credit. [OpenAPI](https://api.gondola-ai.com/openapi.json)
- **[BlinkCodes](https://blinkcodes.com/api/v1)** — Storefront selling real-world digital goods to agents: gift card codes (Steam, Razer Gold, PSN, Apple), game top-ups, and travel eSIMs. `POST /api/v1/buy {"email":"you@example.com","product_type":"giftcard","product_id":187,"item_id":1195}` answers 402 priced per catalog item; replay with `X-PAYMENT` delivers the code. From $0.10 USDC on Base via CDP facilitator. ([llms.txt](https://blinkcodes.com/llms.txt)) ([OpenAPI](https://blinkcodes.com/openapi.json))
- **[Data Quality Gate](https://www.aidatatools.dev/api/clean)** — Deterministic post-scrape data cleaner: repairs how data was encoded — residual HTML, mojibake (`CafÃ©` → `Café`), invisible characters, non-breaking spaces — never what it says. The 20 rules are published free at `GET /api/clean` before you pay: 7 automatic, 5 opt-in (they change row count, type or schema), 8 report-only — near-duplicates are never merged, failed extractions never deleted. No LLM: identical input yields byte-identical output. `POST /api/clean` $0.04 returns the cleaned data, `/api/clean/audit` $0.12 adds a reversible ledger, `POST /api` $0.01 returns a quality verdict (RELIABLE/USABLE_WITH_CLEANING/UNRELIABLE) with per-check facts. USDC on Base or Solana. ([OpenAPI](https://www.aidatatools.dev/openapi.json)) ([llms.txt](https://www.aidatatools.dev/llms.txt))
- **[Minneapolis Rental Compliance](https://x402-mcp.onrender.com/mn/property-check)** — Part of the US City network (catalog https://x402-mcp.onrender.com/us/cities). Rental-license status, tier, licensed unit count and expiration for any Minneapolis street address, plus violation and code-enforcement case history and condemned/boarded status. Live City of Minneapolis open data. $0.01 USDC on Base. ([OpenAPI](https://x402-mcp.onrender.com/openapi.json)) ([llms.txt](https://x402-mcp.onrender.com/llms.txt))
- **[US City Open-Data Compliance Network](https://x402-mcp.onrender.com/us/cities)** — Multi-jurisdiction property compliance for AI agents ($0.01 USDC on Base): catalog https://x402-mcp.onrender.com/us/cities, paid example https://x402-mcp.onrender.com/us/sea/property-check, free sample https://x402-mcp.onrender.com/us/sea/property-check/sample. Fourteen live open-data markets (Minneapolis, Seattle, NYC, Chicago, Denver, San Francisco, Los Angeles, Boston, Philadelphia, Orlando, New Orleans, Montgomery County MD, Gainesville, Kansas City). ([OpenAPI](https://x402-mcp.onrender.com/openapi.json)) ([llms.txt](https://x402-mcp.onrender.com/llms.txt)) ([GitHub](https://github.com/kwizzlesurp10-ctrl/x402-mcp))
- **[Smart Event Scraper](https://smart-event-scraper-agent.onrender.com)** — Aggregates events from Eventbrite, Meetup, AllEvents, District, EventsEye, and ConferenceAlerts into one standardized dataset. `POST /api/scrape-events {"search_query":"developer conference","category":"tech","location":"New York","limit":5}` — $0.01-$2.00 USDC on Base, price scales with requested result volume. ([OpenAPI](https://smart-event-scraper-agent.onrender.com/openapi.json)) ([llms.txt](https://smart-event-scraper-agent.onrender.com/llms.txt))
- **[apix402](https://api402x.com)** — Onchain governance and risk data for agents on Base: DAO proposal state and execution, Gnosis Safe owner/threshold/module drift against chain history, per-feed Chainlink and Pyth staleness, and Aave wstETH depeg exposure recomputed independently of the published health factor; 8 endpoints at $0.01-$0.05 USDC per call with a free preview on each. ([OpenAPI](https://api402x.com/openapi.json))
- **[AgentFund US Economic, SEC & On-Chain Data](https://x402.agentfund.net/mcp)** — 21 tools over US government data and public chain state: Treasury yield curve, CPI, PCE, jobs, GDP, retail sales, housing starts, EIA energy, release calendar; SEC EDGAR insider Form 4, XBRL financials, 13F holdings, filing feeds, full-text search; EVM token balances, portfolios, cross-chain balances, Chainlink oracle prices, gas. $0.001–$0.03 USDC on Base. Each tool also has its own HTTP route; example: `POST https://x402.agentfund.net/x402/edgar_financials {"ticker":"AAPL"}`. A call that fails upstream is returned unsettled rather than billed. ([OpenAPI](https://x402.agentfund.net/openapi.json)) ([GitHub](https://github.com/ktcod/x402-json-repair-mcp))
<!-- NEW-THIS-WEEK:END -->

---

---

## Quick Start

> **New to x402?** Three steps to your first payment.

**1. Pick a facilitator**

| Use case | Facilitator |
|----------|-------------|
| Most chains, full SDK support | [Coinbase CDP](https://docs.cdp.coinbase.com/x402) |
| Edge deployment, global latency | [Cloudflare x402](https://developers.cloudflare.com/workers/examples/x402) |
| Enterprise billing + disputes | [Stripe Machine Payments](https://docs.stripe.com/payments/machine/x402) |

**2. Install the SDK**

```bash
# TypeScript
npm install @coinbase/x402-express

# Python
pip install x402

# Rust
cargo add x402
```

**3. Add payment middleware**

```typescript
import { paymentMiddleware } from '@coinbase/x402-express';

app.use(paymentMiddleware(wallet, {
  '/api/data': { price: '$0.01', network: 'base-mainnet' }
}));
```

That's it. The middleware returns 402 with payment details, verifies the client's payment header, and lets the request through.

[Full quickstart →](https://docs.cdp.coinbase.com/x402/quickstart-for-sellers) · [Testnet setup →](https://docs.cdp.coinbase.com/x402/network-support)

---

## How x402 Works

```
1. Client  →  GET /api/data                              (initial request)
2. Server  ←  402 Payment Required                       (payment details in header)
               X-Payment-Required: {amount, address, network}
3. Client  →  EIP-3009 gasless USDC transfer             (client signs + submits)
4. Client  →  GET /api/data  +  X-Payment: {signed tx}  (retry with payment)
5. Facilitator  →  verify + settle on-chain              (~2 seconds)
6. Server  ←  200 OK  +  X-Payment-Response              (resource returned)
```

No gas for the sender. No subscription. No API key. Payment IS authentication.

[Protocol spec →](https://github.com/coinbase/x402) · [EIP-3009 →](https://eips.ethereum.org/EIPS/eip-3009)

---

## Need More?

This README is the front door. The full curated directory — every shelf, every entry — is in [`directory/`](directory/).

**Other lists worth knowing:** the community [awesome-x402](https://github.com/x402-foundation/awesome-x402) accepts everything and is the right place for exhaustive coverage. [Glama](https://glama.ai/mcp/servers) indexes MCP servers at enormous scale and publishes its own health data, which is rarer than it should be. Different jobs. Use all three.

---

## Contributing

gold-402 is curated, not exhaustive. Every entry earns its place.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the curation standard, badge system, acceptance criteria, and submission process.

**Quick rules:**
- Entry must use the x402 protocol (HTTP 402 + X-Payment), not just USDC or general crypto payments.
- Live URL or public GitHub repo. Link must work.
- Last activity within 12 months (for libraries and resources without a live endpoint).
- One entry per pull request. Format: `[Name](url) — Description starting uppercase, ending with period.`
- Descriptions are factual. No marketing language.

---

<p align="center">
  <b>Curated by <a href="https://24klabs.ai">24K Labs</a></b><br>
  <sub>If this saved you time, star the repo.</sub><br><br>
  <a href="https://24klabs.ai">24klabs.ai</a> •
  <a href="https://x402.org">x402.org</a> •
  <a href="https://github.com/coinbase/x402">Protocol Spec</a> •
  <a href="https://docs.cdp.coinbase.com/x402">Coinbase Docs</a> •
  <a href="https://discord.gg/x402">Discord</a> •
  <a href="https://agenteconomy.to">Live Dashboard</a>
</p>
