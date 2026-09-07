"""HTML component functions for the Sekaidao site.

Each function returns a fragment of markup. Pages in `content.py` are declared as
lists of (component_name, kwargs) blocks and rendered by `build.py`.
"""

from __future__ import annotations

from html import escape

from icons import icon

# --------------------------------------------------------------------------
# Site-wide constants (single source of truth for NAP details)
# --------------------------------------------------------------------------
PHONE = "215-432-8300"
PHONE_HREF = "tel:+12154328300"
EMAIL = "contact@sekaidao.com"
DOMAIN = "sekaidao.com"
CITY = "Philadelphia, PA"
TAGLINE = "Reliable IT. Stronger Businesses."
STRAPLINE = "Secure Systems. Stronger Businesses."

SERVICES = [
    ("Managed IT Support", "/services/managed-it-support.html"),
    ("Microsoft 365 Setup & Administration", "/services/microsoft-365.html"),
    ("Cybersecurity & Compliance", "/services/cybersecurity-compliance.html"),
    ("Cloud Migration & Backup", "/services/cloud-migration-backup.html"),
    ("Network Setup & Troubleshooting", "/services/network-setup-troubleshooting.html"),
    ("IT Consulting / vCIO Services", "/services/it-consulting-vcio.html"),
]

NAV = [
    ("Home", "/index.html", None),
    ("Services", "/services/index.html", SERVICES),
    ("About", "/about.html", None),
    ("Blog", "/blog.html", None),
    ("Contact", "/contact.html", None),
]

QUICK_LINKS = [
    ("Home", "/index.html"),
    ("Services", "/services/index.html"),
    ("About", "/about.html"),
    ("Blog", "/blog.html"),
    ("Contact", "/contact.html"),
]


def e(text: str) -> str:
    return escape(str(text), quote=True)


def _rel(href: str, depth: int) -> str:
    """Rewrite a root-relative href to be relative, so the build works from file://."""
    if href.startswith(("http://", "https://", "mailto:", "tel:", "#")):
        return href
    return ("../" * depth) + href.lstrip("/")


class Ctx:
    """Per-page render context (current URL + directory depth)."""

    def __init__(self, url: str):
        self.url = url
        self.depth = url.strip("/").count("/")

    def href(self, h: str) -> str:
        return _rel(h, self.depth)

    def asset(self, path: str) -> str:
        return ("../" * self.depth) + path.lstrip("/")


# --------------------------------------------------------------------------
# Small shared pieces
# --------------------------------------------------------------------------
def btn(label, href="/contact.html", variant="primary", arrow=True, ico=None, *, ctx):
    inner = ""
    if ico:
        inner += icon(ico)
    inner += e(label)
    if arrow:
        inner += icon("arrow-right")
    return f'<a class="btn btn--{variant}" href="{ctx.href(href)}">{inner}</a>'


def quote_btn(ctx, variant="primary", label="Get a Free Quote"):
    return btn(label, "/contact.html", variant, True, None, ctx=ctx)


def phone_btn(ctx, variant="ghost"):
    return f'<a class="btn btn--{variant}" href="{PHONE_HREF}">{icon("phone")}{PHONE}</a>'


def arrow_link(label, href, ctx, caps=False):
    cls = "arrow-link arrow-link--caps" if caps else "arrow-link"
    return f'<a class="{cls}" href="{ctx.href(href)}">{e(label)}{icon("arrow-right")}</a>'


def _vendor_mark(kind: str) -> str:
    """CSS-drawn vendor lockups (CompTIA Security+, AWS, Microsoft)."""
    if kind == "securityplus":
        return '<div class="badge-sec"><i>CompTIA</i><b>Security+</b></div>'
    if kind == "aws":
        return '<div class="badge-aws">aws</div>'
    if kind == "microsoft":
        return '<div class="badge-ms"><i></i><i></i><i></i><i></i></div>'
    return ""


def _icon_or_mark(name: str) -> str:
    if name.startswith("mark:"):
        return _vendor_mark(name.split(":", 1)[1])
    return icon(name)


