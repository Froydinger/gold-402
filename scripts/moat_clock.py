# scripts/moat_clock.py
# Gold-402: moat clock
# Reads directory/services.json and appends ONE dated summary row to
# directory/moat-history.jsonl. Append-only -- never overwrites, never rewrites
# prior rows. This is the time-series that backs the "we've watched the x402
# ecosystem the longest" claim. Its value is entirely in not losing days.
#
# Designed to run in the verify GitHub Action immediately AFTER verify.py, so it
# captures freshly-probed data (verified counts are meaningful only post-verify).
#
# No external deps -- pure stdlib.

import json
import os
import sys
from datetime import datetime, timezone

SERVICES_PATH = "directory/services.json"
HISTORY_PATH = "directory/moat-history.jsonl"


def build_summary(services_path=SERVICES_PATH):
    """Read services.json and return one summary dict for today."""
    with open(services_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    services = data.get("services", [])
    total = len(services)

    verified_live = sum(1 for s in services if s.get("verified") is True)
    inactive = sum(1 for s in services if s.get("status") == "inactive")

    # verify_status distribution (pending / live / failed / etc.)
    status_counts = {}
    for s in services:
        vs = s.get("verify_status") or "unknown"
        status_counts[vs] = status_counts.get(vs, 0) + 1

    # source distribution -- tracks single-source dependency over time
    source_counts = {}
    for s in services:
        src = s.get("source") or "unknown"
        source_counts[src] = source_counts.get(src, 0) + 1

    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_services": total,
        "verified_live": verified_live,
        "inactive": inactive,
        "verify_status": status_counts,
        "sources": source_counts,
        "services_generated_at": data.get("generated_at"),
    }


def last_recorded_date(history_path=HISTORY_PATH):
    """Return the date string of the last row in the history file, or None."""
    if not os.path.exists(history_path):
        return None
    last = None
    with open(history_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                last = json.loads(line).get("date")
            except json.JSONDecodeError:
                continue
    return last


def append_row(summary, history_path=HISTORY_PATH):
    """Append one JSONL row. Idempotent per day: skips if today already logged."""
    today = summary["date"]
    if last_recorded_date(history_path) == today:
        print(f"moat_clock: {today} already recorded -- skipping (append-only, no dup).")
        return False

    os.makedirs(os.path.dirname(history_path), exist_ok=True)
    line = json.dumps(summary, ensure_ascii=False)
    # Append-only. We never open in 'w'. A row, once written, is permanent.
    with open(history_path, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(
        f"moat_clock: recorded {today} -- "
        f"{summary['total_services']} services, "
        f"{summary['verified_live']} verified live."
    )
    return True


def main():
    try:
        summary = build_summary()
    except FileNotFoundError:
        print(f"moat_clock: {SERVICES_PATH} not found -- nothing to record.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"moat_clock: {SERVICES_PATH} is not valid JSON -- {e}", file=sys.stderr)
        sys.exit(1)

    append_row(summary)


if __name__ == "__main__":
    main()
