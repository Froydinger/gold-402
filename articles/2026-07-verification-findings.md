# Three-Quarters of the x402 Bazaar Is Dead

> 24K Labs Verification Report -- July 2026
>
> 22,545 endpoints probed. 5,792 live. 74% unreachable.

---

## The number that changes how you read every x402 list

The CDP Bazaar is the largest index of x402-enabled services. It is not curated. Any developer can list an endpoint, and thousands have. The Bazaar currently lists 22,545 services across every category: APIs, MCP servers, data feeds, AI inference, on-chain tools.

We probed all of them.

**74.3% did not return a valid 402 response.** The endpoint was gone, the server returned the wrong status, or the payment details were malformed. We verified 5,792 services as live -- meaning they responded with a proper 402 Payment Required header, valid payment metadata, and a reachable payment endpoint. The rest: dead.

This is not a critique of x402. It is a characteristic of any open listing ecosystem at velocity. Developers ship, pivot, take services down, iterate. The Bazaar reflects everything that has ever been listed. It cannot reflect what is actually running right now.

That is the gap gold-402 exists to close.

---

## Methodology

We hit each service's API endpoint directly with a standard HTTP GET request and checked the response.

A service is **verified** if it returns HTTP 402 with a well-formed `X-Payment-Required` or equivalent payment header -- proof that the endpoint is live and the x402 payment flow is functional.

A service is **failed** if it returns any other status (200, 404, 500, connection refused, DNS failure). A service is **timeout** if it does not respond within 10 seconds.

A service that fails two consecutive probes is **delisted** -- its status is set inactive and it drops out of the active catalog. Delisting is a lifecycle flag on failed services, not a separate outcome: the 2,068 services delisted to date are counted within the 16,686 failed, not alongside them.

We make no attempt to actually pay. Verification is a probe, not a transaction. The probe can be reproduced: the full crawler is open source at `scripts/verify.py`.

Run date: July 1, 2026. Total probed: 22,545.

---

## What we found

| Status | Count | Share |
|--------|-------|-------|
| Verified live | 5,792 | 25.7% |
| Failed | 16,686 | 74.0% |
| Timeout | 67 | 0.3% |
| **Total probed** | **22,545** | |

Three in four x402 endpoints in the CDP Bazaar are unreachable. One in four is actually live.

The failure rate is not evenly distributed across categories. Developer tooling dominates the verified set -- 2,170 of the 5,792 verified services are developer tools, which skews toward production infrastructure with stable uptime. Agent automation (926 verified), Finance / DeFi (572), and Data (432) follow. The long tail includes security, compliance, identity, and gaming services.

---

## What is actually live

The 5,792 verified services span a meaningful cross-section of the x402 economy.

**Pricing.** Verified services range from free tier (0 USDC, typically for discovery or trial endpoints) to $100 per call for specialized professional data. The average is $0.51 per call. The majority cluster in the $0.001--$0.05 range: micropayments for data retrieval, on-chain queries, AI inference tokens.

**Usage signal.** The CDP Bazaar tracks calls and unique payers over rolling 30-day windows. Among verified services, the leaders by real payer count:

- **CuseTheJuice Mail** -- agent email on Base USDC. 1,151+ unique payers across endpoints.
- **Exa Search** -- neural web search, 247 payers, 8,625 calls.
- **Onesource** -- Ethereum transaction and chain data (eth_getTransactionByHash, ENS resolve, contract introspection). 250--291 payers per endpoint, consistent across the suite.
- **ENS resolve** -- 277 payers.
- **Tavily Search** -- 73 payers.

These are not vanity numbers. Each payer represents a wallet that completed an on-chain USDC transfer to call the service. They are paying agents -- automated systems hitting APIs at scale, per-call, no subscriptions.

**Infrastructure with real traction.** Onesource alone has more than 291 unique payers across its Ethereum data endpoints. This is the real signal beneath the raw Bazaar counts: a small number of services have achieved genuine recurring use at the agent layer.

---

## Why the dead rate is the moat

The 74% failure rate is not a problem. It is the reason a verified catalog has value.

An agent that trusts the raw CDP Bazaar list will attempt to pay endpoints that no longer exist. It will burn gas on failed probes, build integrations against services that have gone dark, and fail in unpredictable ways when a "listed" service returns 500 instead of 402. The failure is not always immediate -- a service might pass one day and go dark the next. Without continuous verification, lists go stale.

gold-402's verified catalog is a filter on top of the open listing layer. It does not replace the Bazaar. It answers a different question: of everything listed, what is actually working right now?

The monthly probe run refreshes this answer on the 1st of every month. The open-source crawler (`scripts/verify.py`) can be run on demand against any snapshot. The verification methodology is documented and reproducible.

---

## The editorial layer

Verification is necessary but not sufficient for quality. A service can return 402 correctly and still offer little value: thin data, redundant endpoints, missing documentation, unclear pricing.

gold-402 maintains a separate editorial layer -- the README and the curated directory pages -- for services that have cleared the verification bar and earned a place in the hand-curated picks. That layer is smaller: roughly 300 entries out of 5,792 verified, selected for clarity, usefulness, and signal.

The full verified catalog is available via the gold-402 API (`gold-402-api-production.up.railway.app`). The editorial picks are in the README.

---

## The finding in one sentence

Of 22,545 x402 services listed in the CDP Bazaar, 5,792 are live as of July 1, 2026. The other 16,753 are not. Knowing the difference is what the verified catalog is for.

---

*Methodology: HTTP GET probe, 10-second timeout, valid 402 response with payment metadata required for verified status. Full probe source at `scripts/verify.py`. Refreshed monthly via GitHub Actions. Data current as of July 1, 2026.*

*gold-402 is curated by [24K Labs](https://24klabs.ai). Verification report by Nox.*