# --------------------------------------------------------------------------
# Chrome: top bar, header, footer
# --------------------------------------------------------------------------
def topbar(ctx) -> str:
    return f"""
<div class="topbar">
  <div class="container topbar__inner">
    <div class="topbar__left">{icon("shield-check")}<span>Trusted IT support for small businesses.</span></div>
    <div class="topbar__right">
      <a class="topbar__phone" href="{PHONE_HREF}">{icon("phone")}{PHONE}</a>
      <span class="topbar__sep">|</span>
      <a href="{ctx.href('/index.html')}">{icon("globe")}{DOMAIN}</a>
    </div>
  </div>
</div>"""


def header(ctx) -> str:
    items = []
    for label, href, children in NAV:
        current = ctx.url == href or (children and ctx.url.startswith("/services/"))
        aria = ' aria-current="page"' if current else ""
        if children:
            menu = "".join(
                f'<a href="{ctx.href(h)}">{e(t)}</a>' for t, h in
                [("All Services", "/services/index.html")] + list(children)
            )
            items.append(
                f'<li class="nav__item nav__item--has-menu">'
                f'<a class="nav__link" href="{ctx.href(href)}"{aria}>{e(label)}{icon("chevron-down")}</a>'
                f'<div class="nav__menu">{menu}</div></li>'
            )
        else:
            items.append(
                f'<li class="nav__item"><a class="nav__link" href="{ctx.href(href)}"{aria}>{e(label)}</a></li>'
            )

    return f"""
<header class="header">
  <div class="container header__inner">
    <a class="brand" href="{ctx.href('/index.html')}">
      <img src="{ctx.asset('static/img/logo.svg')}" alt="" width="34" height="34">
      <span class="brand__name">SEKAIDAO</span>
    </a>
    <button class="header__toggle" data-nav-toggle aria-expanded="false" aria-label="Toggle navigation">{icon("menu")}</button>
    <nav class="nav" data-nav data-open="false" aria-label="Primary">
      <ul class="nav__list">{''.join(items)}</ul>
      {quote_btn(ctx)}
    </nav>
    <div class="header__cta">{quote_btn(ctx)}</div>
  </div>
</header>"""


def footer(ctx, *, partner=True, socials=("linkedin", "facebook", "youtube")) -> str:
    svc = "".join(f'<a href="{ctx.href(h)}">{e(t)}</a>' for t, h in SERVICES)
    quick = "".join(f'<a href="{ctx.href(h)}">{e(t)}</a>' for t, h in QUICK_LINKS)
    soc = "".join(
        f'<a href="#" aria-label="{e(s.capitalize())}">{icon(s)}</a>' for s in socials
    )
    partner_col = ""
    if partner == "tomorrow":
        partner_col = f"""
      <div class="footer__partner footer__partner--tomorrow">
        {icon('globe')}
        <span>Technology</span><span>a brighter</span><span>tomorrow</span>
      </div>"""
    elif partner:
        partner_col = f"""
      <div class="footer__partner">
        {_vendor_mark('microsoft')}
        <strong>Microsoft</strong>
        <span>Solutions Partner</span>
        <span>Modern Work</span>
      </div>"""

    return f"""
<footer class="footer">
  <div class="container">
    <div class="footer__grid">
      <div>
        <a class="brand" href="{ctx.href('/index.html')}">
          <img src="{ctx.asset('static/img/logo.svg')}" alt="" width="34" height="34">
          <span class="brand__name">SEKAIDAO</span>
        </a>
        <p class="footer__tagline">{TAGLINE}</p>
        <div class="socials">{soc}</div>
      </div>
      <div><h4>Services</h4><div class="footer__links">{svc}</div></div>
      <div><h4>Quick Links</h4><div class="footer__links">{quick}</div></div>
      <div>
        <h4>Get In Touch</h4>
        <ul class="footer__contact">
          <li>{icon("phone")}<a href="{PHONE_HREF}">{PHONE}</a></li>
          <li>{icon("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{icon("globe")}<a href="{ctx.href('/index.html')}">{DOMAIN}</a></li>
          <li>{icon("pin")}<span>{CITY}</span></li>
        </ul>
      </div>{partner_col}
    </div>
    <div class="footer__bar">
      <span>&copy; 2024 Sekaidao. All rights reserved.</span>
      <span class="tagline">{STRAPLINE}</span>
    </div>
  </div>
</footer>"""


