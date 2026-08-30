#!/usr/bin/env python3
"""readme_numbers.py — keep the README's entry count equal to the shelf.

WHY THIS EXISTS
---------------
On 2026-08-30 the README's headline read "459 curated entries" while the shelves held
506. Off by forty-seven. Nobody lied; the number was typed by hand once and every merge
after that made it a little more wrong. It is the first sentence a stranger reads and it
is the product claim.

The fix is not "remember to update it." A rule enforced by remembering is not a rule --
that same day the boot card's own hard line cap was overshot twice in two days for
exactly this reason. So the number is computed from the files and written by a machine.

WHAT THIS OWNS, AND WHAT IT DOES NOT
------------------------------------
It owns ONLY what sits between the fence markers:

    <!--COUNT:START-->506<!--COUNT:END-->
    <!--SHELVES:START-->13<!--SHELVES:END-->

Everything else in the README is human prose and this script must never touch it. The
marker pattern is borrowed from NEW-THIS-WEEK, which has worked here since it shipped.

**It deliberately does NOT police the CLAIMS.** The same audit that found 459-vs-506 also
found "No dead links." standing as an absolute the shelf could not support, and "every one
checked by hand" surviving past the day the Submission Gate started verifying submissions
by itself. No cron would ever have caught either. Those need a human read after every
merge -- that is a separate standing rule and this script is not a substitute for it. If
you are reading this because you assumed the bot had the README covered: it has the
NUMBERS covered. That is all.

FAIL CLOSED
-----------
This has write access to the public front door. A wrong number written confidently by a
machine is worse than a stale one, because nobody re-checks a bot -- that is precisely how
the 24K Vault's monthly audit filed a passing report every month for four months while
checking nothing. So: if any shelf is missing, unreadable, or parses to zero entries, this
refuses to write anything and opens a ticket. A partial count is never published.

TICKETS
-------
Failures file an issue in the `web` seat's name, never `sean`'s -- a bot that cannot count
a shelf is seat-fixable work, and Sean's queue is reserved for what only he can do.

It files on STATE CHANGE ONLY. If a ticket for this condition is already open it adds a
comment instead of opening a second one. Thirty identical issues in a month would teach
everyone to ignore the queue, which is worse than no bot at all, because then the signal
is buried instead of merely absent.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request

REPO = os.environ.get("GITHUB_REPOSITORY", "Haustorium12/gold-402")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
DIRECTORY = os.path.join(ROOT, "directory")

# The canonical shelf list. Named explicitly rather than globbed: a glob silently
# counts a new file as a shelf and silently stops noticing a deleted one. If a shelf
# is genuinely added, this list is the deliberate act that admits it.
SHELVES = [
    "apis", "mcp-servers", "sdks", "facilitators", "frameworks", "tools",
    "security", "ecosystem", "aggregators", "global", "learning",
    "community", "market-data",
]

# An entry is a top-level markdown bullet opening with a link. Same shape the
# CONTRIBUTING format mandates: `- [Name](url) — Description.`
ENTRY = re.compile(r"^- \[", re.MULTILINE)

TICKET_TAG = "[readme-numbers]"  # how this bot recognises its own open ticket


def api(method: str, path: str, payload: dict | None = None):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        method=method,
        data=json.dumps(payload).encode() if payload else None,
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": "gold-402-readme-numbers",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read() or "{}")


def report_failure(title_suffix: str, body: str) -> None:
    """Open a ticket, or comment on the one already open. Never both, never a second."""
    if not TOKEN:
        print("no token — cannot file a ticket; failing loudly instead", file=sys.stderr)
        return
    try:
        existing = api("GET", f"/repos/{REPO}/issues?state=open&per_page=100")
        for issue in existing:
            if "pull_request" in issue:
                continue
            if TICKET_TAG in issue.get("title", ""):
                api(
                    "POST",
                    f"/repos/{REPO}/issues/{issue['number']}/comments",
                    {"body": f"Still failing on a later run.\n\n{body}"},
                )
                print(f"commented on existing ticket #{issue['number']}")
                return
        created = api(
            "POST",
            f"/repos/{REPO}/issues",
            {
                "title": f"{TICKET_TAG} {title_suffix}",
                "labels": ["web", "bug"],
                "body": body,
            },
        )
        print(f"opened ticket #{created['number']}")
    except urllib.error.HTTPError as exc:
        # Ticketing failing must not be silent either.
        print(f"could not file ticket: HTTP {exc.code} {exc.reason}", file=sys.stderr)


def count_shelves() -> tuple[dict[str, int], list[str]]:
    counts: dict[str, int] = {}
    problems: list[str] = []
    for shelf in SHELVES:
        path = os.path.join(DIRECTORY, f"{shelf}.md")
        if not os.path.exists(path):
            problems.append(f"`directory/{shelf}.md` — MISSING")
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except OSError as exc:
            problems.append(f"`directory/{shelf}.md` — unreadable ({exc})")
            continue
        n = len(ENTRY.findall(text))
        if n == 0:
            problems.append(f"`directory/{shelf}.md` — parsed to ZERO entries")
        counts[shelf] = n
    return counts, problems


def replace_fenced(text: str, marker: str, value: str) -> tuple[str, int]:
    pattern = re.compile(
        rf"(<!--{marker}:START-->)(.*?)(<!--{marker}:END-->)", re.DOTALL
    )
    if not pattern.search(text):
        return text, -1  # marker absent — caller treats as fatal
    new_text, n = pattern.subn(rf"\g<1>{value}\g<3>", text)
    return new_text, n


def main() -> int:
    counts, problems = count_shelves()

    if problems:
        detail = "\n".join(f"- {p}" for p in problems)
        body = (
            "**The README count was NOT written. Failing closed on purpose.**\n\n"
            "A partial count published confidently is worse than a stale one, because "
            "nobody re-checks a bot.\n\n"
            f"### What went wrong\n\n{detail}\n\n"
            "### What the README still says\n\n"
            "Whatever it said before this run. It was not touched.\n\n"
            "### Done looks like\n\n"
            "The shelf files above parse again, this workflow runs green, and the "
            "count in the README matches the shelves.\n\n"
            f"_Filed automatically by `scripts/readme_numbers.py`. Owner `web` — a bot "
            f"that cannot count a shelf is seat-fixable work._"
        )
        report_failure("shelf files did not parse — README count not written", body)
        print("FAILED CLOSED — README untouched", file=sys.stderr)
        for p in problems:
            print(f"  {p}", file=sys.stderr)
        return 1

    total = sum(counts.values())
    shelves = len(counts)

    text = open(README, encoding="utf-8").read()
    original = text

    text, hits_count = replace_fenced(text, "COUNT", str(total))
    text, hits_shelves = replace_fenced(text, "SHELVES", str(shelves))

    if hits_count == -1 or hits_shelves == -1:
        body = (
            "**The fence markers are gone from README.md, so the count could not be "
            "written and nothing was changed.**\n\n"
            "This bot only ever edits what sits between:\n\n"
            "```\n<!--COUNT:START-->…<!--COUNT:END-->\n"
            "<!--SHELVES:START-->…<!--SHELVES:END-->\n```\n\n"
            "If those are missing, someone rewrote that part of the README by hand "
            "and dropped them. **That is not a crisis — but until the markers are back, "
            "the entry count is hand-maintained again**, which is the exact condition "
            "that produced 459-vs-506 on 2026-08-30.\n\n"
            f"Live count from the shelves right now: **{total}** across **{shelves}** shelves.\n\n"
            "### Done looks like\n\nMarkers restored around both numbers; this runs green.\n"
        )
        report_failure("fence markers missing from README — count not written", body)
        print("FAILED CLOSED — markers absent", file=sys.stderr)
        return 1

    breakdown = "  ".join(f"{k}={v}" for k, v in counts.items())
    if text == original:
        print(f"no change — README already says {total} across {shelves} shelves")
        print(f"  {breakdown}")
        return 0

    open(README, "w", encoding="utf-8").write(text)
    print(f"README count updated -> {total} across {shelves} shelves")
    print(f"  {breakdown}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
