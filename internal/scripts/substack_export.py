#!/usr/bin/env python3
"""Export a repo essay to a Substack-ready markdown file, and track sync drift.

Usage:
  python3 internal/scripts/substack_export.py <essay.md>   # export one essay
  python3 internal/scripts/substack_export.py --status     # sync drift report

Export rewrites relative links so a single copy-paste into
md-to-substack -> Substack produces no broken links:

  ./foo.md          -> that essay's Substack post (slug from its frontmatter),
                       falling back to its mattsly.com URL if it has no slug
  ./foo.html        -> https://www.mattsly.com/fair-and-simple-tax-act/foo.html
  ./assets/bar.png  -> https://www.mattsly.com/fair-and-simple-tax-act/assets/bar.png
  #anchor           -> https://www.mattsly.com/fair-and-simple-tax-act/<essay>.html#anchor

Slugs live in each essay's YAML frontmatter:

  substack_slug: the-lifetime-gains-framework
  substack_synced: 2026-06-16   # date the Substack post last matched Git

AFTER EVERY SUBSTACK SYNC, UPDATE substack_synced. `--status` compares each
essay's last Git commit date against substack_synced and flags drift.

FALLBACK_META covers published essays that don't yet have YAML frontmatter
(adding frontmatter changes which github-pages plugins process them, so
migrate those only after eyeballing `make serve`). Frontmatter wins when both
exist.
"""

import re
import subprocess
import sys
from pathlib import Path

BASE = "https://www.mattsly.com/fair-and-simple-tax-act/"
SUBSTACK = "https://taxrefactor.substack.com/p/"

# stem -> (slug, last-synced date). Only for essays WITHOUT frontmatter.
FALLBACK_META = {
    "warren-wealth-tax-oped-v7": ("senator-warren-is-right-about-the", "2026-04-09"),
    "gemstone-essay": ("the-magic-gemstone", "2026-03-28"),
    "dear-tech-bros": ("dear-tech-bros-stop-whining-about", "2026-05-07"),
    "trump-accounts-essay": ("trump-accounts-great-idea-bad-product", "2026-06-01"),
}

REPO_ROOT = Path(__file__).resolve().parents[2]


def frontmatter(path: Path) -> dict:
    """Cheap YAML frontmatter reader (flat string keys only)."""
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return {}
    m = re.match(r"\A---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        kv = re.match(r"^([A-Za-z0-9_-]+):\s*(.+?)\s*$", line)
        if kv:
            out[kv.group(1)] = kv.group(2).strip("\"'")
    return out


def essay_meta(stem: str) -> tuple[str | None, str | None]:
    """(slug, synced) for a root essay, frontmatter first, fallback second."""
    fm = frontmatter(REPO_ROOT / f"{stem}.md")
    slug = fm.get("substack_slug")
    synced = fm.get("substack_synced")
    if not slug and stem in FALLBACK_META:
        slug, fb_synced = FALLBACK_META[stem]
        synced = synced or fb_synced
    return slug, synced


def export(essay_arg: str) -> int:
    essay_path = (REPO_ROOT / essay_arg).resolve()
    if not essay_path.exists():
        print(f"error: {essay_path} not found")
        return 1

    text = essay_path.read_text(encoding="utf-8")
    text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL)

    rewrites: list[tuple[str, str]] = []
    self_url = BASE + essay_path.stem + ".html"

    def sub(pattern: str, repl_fn, s: str) -> str:
        def _wrapped(m: re.Match) -> str:
            new = repl_fn(m)
            rewrites.append((m.group(0), new))
            return new

        return re.sub(pattern, _wrapped, s)

    def md_target(stem: str) -> str:
        slug, _ = essay_meta(stem)
        if slug:
            return SUBSTACK + slug
        if stem == "index":
            return BASE
        return f"{BASE}{stem}.html"

    # ](./foo.md) -> Substack post URL (fallback: mattsly.com)
    text = sub(
        r"\]\(\.?/?([A-Za-z0-9_-]+)\.md\)",
        lambda m: f"]({md_target(m.group(1))})",
        text,
    )
    # ](./foo.html), ](./assets/...), any other relative path -> mattsly.com
    text = sub(r"\]\(\./([^)#\s]+)\)", lambda m: f"]({BASE}{m.group(1)})", text)
    # ](#anchor) -> absolute self URL + anchor (never leaks a tool domain)
    text = sub(r"\]\(#([^)\s]+)\)", lambda m: f"]({self_url}#{m.group(1)})", text)

    out_dir = REPO_ROOT / "internal" / "substack-exports"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{essay_path.stem}.substack.md"
    out_path.write_text(text, encoding="utf-8")

    print(f"wrote {out_path.relative_to(REPO_ROOT)}")
    print(f"{len(rewrites)} link(s) rewritten:")
    for old, new in rewrites:
        print(f"  {old}  ->  {new}")

    leftovers = re.findall(r"\]\((?:\./|#)[^)]*\)", text)
    if leftovers:
        print("\nWARNING: unrewritten relative links remain:")
        for link in leftovers:
            print(f"  {link}")
    print("\nReminder: after pasting to Substack, update substack_synced "
          f"in {essay_path.name} to today's date.")
    return 0


def last_commit_date(path: Path) -> str:
    out = subprocess.run(
        ["git", "log", "-1", "--format=%cs", "--", str(path)],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    return out.stdout.strip()


def status() -> int:
    stems = sorted(
        p.stem for p in REPO_ROOT.glob("*.md")
        if essay_meta(p.stem)[0] is not None
    )
    drifted = 0
    print(f"{'essay':<32} {'last commit':<12} {'synced':<12} status")
    for stem in stems:
        slug, synced = essay_meta(stem)
        commit = last_commit_date(REPO_ROOT / f"{stem}.md")
        stale = bool(commit and synced and commit > synced)
        drifted += stale
        flag = "DRIFTED — needs Substack sync" if stale else "ok"
        print(f"{stem + '.md':<32} {commit:<12} {synced or '?':<12} {flag}")
    print(f"\n{drifted} essay(s) out of sync.")
    return 0


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    if sys.argv[1] == "--status":
        return status()
    return export(sys.argv[1])


if __name__ == "__main__":
    sys.exit(main())