# --------------------------------------------------------------------------
# Page blocks
# --------------------------------------------------------------------------
def hero(ctx, *, image, h1, lede, eyebrow=None, crumbs=None, subhead=None,
         pills=(), actions=True) -> str:
    top = ""
    if crumbs:
        parts = []
        for i, (label, href) in enumerate(crumbs):
            if i:
                parts.append("<span>/</span>")
            parts.append(f'<a href="{ctx.href(href)}">{e(label)}</a>' if href else f"<span>{e(label)}</span>")
        top = f'<div class="hero__crumbs">{"".join(parts)}</div>'
    elif eyebrow:
        top = f'<span class="eyebrow">{e(eyebrow)}</span>'

    sub = f'<p class="hero__sub">{e(subhead)}</p>' if subhead else ""

    acts = ""
    if actions:
        acts = f'<div class="hero__actions">{quote_btn(ctx)}{phone_btn(ctx)}</div>'

    pill_html = ""
    if pills:
        cells = "".join(
            f'<div class="hero__pill">{_icon_or_mark(ic)}<div><strong>{e(t)}</strong>'
            + (f"<span>{e(s)}</span>" if s else "")
            + "</div></div>"
            for ic, t, s in pills
        )
        pill_html = f'<div class="hero__pills">{cells}</div>'

    return f"""
<section class="hero">
  <div class="hero__bg" style="background-image:url('{ctx.asset('static/img/' + image)}')"></div>
  <div class="container hero__inner">
    <div class="hero__content">
      {top}
      <h1>{e(h1)}</h1>
      {sub}
      <p class="hero__lede">{e(lede)}</p>
      {acts}
    </div>
    {pill_html}
  </div>
</section>"""


def trustbar(ctx, *, items) -> str:
    cells = "".join(
        f'<div class="trustbar__item"><div class="trustbar__icon">{_icon_or_mark(ic)}</div>'
        f'<div><div class="trustbar__title">{e(t)}</div>'
        + (f'<div class="trustbar__text">{e(s)}</div>' if s else "")
        + "</div></div>"
        for ic, t, s in items
    )
    return f'<section class="trustbar"><div class="container trustbar__inner">{cells}</div></section>'


def _head(eyebrow=None, heading=None, lede=None, align="center") -> str:
    if not (eyebrow or heading or lede):
        return ""
    cls = "section__head" + ("" if align == "center" else " section__head--left")
    out = f'<div class="{cls}">'
    if eyebrow:
        out += f'<span class="eyebrow">{e(eyebrow)}</span>'
    if heading:
        out += f"<h2>{e(heading)}</h2>"
    if lede:
        out += f'<p class="section__lede">{e(lede)}</p>'
    return out + "</div>"


def cards(ctx, *, items, cols=4, variant="center", eyebrow=None, heading=None,
          lede=None, bg=None, align="center", plain=False) -> str:
    """Grid of icon cards.

    `items` entries are dicts: {icon, title, text, link?, link_label?, question?}
    `variant`: center | slim | row | navy | service
    """
    out = []
    for it in items:
        klass = "plaincol" if plain else f"card card--hover card--{variant}"
        icon_cls = "card__icon"
        if it.get("accent") == "orange":
            icon_cls += " card__icon--orange"
        if it.get("chip"):
            icon_cls += " card__icon--chip"

        body = ""
        if variant == "row":
            body += f'<div class="{icon_cls}">{_icon_or_mark(it["icon"])}</div><div>'
        else:
            body += f'<div class="{icon_cls}">{_icon_or_mark(it["icon"])}</div>'

        if it.get("question"):
            body += f'<p class="card__q">{e(it["question"])}</p>'
        body += f'<h3>{e(it["title"])}</h3>'
        if it.get("text"):
            body += f'<p>{e(it["text"])}</p>'
        if it.get("link"):
            body += arrow_link(it.get("link_label", "Learn More"), it["link"], ctx,
                               caps=it.get("caps", False))
        if variant == "row":
            body += "</div>"

        out.append(f'<div class="{klass}">{body}</div>')

    grid_cls = "grid" if plain else "grid"
    section_cls = "section" + (f" section--{bg}" if bg else "")
    return f"""
<section class="{section_cls}">
  <div class="container">
    {_head(eyebrow, heading, lede, align)}
    <div class="{grid_cls} grid--{cols}">{''.join(out)}</div>
  </div>
</section>"""


