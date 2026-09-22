#!/usr/bin/env python3
"""Builds marcellspaper.com as plain HTML from the page content in content.py.
Run: python3 tools/build_site.py  -> writes site/*.html. No framework, no
build step on Cloudflare: Pages just serves the folder."""
import os, html, datetime
from content import PAGES, IMAGES

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
PHONE = "(773) 265-1200"; PHONE_TEL = "+17732651200"; FAX = "(773) 265-1220"
EMAIL = "info@marcellspaper.com"
ADDR = "4221 W Ferdinand St, Chicago, IL 60624"
PORTAL = "https://portal.marcellspaper.com"
NAV = [("Home", "index.html"), ("About", "about.html"), ("Equipment", "equipment.html"),
       ("Services", "services.html", [("Services overview", "services.html"),
                                      ("Metal Waste Collection", "metal-waste-collection.html"),
                                      ("Paper Waste Collection", "paper-waste-collection.html"),
                                      ("Metal Recycling", "metal-recycling.html"),
                                      ("Paper Recycling", "paper-recycling.html")]),
       ("Contact", "contact.html"), ("FAQ", "faq.html"), ("Client Login", PORTAL)]

def nav_html(current):
    out = []
    for item in NAV:
        label, href = item[0], item[1]
        subs = item[2] if len(item) > 2 else None
        active = ' class="active"' if href == current or (subs and any(s[1] == current for s in subs)) else ""
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        if subs:
            out.append(f'<li class="has-sub"><a href="{href}"{active}>{label} &#9662;</a><ul>' +
                       "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in subs) + "</ul></li>")
        else:
            out.append(f'<li><a href="{href}"{active}{ext}>{label}</a></li>')
    return "".join(out)

def page(slug, title, desc, body, current=None):
    current = current or slug
    year = datetime.date.today().year
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://marcellspaper.com/assets/hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.png">
<link rel="stylesheet" href="styles.css">
</head>
<body>
<div class="topbar"><div class="wrap">
  <span>Recycling paper &amp; metal in Chicago since the 1970s</span>
  <span><a href="tel:{PHONE_TEL}">{PHONE}</a> &nbsp;|&nbsp; <a href="mailto:{EMAIL}">{EMAIL}</a></span>
</div></div>
<header class="site"><div class="wrap">
  <a class="brand" href="index.html"><img src="assets/logo.webp" alt="Marcells Paper &amp; Metal"></a>
  <button class="menu-btn" aria-label="Menu" onclick="document.querySelector('nav.main').classList.toggle('open')">&#9776;</button>
  <nav class="main"><ul>{nav_html(current)}</ul></nav>
</div></header>
{body}
<footer class="site"><div class="wrap">
  <div><h4>Marcells Paper &amp; Metal Inc</h4>
    <p>{ADDR}<br>Phone: <a href="tel:{PHONE_TEL}">{PHONE}</a><br>Fax: {FAX}<br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    <p><a class="btn" href="contact.html">Request a quote</a></p></div>
  <div><h4>Services</h4><ul>
    <li><a href="metal-waste-collection.html">Metal Waste Collection</a></li>
    <li><a href="paper-waste-collection.html">Paper Waste Collection</a></li>
    <li><a href="metal-recycling.html">Metal Recycling</a></li>
    <li><a href="paper-recycling.html">Paper Recycling</a></li>
    <li><a href="equipment.html">Recycling Equipment</a></li></ul></div>
  <div><h4>Company</h4><ul>
    <li><a href="about.html">About us</a></li>
    <li><a href="faq.html">FAQ</a></li>
    <li><a href="contact.html">Contact</a></li>
    <li><a href="{PORTAL}" target="_blank" rel="noopener">Client Login</a></li></ul></div>
  <div class="copy" style="grid-column:1/-1">&copy; {year} Marcells Paper and Metal Inc &middot; Chicago, IL 60624</div>
</div></footer>
</body>
</html>
"""

def prose(h1, blocks):
    """blocks: list of ('p'|'h2'|'h3'|'ul', text|items)"""
    out = [f"<h1>{h1}</h1>"] if h1 else []
    for kind, val in blocks:
        if kind == "p": out.append(f"<p>{val}</p>")
        elif kind in ("h2", "h3"): out.append(f"<{kind}>{val}</{kind}>")
        elif kind == "ul": out.append("<ul>" + "".join(f"<li>{x}</li>" for x in val) + "</ul>")
        elif kind == "raw": out.append(val)
    return '<section><div class="wrap"><div class="prose">' + "".join(out) + "</div></div></section>"

def build():
    os.makedirs(ROOT, exist_ok=True)
    for slug, spec in PAGES.items():
        body = spec["body"] if "body" in spec else prose(spec.get("h1"), spec["blocks"])
        with open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(page(f"{slug}.html", spec["title"], spec["desc"], body))
        print("wrote", slug)
    # Cloudflare Pages: clean URLs (/about -> about.html) are automatic; the
    # old GoDaddy addresses redirect so nothing bookmarked or indexed breaks.
    with open(os.path.join(ROOT, "_redirects"), "w") as f:
        f.write("/about-1 /about 301\n/about-1/ /about 301\n/index /  301\n")

if __name__ == "__main__":
    build()
