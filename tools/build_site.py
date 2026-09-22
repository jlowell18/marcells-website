#!/usr/bin/env python3
"""Builds marcellspaper.com (v2 redesign) as plain HTML. Run: python3 tools/build_site.py -> site/*.html"""
import os, html, datetime
from content import PAGES

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
PHONE = "(773) 265-1200"; PHONE_TEL = "+17732651200"; FAX = "(773) 265-1220"
EMAIL = "info@marcellspaper.com"; PORTAL = "https://portal.marcellspaper.com"
NAV = [("Programs", "programs.html"), ("Equipment", "equipment.html"), ("Portal", "portal.html"), ("Paper", "paper.html"),
       ("Metal", "metal.html"), ("Coverage", "coverage.html"), ("About", "about.html")]

def page(slug, title, desc, body):
    year = datetime.date.today().year
    nav = "".join(('<a href="%s"%s>%s</a>' % (h, ' class="active"' if h == slug else '', l)) for l, h in NAV)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="https://marcellspaper.com/assets/mpm2-hero.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.png">
<link rel="stylesheet" href="styles.css?v=2">
</head>
<body>
<div class="topbar"><div class="in"><span><b>Family-owned since 1979</b><span class="dot">·</span>Programs nationwide<span class="dot">·</span>Domestic &amp; export mills<span class="dot">·</span>Chicago, IL</span><span><b><a href="tel:{PHONE_TEL}">{PHONE}</a></b></span></div></div>
<header class="site-h"><div class="in">
  <a class="brand" href="index.html"><img src="assets/logo.webp" alt="Marcells Paper &amp; Metal"></a>
  <button class="menu-btn" aria-label="Menu" onclick="document.querySelector('nav.site-n').classList.toggle('open')">&#9776;</button>
  <nav class="site-n">{nav}<a class="login" href="{PORTAL}" target="_blank" rel="noopener">Client Login</a><a class="cta" href="contact.html">Talk to us</a></nav>
</div></header>
{body}
<footer class="site-f"><div class="wrap"><div class="cols">
  <div><h4>Marcells Paper &amp; Metal Inc</h4><div class="phone"><a href="tel:{PHONE_TEL}">{PHONE}</a></div><p style="font-size:14px">4221 W Ferdinand St, Chicago, IL 60624<br>Fax {FAX} · <a href="mailto:{EMAIL}" style="display:inline">{EMAIL}</a></p></div>
  <div><h4>Programs</h4><a href="programs.html">How a program works</a><a href="equipment.html">Equipment</a><a href="portal.html">Portal</a><a href="coverage.html">Coverage</a></div>
  <div><h4>Materials</h4><a href="paper.html">Paper</a><a href="metal.html">Metal</a><a href="secure-destruction.html">Secure destruction</a></div>
  <div><h4>Company</h4><a href="about.html">About</a><a href="faq.html">FAQ</a><a href="contact.html">Contact</a><a href="{PORTAL}" target="_blank" rel="noopener" style="color:#fff;font-weight:700">Client Login →</a></div>
</div><div class="copy"><span>&copy; {year} Marcells Paper and Metal Inc · Chicago, IL</span><span>Family-owned since 1979</span></div></div></footer>
</body>
</html>
"""

def build():
    os.makedirs(ROOT, exist_ok=True)
    for slug, spec in PAGES.items():
        with open(os.path.join(ROOT, f"{slug}.html"), "w", encoding="utf-8") as f:
            f.write(page(f"{slug}.html", spec["title"], spec["desc"], spec["body"]))
        print("wrote", slug)
    # Cloudflare Pages clean URLs are automatic; retired addresses 301 to their merged pages.
    with open(os.path.join(ROOT, "_redirects"), "w") as f:
        f.write("\n".join([
            "/about-1 /about 301", "/about-1/ /about 301", "/index / 301",
            "/services /programs 301", "/services.html /programs 301",
            "/metal-waste-collection /metal 301", "/metal-waste-collection.html /metal 301",
            "/metal-recycling /metal 301", "/metal-recycling.html /metal 301",
            "/paper-waste-collection /paper 301", "/paper-waste-collection.html /paper 301",
            "/paper-recycling /paper 301", "/paper-recycling.html /paper 301",
        ]) + "\n")

if __name__ == "__main__":
    build()