def split(ctx, *, image, body_heading, body_paragraphs, eyebrow=None, caption=None,
          caption_sub=None, caption_top=False, cta=None, aside=None, checks=None,
          bg=None, reverse=False, wide_media=False, body_first=False) -> str:
    cap = ""
    if caption:
        cap_cls = "media__caption media__caption--top" if caption_top else "media__caption"
        sub = f"<small>{e(caption_sub)}</small>" if caption_sub else ""
        cap = f'<div class="{cap_cls}">{e(caption)}{sub}</div>'

    media = (f'<figure class="media" style="margin:0">'
             f'<img src="{ctx.asset("static/img/" + image)}" alt="" loading="lazy">{cap}</figure>')

    paras = "".join(f"<p>{e(p)}</p>" for p in body_paragraphs)
    eb = f'<span class="eyebrow">{e(eyebrow)}</span>' if eyebrow else ""
    cta_html = quote_btn(ctx) if cta is True else (
        btn(cta[0], cta[1], "primary", True, None, ctx=ctx) if cta else "")

    checks_html = ""
    if checks:
        lis = "".join(f'<li>{icon("badge-check")}<span>{e(c)}</span></li>' for c in checks)
        checks_html = f'<ul class="check-list">{lis}</ul>'

    body = f'<div class="split__body">{eb}<h2>{e(body_heading)}</h2>{paras}{checks_html}{cta_html}</div>'

    aside_html = ""
    cls = "split"
    if aside:
        cls += " split--with-aside"
        rows = "".join(
            f'<div class="aside-list__item">{_icon_or_mark(a["icon"])}'
            f'<div><h4>{e(a["title"])}</h4>'
            + (f'<p>{e(a["text"])}</p>' if a.get("text") else "")
            + "</div></div>"
            for a in aside
        )
        aside_html = f'<div class="aside-list">{rows}</div>'
    elif reverse:
        cls += " split--reverse"
    elif wide_media:
        cls += " split--wide-media"

    if reverse:
        inner = f"{body}{media}"
    elif body_first:
        inner = f"{body}{media}{aside_html}"
    else:
        inner = f"{media}{body}{aside_html}"
    section_cls = "section" + (f" section--{bg}" if bg else "")
    return f'<section class="{section_cls}"><div class="container"><div class="{cls}">{inner}</div></div></section>'


def process(ctx, *, steps, eyebrow=None, heading=None, lede=None, bg=None,
            boxed=True, arrows=True, step_icons=False) -> str:
    cells = []
    for i, s in enumerate(steps, 1):
        ic = f'{icon(s["icon"])}' if (step_icons and s.get("icon")) else ""
        box = " process__step--boxed" if boxed else ""
        cells.append(
            f'<div class="process__step{box}"><div class="process__num">{i}</div>'
            f'<div><h3>{ic}{e(s["title"])}</h3><p>{e(s["text"])}</p></div></div>'
        )
        if arrows and i < len(steps):
            cells.append(f'<div class="process__arrow">{icon("arrow-right")}</div>')

    wrap_cls = "process" + ("" if boxed else " process--divided")
    section_cls = "section" + (f" section--{bg}" if bg else "")
    return f"""
<section class="{section_cls}">
  <div class="container">
    {_head(eyebrow, heading, lede)}
    <div class="{wrap_cls}">{''.join(cells)}</div>
  </div>
</section>"""


