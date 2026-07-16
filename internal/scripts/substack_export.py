#!/usr/bin/env python3
"""Export a repo essay to Substack-ready form, and track sync drift.

Usage:
  python3 internal/scripts/substack_export.py <essay.md>   # write .substack.md
  python3 internal/scripts/substack_export.py --copy <essay.md>
        # render to rich text and put it on the macOS clipboard, ready to
        # paste straight into the Substack editor (replaces md-to-substack).
        # Also writes a .substack.html preview you can open in a browser.
        # Requires the 'markdown' package once: pip3 install markdown
  python3 internal/scripts/substack_export.py --status     # sync drift report

Link rewriting (both modes):
  ./foo.md, ./foo.html -> that essay's Substack post (slug from frontmatter),
                          falling back to its mattsly.com URL if no slug
  ./assets/bar.png     -> https://www.mattsly.com/fair-and-simple-tax-act/assets/bar.png
  #anchor              -> https://www.mattsly.com/fair-and-simple-tax-act/<essay>.html#anchor

Slugs live in each essay's YAML frontmatter:

  substack_slug: the-lifetime-gains-framework
  substack_synced: 2026-06-16   # date the Substack post last matched Git

AFTER EVERY SUBSTACK SYNC, UPDATE substack_synced. `--status` compares each
essay's last Git commit date against substack_synced and flags drift.

FALLBACK_META covers published essays that don't yet have YAML frontmatter
(adding frontmatter changes which github-pages plugins process them, so
migrate those only after eyeballing `make serve`). Frontmatter wins when both
exist. ADD NEW POSTS' SLUGS TO FRONTMATTER ON PUBLICATION DAY.
"""

import re
import subprocess
import sys
from pathlib import Path

BASE = "https://www.mattsly.com/fair-and-simple-tax-act/"
SUBSTACK = "https://taxrefactor.substack.com/p/"

# stem -> (slug, last-synced date). Only for essays WITHOUT frontmatter.
FALLBACK_META = {
    "warren-wealth-tax-oped-v7": ("senator-warren-is-right-about-the", "2026-07-16"),
    "gemstone-essay": ("the-magic-gemstone", "2026-07-16"),
    "dear-tech-bros": ("dear-tech-bros-stop-whining-about", "2026-07-16"),
    "trump-accounts-essay": ("trump-accounts-great-idea-bad-product", "2026-07-16"),
}

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "internal" / "substack-exports"


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


def transform(essay_path: Path) -> tuple[str, list[tuple[str, str]]]:
    """Strip frontmatter and absolutize every relative link."""
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

    text = sub(
        r"\]\(\.?/?([A-Za-z0-9_-]+)\.(?:md|html)\)",
        lambda m: f"]({md_target(m.group(1))})",
        text,
    )
    text = sub(r"\]\(\./([^)#\s]+)\)", lambda m: f"]({BASE}{m.group(1)})", text)
    text = sub(r"\]\(#([^)\s]+)\)", lambda m: f"]({self_url}#{m.group(1)})", text)
    return text, rewrites


def report(rewrites: list[tuple[str, str]], text: str) -> None:
    print(f"{len(rewrites)} link(s) rewritten:")
    for old, new in rewrites:
        print(f"  {old}  ->  {new}")
    leftovers = re.findall(r"\]\((?:\./|#)[^)]*\)", text)
    if leftovers:
        print("\nWARNING: unrewritten relative links remain:")
        for link in leftovers:
            print(f"  {link}")


def resolve(essay_arg: str) -> Path | None:
    p = (REPO_ROOT / essay_arg).resolve()
    if not p.exists():
        print(f"error: {p} not found")
        return None
    return p


def export(essay_arg: str) -> int:
    essay_path = resolve(essay_arg)
    if not essay_path:
        return 1
    text, rewrites = transform(essay_path)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{essay_path.stem}.substack.md"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {out_path.relative_to(REPO_ROOT)}")
    report(rewrites, text)
    print("\nReminder: after pasting to Substack, update substack_synced "
          f"in {essay_path.name} to today's date.")
    return 0


def copy(essay_arg: str) -> int:
    essay_path = resolve(essay_arg)
    if not essay_path:
        return 1
    try:
        import markdown  # type: ignore
    except ImportError:
        print("The --copy mode needs the 'markdown' package (one-time setup):")
        print("  pip3 install markdown")
        return 1

    text, rewrites = transform(essay_path)
    html = markdown.markdown(
        text,
        extensions=["extra", "smarty", "sane_lists"],  # smarty = curly quotes
    )

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    html_path = OUT_DIR / f"{essay_path.stem}.substack.html"
    html_path.write_text(html, encoding="utf-8")
    report(rewrites, text)
    print(f"\nwrote {html_path.relative_to(REPO_ROOT)} (browser-openable preview)")

    if sys.platform == "darwin":
        hexed = html.encode("utf-8").hex()
        result = subprocess.run(
            ["osascript", "-e", f"set the clipboard to «data HTML{hexed}»"],
            capture_output=True, text=True,
        )
        if result.returncode == 0:
            print("Rich text is on your clipboard. Paste directly into the "
                  "Substack editor, then update substack_synced.")
        else:
            print(f"clipboard failed ({result.stderr.strip()}); open the "
                  ".html preview, select all, and copy from the browser.")
    else:
        print("(Not macOS: open the .html preview in a browser, select all, "
              "copy, and paste into Substack.)")
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
    args = sys.argv[1:]
    if args == ["--status"]:
        return status()
    if len(args) == 2 and args[0] == "--copy":
        return copy(args[1])
    if len(args) == 1 and not args[0].startswith("-"):
        return export(args[0])
    print(__doc__)
    return 1


if __name__ == "__main__":
    sys.exit(main())
