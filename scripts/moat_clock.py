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
# Churn sidecar (Fix 4): the full id set lives here, one id per line, so the
# history row can carry new/churned COUNTS without bloating the time-series.
IDS_SIDECAR_PATH = "directory/moat-ids-latest.txt"


def read_id_sidecar(path=IDS_SIDECAR_PATH):
    """Return the set of service ids from the churn sidecar, or empty set."""
    if not os.path.exists(path):
        return set()
    ids = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                ids.add(line)
    return ids


def write_id_sidecar(ids, path=IDS_SIDECAR_PATH):
    """Overwrite the sidecar with one id per line (sorted for stable diffs)."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for sid in sorted(ids):
            f.write(sid + "\n")


def build_summary(services_path=SERVICES_PATH, ids_sidecar_path=IDS_SIDECAR_PATH):
    """Read services.json and return (summary_dict, today_id_set) for today.

    The id set is returned so the caller can refresh the churn sidecar ONLY
    after the row is actually committed -- keeping the churn baseline aligned
    with the recorded history (a same-day re-run must not move the baseline)."""
    with open(services_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    services = data.get("services", [])
    total = len(services)

    # Fix 1: liveness reads verify_status, not the `verified` int field.
    # In this schema `verified` is a probe counter (0 on every service today),
    # not a boolean -- reading `verified is True` printed verified_live: 0 on
    # every historical row even when verify_status showed thousands live.
    verified_live = sum(1 for s in services if s.get("verify_status") == "verified")
    inactive = sum(1 for s in services if s.get("status") == "inactive")

    # verify_status distribution (pending / verified / failed / timeout / ...)
    status_counts = {}
    for s in services:
        vs = s.get("verify_status") or "unknown"
        status_counts[vs] = status_counts.get(vs, 0) + 1

    # source distribution -- tracks single-source dependency over time
    source_counts = {}
    for s in services:
        src = s.get("source") or "unknown"
        source_counts[src] = source_counts.get(src, 0) + 1

    # Fix 3: usage signal -- which of these services are actually being paid
    # for. CDP hands us l30DaysTotalCalls / l30DaysUniquePayers per service
    # (stored as quality_calls_30d / quality_payers_30d). This is the
    # "which of N actually matter" signal the bare headcount throws away.
    total_calls_30d = sum((s.get("quality_calls_30d") or 0) for s in services)
    total_payers_30d = sum((s.get("quality_payers_30d") or 0) for s in services)
    services_with_usage = sum(
        1 for s in services if (s.get("quality_payers_30d") or 0) > 0
    )
    top_by_payers = [
        {
            "id": s.get("id"),
            "name": s.get("name"),
            "payers_30d": s.get("quality_payers_30d") or 0,
            "calls_30d": s.get("quality_calls_30d") or 0,
        }
        for s in sorted(
            [s for s in services if s.get("id")],
            key=lambda s: (s.get("quality_payers_30d") or 0),
            reverse=True,
        )[:10]
    ]

    # Fix 4: churn -- diff today's id set against the sidecar from the last
    # recorded run. Counts go in the row; the full id set stays in the sidecar.
    today_ids = {s.get("id") for s in services if s.get("id")}
    prev_ids = read_id_sidecar(ids_sidecar_path)
    if prev_ids:
        new_services = len(today_ids - prev_ids)
        churned_services = len(prev_ids - today_ids)
    else:
        # No sidecar baseline -- genuine first run, OR a lost baseline (a partial
        # write, manual repo surgery, or a checkout predating the sidecar
        # commit). We cannot know the churn without a baseline, so record null
        # rather than a misleading 0 that a reader could not tell apart from a
        # real no-churn day. The sidecar written on append makes the next run
        # real. (The brief omits the +new/-gone clause when these are null.)
        new_services = None
        churned_services = None

    summary = {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "captured_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "total_services": total,
        "verified_live": verified_live,
        "inactive": inactive,
        "verify_status": status_counts,
        "sources": source_counts,
        "total_calls_30d": total_calls_30d,
        "total_payers_30d": total_payers_30d,
        "services_with_usage": services_with_usage,
        "top_by_payers": top_by_payers,
        "new_services": new_services,
        "churned_services": churned_services,
        "services_generated_at": data.get("generated_at"),
    }
    return summary, today_ids


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
        summary, today_ids = build_summary()
    except FileNotFoundError:
        print(f"moat_clock: {SERVICES_PATH} not found -- nothing to record.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"moat_clock: {SERVICES_PATH} is not valid JSON -- {e}", file=sys.stderr)
        sys.exit(1)

    if append_row(summary):
        # Refresh the churn baseline only when a new row was actually recorded,
        # so a same-day re-run (idempotent skip) never erases the baseline.
        write_id_sidecar(today_ids)


if __name__ == "__main__":
    main()