def faqs(ctx, *, items, heading, eyebrow="Frequently Asked Questions", cols=2,
         bg=None, view_all=True, sign="chevron-down", show_icon=True, expanded=False) -> str:
    blocks = []
    op = " open" if expanded else ""
    for q, a in items:
        ic = f'<span class="faq-item__icon">{icon("badge-check")}</span>' if show_icon else ""
        blocks.append(
            f'<details class="faq-item"{op}><summary>{ic}'
            f'<span class="faq-item__q">{e(q)}</span>'
            f'<span class="faq-item__sign">{icon(sign)}</span></summary>'
            f'<div class="faq-item__a">{e(a)}</div></details>'
        )

    va = f'<div>{btn("View All FAQs", "/faqs.html", "outline", True, None, ctx=ctx)}</div>' if view_all else ""
    section_cls = "section" + (f" section--{bg}" if bg else "")
    return f"""
<section class="{section_cls}">
  <div class="container">
    <div class="faq__head">
      <div><span class="eyebrow">{e(eyebrow)}</span><h2>{e(heading)}</h2></div>
      {va}
    </div>
    <div class="faq__grid faq__grid--{cols}" data-faq-group>{''.join(blocks)}</div>
  </div>
</section>"""


def ctaband(ctx, *, heading, lede=None, eyebrow=None, label="Get a Free Quote") -> str:
    eb = f'<span class="eyebrow">{e(eyebrow)}</span>' if eyebrow else ""
    ld = f"<p>{e(lede)}</p>" if lede else ""
    return f"""
<section class="ctaband">
  <div class="ctaband__bg"></div>
  <div class="container ctaband__inner">
    <div>{eb}<h2>{e(heading)}</h2>{ld}{quote_btn(ctx, label=label)}</div>
    <div class="ctaband__tag">Technology<br>a brighter<br>tomorrow</div>
  </div>
</section>"""


def reviews(ctx, *, items, heading, eyebrow, note=None) -> str:
    stars = '<div class="stars">' + icon("star") * 5 + "</div>"
    cards_html = "".join(
        f'<div class="card review">{stars}<h3>{e(r["title"])}</h3>'
        f'<p>&ldquo;{e(r["quote"])}&rdquo;</p><cite>&mdash; {e(r["author"])}</cite></div>'
        for r in items
    )
    note_html = f'<p class="section__lede" style="text-align:right">{e(note)}</p>' if note else ""
    return f"""
<section class="section">
  <div class="container">
    <div class="faq__head">
      <div><span class="eyebrow">{e(eyebrow)}</span><h2>{e(heading)}</h2></div>
      {note_html}
    </div>
    <div class="grid grid--3">{cards_html}</div>
  </div>
</section>"""


def posts(ctx, *, items, heading, eyebrow, view_all=True) -> str:
    cards_html = "".join(
        f'<div class="post"><div class="post__thumb">'
        f'<img src="{ctx.asset("static/img/" + p["image"])}" alt="" loading="lazy"></div>'
        f'<div><h3>{e(p["title"])}</h3><p>{e(p["text"])}</p>'
        f'{arrow_link("Read More", "/blog.html", ctx)}</div></div>'
        for p in items
    )
    va = f'<div>{btn("View All Articles", "/blog.html", "outline", True, None, ctx=ctx)}</div>' if view_all else ""
    return f"""
<section class="section">
  <div class="container">
    <div class="faq__head">
      <div><span class="eyebrow">{e(eyebrow)}</span><h2>{e(heading)}</h2></div>
      {va}
    </div>
    <div class="grid grid--3">{cards_html}</div>
  </div>
</section>"""


def promos(ctx, *, items) -> str:
    cards_html = "".join(
        f'<div class="card promo"><span class="chip">{icon(p["icon"])}</span>'
        f'<div><h3>{e(p["title"])}</h3><p>{e(p["text"])}</p>'
        f'{arrow_link(p["link_label"], p["link"], ctx)}</div></div>'
        for p in items
    )
    return f'<section class="section section--tight"><div class="container"><div class="grid grid--2">{cards_html}</div></div></section>'


def rich(ctx, *, html) -> str:
    """Escape hatch for one-off page bodies (blog / contact / FAQs)."""
    return html
