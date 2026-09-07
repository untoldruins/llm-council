# Sekaidao — static marketing site

A 1:1 recreation of the seven Sekaidao design mockups as a working, responsive
static site. No framework, no runtime dependencies — a small Python generator
renders plain HTML that you can host anywhere.

## Quick start

```bash
cd sekaidao
python3 build.py            # renders dist/
python3 build.py --serve    # renders, then serves on http://localhost:4173
```

`build.py` has no third-party dependencies (standard library only). The output
in `dist/` also opens directly from the filesystem — every link and asset path
is relative, so `open dist/index.html` works without a server.

## Layout

```
sekaidao/
├── build.py            entry point: renders every page into dist/
├── src/
│   ├── content.py      all page copy, as ordered (component, kwargs) blocks
│   ├── components.py   the HTML component library + site-wide constants
│   └── icons.py        inline SVG icon set (24×24, inherits currentColor)
├── static/
│   ├── css/site.css    design system: tokens, components, responsive rules
│   ├── js/site.js      mobile nav + FAQ accordion (progressive enhancement)
│   └── img/            photography, logo, favicon
└── dist/               generated — do not edit by hand
```

Pages are declared as data. To change copy, edit `src/content.py`; to change how
a block looks, edit the matching function in `src/components.py` and every page
using it updates.

## Pages

| Page | Source mockup |
| --- | --- |
| `/index.html` | `image55` |
| `/services/managed-it-support.html` | `image44` |
| `/services/microsoft-365.html` | `image0` |
| `/services/cybersecurity-compliance.html` | `image6` |
| `/services/cloud-migration-backup.html` | `image3` |
| `/services/it-consulting-vcio.html` | `image4` |
| `/about.html` | `image1` |
| `/services/network-setup-troubleshooting.html` | — built on-system |
| `/services/index.html` | — built on-system |
| `/blog.html`, `/contact.html`, `/faqs.html` | — built on-system |

The site navigation and footer list six services, but the mockups only cover
five of them. **Network Setup & Troubleshooting** has no mockup, so it was
composed from the same components and design language as its siblings — same
hero, challenge columns, six-up service grid, process steps, and FAQ. The
services index, blog, contact, and FAQ pages were built the same way, because
the header links to them.

## Design tokens

Colours were sampled from the mockup pixels rather than guessed:

| Token | Value | Used for |
| --- | --- | --- |
| `--navy-900` | `#0d274c` | hero and footer ground |
| `--navy-800` | `#122a56` | top utility bar |
| `--navy-700` | `#143270` | solid "real results" cards |
| `--blue-500` | `#275de1` | icons, step numbers, links |
| `--orange-500` | `#ea6533` | primary CTA |
| `--surface-soft` | `#f5f8fd` | alternating sections |
| `--surface-blue` | `#f0f7fd` | pale blue sections |

Type is Inter (Google Fonts) with a system fallback stack, so the layout holds
if the webfont is blocked.

## Imagery

The mockups are flat JPEGs, so there were no separate photo assets to work
from. The photography in `static/img/` was cropped out of the mockups
themselves and upscaled, which keeps the site visually identical to the design
at the cost of resolution — these are placeholders to swap for the originals.

Two consequences worth knowing:

- **Hero images are the clean right-hand portion of each mockup hero.** The
  headline text is re-rendered in HTML over a CSS gradient, so it is real,
  selectable, translatable text rather than pixels.
- **Section photos still carry their caption text baked in** (for example
  "REAL-WORLD EXPERIENCE. REAL IMPACT." on `founder.jpg`). The `split`
  component supports a CSS caption overlay via `caption=` / `caption_sub=`, but
  it is deliberately unused — turning it on would print the caption twice.
  When you replace these crops with clean originals, pass those arguments to
  get the overlay back.

Vendor lockups (CompTIA Security+, AWS, Microsoft) are drawn in CSS as
approximations. Replace `_vendor_mark()` in `src/components.py` with the real
trademarked logos before going live.

## Notes before launch

- The contact form has no backend. `site.js` intercepts the submit and shows a
  notice; point the `<form>` at your handler or CRM to make it live.
- Blog posts, reviews, and the three article thumbnails are the placeholder
  content shown in the mockups.
- Social links in the footer are `#` placeholders.
