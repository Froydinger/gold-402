# gold-402

> The gold standard for x402 resources. **464 curated entries** — every one checked by hand before it was listed. No filler. No dead links.

[![GitHub stars](https://img.shields.io/github/stars/Haustorium12/gold-402?style=social)](https://github.com/Haustorium12/gold-402)
[![Last Commit](https://img.shields.io/github/last-commit/Haustorium12/gold-402)](https://github.com/Haustorium12/gold-402/commits/main)
[![Curated by 24K Labs](https://img.shields.io/badge/Curated_by-24K_Labs-gold)](https://24klabs.ai)

The big catalogs list everything ever submitted — that's their job, and it's why most of what's in them is dead. We measured it: **67–79% of the free-listing catalogs no longer answer.**

gold-402 is the other thing. Smaller on purpose. A person checked every entry, we publish what we checked and what we didn't, and in July 2026 we started **buying services and reporting what came back** — which as far as we can tell nobody else in this ecosystem does.

---

## The Directory

The product. 464 entries across 13 shelves, in [`directory/`](directory/).

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

In July 2026 we ran the first paid delivery check across our own shelf — actually buying services and recording what came back.

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

> ★ **July 2026** — [**24K Labs Verification Report: Three-Quarters of the x402 Bazaar Is Dead**](articles/2026-07-verification-findings.md) by [24K Labs](https://24klabs.ai)

[![24K Featured](https://img.shields.io/badge/24K_Featured-2026--07-C0C0C0?style=plastic)](FEATURED.md)

We probed all 22,545 x402 services in the CDP Bazaar. 5,792 answered. The rest were gone, misconfigured, or unreachable — 74% dead.

The Bazaar records everything ever listed; it can't tell you what runs today. That gap is the whole argument for a checked catalog.

[Read the full report →](articles/2026-07-verification-findings.md) · [Past features →](FEATURED.md)

---

## This Week in x402

_Week of July 20–26, 2026_

- **The x402 Foundation is live.** The Linux Foundation announced its operational launch on July 14, with 40 members and Coinbase's contribution of the protocol complete — 17 of them premier, including Adyen, AWS, American Express, Circle, Cloudflare, Coinbase, Fiserv, Google, Mastercard, MoonPay, Ripple, Shopify, the Solana and Stellar foundations, Stripe, and Visa. The standard now sits under open governance rather than one company's roadmap, and an executive-director search and a technical steering committee are underway. [[Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-operational-launch-of-x402-foundation-to-standardize-internet-native-payments-for-ai-agents-and-applications)]
- **Ripple and MoonPay buy in.** Ripple joined with production data, not a pitch — more than 1M agentic transactions on the XRP Ledger and a June-shipped XRPL AI Starter Kit; MoonPay took a board seat. [[Genfinity](https://genfinity.io/2026/07/14/x402-foundation-launch-ripple-stellar-solana-quant-premier-members/)]
- **The numbers, unvarnished.** x402 moved about $24M across 75M transactions in the last 30 days — roughly 94k buyers, 22k sellers, an average payment near 32¢. That's the whole thesis: charges too small for a card network to touch, working as designed. It's also a fraction of what any premier member clears in a day. Both true. [[CoinDesk](https://www.coindesk.com/tech/2026/07/15/visa-mastercard-and-ripple-join-the-standard-letting-ai-agents-pay-in-stablecoins)]

---

<!-- NEW-THIS-WEEK:START -->
## New This Week

**This week** (Jul 27—Aug 2)

- **[NEAR x402 Facilitator](https://x402.mikedotexe.com/)** — Open-source, API-key-gated facilitator for exact Circle USDC payments on NEAR and Base. It sponsors relayer gas and persists settlements for recovery. [Source](https://github.com/fastnear/x402-near-facilitator) and sanitized paid-flow evidence for [NEAR](https://github.com/fastnear/x402-near-facilitator/blob/main/docs/evidence/2026-07-26-v041-near-mainnet-canary.md) and [Base](https://github.com/fastnear/x402-near-facilitator/blob/main/docs/evidence/2026-07-26-v041-base-mainnet-canary.md).
- **[x402 FixSpec](https://github.com/am5188/x402-fixspec)** — Deterministic endpoint conformance and remediation tool that inspects unpaid challenges, validates Base USDC requirements, probes discovery documents, and returns OpenAPI, Bazaar, and agent-instruction templates. [Live x402 offer](https://fixspec.am518.uk/buy/fixspec).
- **[modelprices.xyz](https://modelprices.xyz)** — Normalized LLM market data: per-token prices, context windows, and capability limits for 2,000+ models across 70+ providers, cross-checked hourly against two upstreams. Single-model lookups $0.002, cheapest-model queries $0.005 (ranked by blended $/request), full tables $0.01, price-change feed $0.02. Provenance on every row: source URL, first-observed date, confidence tier. USDC on Base. ([OpenAPI](https://modelprices.xyz/openapi.json)) ([llms.txt](https://modelprices.xyz/llms.txt))
- **[Hermes Plant Action Safety](https://hermesplant.com/api/agent-services/action-safety/quick)** — Deterministic pre-execution gate for agent shell, Git, SQL, infrastructure, and deployment actions, with a $0.01 quick check and a $0.25 signed-receipt workflow on Base.
- **[GBLIN Protocol](https://gblin.digital/agents)** — Treasury and risk data for a NAV-backed basket token on Base (cbBTC/WETH/USDC) with an automated on-chain crash-response policy. 7 endpoints: NAV and basket state, market risk regime attestation, MEV-safe swap quotes, wallet treasury health, and just-in-time redemption calldata to convert holdings to USDC when an invoice arrives. $0.001-$0.005 USDC on Base via the Coinbase CDP facilitator. ([x402](https://gblin.digital/.well-known/x402)) ([MCP](https://www.npmjs.com/package/@gblin-protocol/mcp-server))
- **[ArisPay](https://facilitator.arispay.app)** — Free, public x402 facilitator on Base mainnet with USDC and EURC settlement. Open /verify and /settle, no API key or signup. Machine-readable fee policy and discovery at [/supported](https://facilitator.arispay.app/supported) and [/facilitator](https://facilitator.arispay.app/facilitator).
- **[The Bot Wire](https://thebotwire.com)** — 57 primary-source data wires for AI agents: SEC EDGAR, Federal Register, federal court opinions, congressional bills, DOJ, FDA, Federal Reserve and ECB, BLS/BEA releases, CISA CVEs, cloud outages, NWS alerts, USGS quakes, arXiv, WHO/CDC, European Commission, GOV.UK, NASA, EIA, plus 40 curated news sources. $0.005–$0.01 USDC on Base, free 3-result preview on every wire. Example: `GET /fed/latest?src=fomc&since=30d`. ([Manifest](https://thebotwire.com/.well-known/x402)) ([OpenAPI](https://thebotwire.com/openapi.json)) ([Routing table](https://thebotwire.com/llms-full.txt))
- **[botwire-mcp](https://www.npmjs.com/package/botwire-mcp)** — The Bot Wire as MCP tools: 57 real-time primary-source wires (SEC EDGAR, Federal Register, federal courts, DOJ, FDA, Fed/ECB, BLS/BEA, CISA, NWS, USGS, arXiv) paid per call in USDC on Base. Free preview tier works with no wallet configured. Remote endpoint at [thebotwire.com/mcp](https://thebotwire.com/mcp) or `npx botwire-mcp`. ([GitHub](https://github.com/ArasPasha/botwire-mcp))
- **[minia2a.uk](https://minia2a.uk)** — Open M2M micropayment marketplace. 174 x402-payable services across 50+ categories (crypto data, web scraping, email verification, token security, agent toolkits). 115 registered AI agents. 5% fee, USDC settlement on Base. MCP registry, CLI, and 5-minute hands-on tutorial.

**Last week** (Jul 20—26)

- **[Fabler Labs x402 Storefront](https://fablerlabs.com/x402/)** — Security and utility APIs for AI agents on Base, USDC per call, no signup: secret scan ($0.005), agent-config audit ($0.05), diff security gate ($0.10), pre-deploy evidence gate ($0.08), URL security evidence ($0.08), plus data and rendering endpoints and digital-product downloads; free machine-readable catalog at GET https://x402.fablerlabs.com/. Built and operated end-to-end by an autonomous AI agent.
- **[x402-seller](https://x402-seller-m8nx.onrender.com)** — Token rug/honeypot scoring combining GoPlus static analysis with live Honeypot.is sell simulation, liquidity-drain detection from a self-collected reserve time-series, and market data. EVM + Solana. $0.001-$0.05 USDC on Base. ([Track record](https://x402-seller-m8nx.onrender.com/track-record))
- **[Groundcheck](https://groundcheck.seiche.info)** — Claim grounding and delivery attestation for AI agents: machine-verified verdicts (supported/refuted/unverified) with confidence scores and cited sources, plus signed offline-verifiable receipts binding an x402 payment to what was delivered. Free single-claim tier; paid endpoints $0.005–$0.05 USDC on Base. ([OpenAPI](https://groundcheck.seiche.info/openapi.json)) ([npm](https://www.npmjs.com/package/groundcheck-mcp))
- **[Mart402](https://mart402.com)** — Web and PDF extraction for AI agents: URL-to-Markdown extraction, PDF parsing with dual-engine OCR consensus (hallucination detection, calibrated confidence, Japanese-strong), invoice field verification, schema-driven structured extraction, and JP company profiles. $0.001–$0.02 USDC on Base; free Sepolia sandbox at mart402.dev. ([Docs](https://mart402.com/agents.md)) ([GitHub](https://github.com/tanaka-77/mart402-agent-kit))
- **[Apiosk](https://apiosk.com)** — MCP gateway to discover, pay for, execute, and publish x402 APIs. Buyers settle per call over USDC/x402 or prepaid credits; providers publish paid routes that pay 98% of each call to their own wallet. Hosted at mcp.apiosk.com/mcp and listed in the official MCP Registry as io.github.obcraft/apiosk-mcp. USDC on Base. `npx @apiosk/mcp`. ([npm](https://www.npmjs.com/package/@apiosk/mcp)) ([PyPI](https://pypi.org/project/apiosk-mcp/)) ([GitHub](https://github.com/obcraft/apiosk-mcp))
- **[VirtualSMS](https://virtualsms.io/api/v1/x402/sms-verify)** — SMS verification and OTP receiving for AI agents: real carrier numbers across 145+ countries and 2500+ services, no account or API key. Also number rentals, matching-country proxies, and a hosted MCP server at mcp.virtualsms.io. USDC on Base, BNB Chain, and Solana.
- **[402Found](https://402found.dev)** — Marketplace of 18 specialized AI agent microservices: PII scrubbing, hallucination detection, prompt injection detection, format conversion, agent permission checks, and more. Each service is independently pay-per-request via x402 in USDC on Base.
- **[token-risk](https://token-risk.com)** — Deterministic structural risk reports for ERC-20 tokens and wallet addresses on Base via x402 USDC per request.
- **[Zugabot Code Agent](https://zugabot.ai/x402)** — AI developer services: code review, bug fix, test generation, docs, refactor, security audit, architecture review, full-repo audit. USDC on Base.
- **[Macro Pulse](https://macro-pulse-x402.onrender.com)** — Pay-per-call macroeconomic indicator API sourced from the World Bank (GDP growth, inflation, unemployment trend). Single-country lookup $0.02, 8-country flat-priced batch endpoint $0.05, 6-hour response caching. USDC on Base.
- **[Stelar Digital](https://api.stelardigital.com)** — Live crypto grid-trading telemetry (real P&L, not simulated), grid-parameter recommendations, market-regime classification, and sentiment scoring. 8 endpoints, $0.005-$2.50 USDC on Base. ([x402](https://api.stelardigital.com/.well-known/x402))
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
  <a href="https://x402.org">x402.org</a> •
  <a href="https://github.com/coinbase/x402">Protocol Spec</a> •
  <a href="https://docs.cdp.coinbase.com/x402">Coinbase Docs</a> •
  <a href="https://discord.gg/x402">Discord</a> •
  <a href="https://agenteconomy.to">Live Dashboard</a>
</p>
