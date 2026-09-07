#!/usr/bin/env python3
"""Build the static Sekaidao site into `dist/`.

    python build.py            # build
    python build.py --serve    # build, then serve dist/ on http://localhost:4173

Pages are declared in `src/content.py` as ordered lists of (component, kwargs)
blocks; components live in `src/components.py`.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
sys.path.insert(0, str(ROOT / "src"))

import components as C  # noqa: E402
from content import PAGES  # noqa: E402

DIST = ROOT / "dist"
STATIC = ROOT / "static"

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" href="{favicon}" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
</head>
<body>
{topbar}
{header}
<main id="main">
{body}
</main>
{footer}
<script src="{js}"></script>
</body>
</html>
"""


def render_page(url: str, page: dict) -> str:
    ctx = C.Ctx(url)
    body = []
    for name, kwargs in page["blocks"]:
        fn = getattr(C, name)
        body.append(fn(ctx, **kwargs))

    return SHELL.format(
        title=C.e(page["title"]),
        description=C.e(page["description"]),
        favicon=ctx.asset("static/img/favicon.svg"),
        css=ctx.asset("static/css/site.css"),
        js=ctx.asset("static/js/site.js"),
        topbar=C.topbar(ctx),
        header=C.header(ctx),
        body="\n".join(body),
        footer=C.footer(ctx, **page.get("footer", {})),
    )


def build() -> int:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    shutil.copytree(STATIC, DIST / "static")

    for url, page in PAGES.items():
        out = DIST / url.lstrip("/")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(url, page), encoding="utf-8")
        print(f"  {url:52s} {len(out.read_text(encoding='utf-8')):>7,} bytes")

    print(f"\nBuilt {len(PAGES)} pages -> {DIST}")
    return 0


def serve(port: int = 4173) -> None:
    import functools
    import http.server
    import socketserver

    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(DIST))
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving {DIST} at http://localhost:{port}/  (Ctrl-C to stop)")
        httpd.serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--serve", action="store_true", help="serve dist/ after building")
    ap.add_argument("--port", type=int, default=4173)
    args = ap.parse_args()

    build()
    if args.serve:
        serve(args.port)
