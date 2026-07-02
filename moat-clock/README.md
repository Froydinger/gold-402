# Moat-Clock

The accruing record of the gold-402 catalog's liveness over time.

## Why this exists

A curated list can be copied in an afternoon. A *dated* record of honest
observations cannot — you cannot backdate an observation you did not make.
The moat-clock is what turns "the catalog is 25.7% live today" into "we have
watched this ecosystem decay, observation by observation, since 2026-07-01."
That claim — *we have watched longest* — is an advantage no rival can purchase
or counterfeit. It is amassed one honest observation at a time.

It is the dated spine under two things:
- the verification-findings work (the "~74% dead" story needs a *series* to say
  "we watched it decay over time," not just a single snapshot);
- the "independent registry" claim (which leans on "we've watched longest").

## The one rule that gives it worth

**Observations are append-only. A past observation is never edited or deleted.**

The clock's entire value is that its history is untampered. An edited series is
worth nothing — it is no longer evidence, just assertion. If a past number was
wrong, the correction is a *new* observation with a `correction_of` note, never
a rewrite of the old line. Guard this as fiercely as the catalog itself.

## Schema — `series.jsonl`

One JSON object per line (JSON Lines), one line per observation run. Fields:

| field                 | meaning |
|-----------------------|---------|
| `observed_at`         | ISO-8601 UTC — when the observation was recorded |
| `source`              | the artifact observed (e.g. `directory/services.json`) |
| `source_generated_at` | the source's own generation timestamp, if it has one |
| `records`             | total records observed |
| `verified`            | count with `verify_status == verified` |
| `failed`              | count with `verify_status == failed` |
| `timeout`             | count with `verify_status == timeout` |
| `verified_pct`        | verified / records, to 1 decimal |
| `notes`               | free text — anomalies, corrections, methodology changes |

Add fields over time (append to the schema, never repurpose an existing field's
meaning). Downstream readers must tolerate unknown fields.

## How to append (each session that runs a fresh count)

```bash
python3 - <<'EOF'
import json, collections, datetime
d = json.load(open('directory/services.json'))
svcs = d.get('services', [])
b = collections.Counter(s.get('verify_status','(missing)') for s in svcs if isinstance(s, dict))
n = sum(b.values())
obs = {
  "observed_at": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
  "source": "directory/services.json",
  "source_generated_at": d.get('generated_at'),
  "records": n,
  "verified": b.get('verified',0),
  "failed": b.get('failed',0),
  "timeout": b.get('timeout',0),
  "verified_pct": round(100*b.get('verified',0)/n, 1) if n else None,
  "notes": ""
}
with open('moat-clock/series.jsonl','a') as f:
    f.write(json.dumps(obs) + "\n")
print("appended:", obs)
EOF
```

Then one commit: `moat-clock: observation YYYY-MM-DD`. Never `git push --force`
this file. Never rewrite a prior line.

_Kept by The Registry (LEDGER). Started 2026-07-01._
