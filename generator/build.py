"""Static site generator for Rapid Rescue & Recovery.
Usage: python3 build.py  -> writes ../site/
"""
import json, os, html, datetime
from icons import I
from content import BIZ, SERVICES, AREAS, HOME_FAQS, WA_DEFAULT
from urllib.parse import quote

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
DOMAIN = BIZ['domain']
TEL = 'tel:' + BIZ['phone_tel']
WA = 'https://wa.me/' + BIZ['wa'] + '?text=' + quote(WA_DEFAULT)
TODAY = datetime.date.today().isoformat()
V = '3'  # asset cache-buster
PAGES = []  # for sitemap

def esc(s): return html.escape(s, quote=True)
def strip_tags(s):
    import re
    return re.sub('<[^>]+>', '', s)

# ---------------------------------------------------------------------------
# Shared fragments
# ---------------------------------------------------------------------------
def head(path, title, desc, schema, og_type='website'):
    url = DOMAIN + path
    ld = ''.join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    return f'''<!doctype html>
<html lang="en-GB" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#F6F5F1" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0B0D11" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#0B0D11">
<meta name="format-detection" content="telephone=no">
<meta name="apple-mobile-web-app-title" content="Rapid Rescue">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(BIZ['name'])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/assets/img/icon-amber.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/inter-display-800.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/assets/fonts/inter-400.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="/assets/css/styles.css?v={V}">
<script>(function(){{try{{var m=localStorage.getItem("rrr-theme");if(m==="light"||m==="dark")document.documentElement.setAttribute("data-theme",m)}}catch(e){{}}}})();window.RRR={{wa:"{BIZ['wa']}"}};</script>
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

NAV = [('/services/', 'Services'), ('/areas/', 'Areas'), ('/trade-accounts/', 'Trade'), ('/broken-down/', 'Broken down?'), ('/contact/', 'Contact')]

def header(active):
    nav = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if active == h else ""}>{t}</a></li>' for h, t in NAV)
    svc_sub = ''.join(f'<li class="sub"><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    area_sub = ''.join(f'<li class="sub"><a href="/areas/{a["slug"]}/">{a["name"]}</a></li>' for a in AREAS)
    toggle = f'<button class="icon-btn theme-toggle" type="button" data-mode="auto" aria-label="Change theme">{I["sun"].replace("<svg", "<svg class=\"i-sun\"")}{I["moon"].replace("<svg", "<svg class=\"i-moon\"")}{I["auto"].replace("<svg", "<svg class=\"i-auto\"")}</button>'
    hours = '24/7 recovery' if BIZ['is_24_7'] else 'Vehicle recovery'
    return f'''<div class="topbar"><div class="container"><span><span class="live-dot" aria-hidden="true"></span>{hours} <span class="topbar-hide-sm">· Telford, Shropshire &amp; UK-wide</span></span><a href="{TEL}">{BIZ['phone_display']}</a></div></div>
<header class="header">
 <div class="container">
  <a class="brand" href="/" aria-label="{esc(BIZ['name'])} home">
   <img class="logo-light" src="/assets/img/logo-horizontal-light.svg" alt="{esc(BIZ['name'])}" width="331" height="64">
   <img class="logo-dark" src="/assets/img/logo-horizontal-dark.svg" alt="{esc(BIZ['name'])}" width="331" height="64">
  </a>
  <nav class="nav" aria-label="Main"><ul>{nav}</ul></nav>
  <div class="header-actions">
   {toggle}
   <a class="btn btn--primary header-call" href="{TEL}">{I['phone']}{BIZ['phone_display']}</a>
   <button class="icon-btn menu-btn" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobile-menu">{I['menu']}</button>
  </div>
 </div>
</header>
<div class="mobile-menu" id="mobile-menu" aria-hidden="true">
 <div class="mobile-menu-top">
  <a class="brand" href="/"><img class="logo-light" src="/assets/img/logo-horizontal-light.svg" alt="{esc(BIZ['name'])}" width="331" height="64" style="height:38px"><img class="logo-dark" src="/assets/img/logo-horizontal-dark.svg" alt="" width="331" height="64" style="height:38px"></a>
  <div style="display:flex;gap:8px">{toggle}<button class="icon-btn menu-close" type="button" aria-label="Close menu">{I['close']}</button></div>
 </div>
 <nav aria-label="Mobile"><ul>
  <li><a href="/">Home</a></li>
  <li><a href="/services/">Services</a></li>{svc_sub}
  <li><a href="/areas/">Areas we cover</a></li>{area_sub}
  <li><a href="/trade-accounts/">Trade accounts</a></li>
  <li><a href="/broken-down/">Broken down? Read this</a></li>
  <li><a href="/contact/">Contact &amp; quotes</a></li>
 </ul></nav>
 <div class="btn-row"><a class="btn btn--primary" href="{TEL}">{I['phone']}Call now</a><a class="btn btn--wa" href="{WA}">{I['wa']}WhatsApp</a></div>
</div>
'''

def footer():
    svc = ''.join(f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    areas = ''.join(f'<li><a href="/areas/{a["slug"]}/">{"Recovery " + a["name"] if a["local"] else "Nationwide"}</a></li>' for a in AREAS)
    socials = ''.join(f'<a href="{u}" aria-label="{k.title()}" rel="noopener" target="_blank">{I[k]}</a>' for k, u in BIZ['socials'].items() if u)
    socials = f'<div class="socials">{socials}</div>' if socials else ''
    return f'''<footer class="footer">
 <div class="container">
  <div class="footer-grid">
   <div>
    <a class="brand" href="/"><img src="/assets/img/logo-horizontal-dark.svg" alt="{esc(BIZ['name'])}" width="331" height="64" loading="lazy"></a>
    <a class="big-num" href="{TEL}">{BIZ['phone_display']}</a>
    <p style="margin:0 0 6px"><a href="mailto:{BIZ['email']}">{BIZ['email']}</a></p>
    <p style="margin:0">{BIZ['hours_text'] if BIZ['is_24_7'] else ''}<br>Based in Telford, Shropshire · Covering the UK</p>
    {socials}
   </div>
   <div><h4>Services</h4><ul>{svc}</ul></div>
   <div><h4>Areas</h4><ul>{areas}</ul></div>
   <div><h4>Help</h4><ul>
    <li><a href="/broken-down/">What to do if you break down</a></li>
    <li><a href="/contact/">Get a quote</a></li>
    <li><a href="/trade-accounts/">Trade accounts</a></li>
    <li><a href="{WA}">WhatsApp us</a></li>
    <li><a href="/privacy/">Privacy policy</a></li>
   </ul></div>
  </div>
  <div class="footer-bottom">
   <span>© <span data-year>{datetime.date.today().year}</span> {esc(BIZ['name'])}. All rights reserved.</span>
   <span>In danger or in a live lane? Call <a href="tel:999">999</a>.</span>
  </div>
 </div>
</footer>
<nav class="action-bar" aria-label="Quick contact">
 <a class="ab-call" href="{TEL}">{I['phone']}Call now</a>
 <a class="ab-wa" href="{WA}">{I['wa']}WhatsApp</a>
 <button class="ab-loc" type="button" data-share-location>{I['nav']}Send location</button>
</nav>
<a class="fab-wa" href="{WA}" aria-label="Message us on WhatsApp">{I['wa']}</a>
<script src="/assets/js/main.js?v={V}" defer></script>
</body>
</html>
'''

def org_schema():
    s = {
        '@context': 'https://schema.org', '@type': 'TowingService', '@id': DOMAIN + '/#business',
        'name': BIZ['name'], 'url': DOMAIN + '/', 'telephone': BIZ['phone_tel'], 'email': BIZ['email'],
        'logo': DOMAIN + '/assets/img/logo-512.png', 'image': DOMAIN + '/assets/img/og-image.png',
        'description': 'Pay-as-you-go breakdown recovery, accident recovery, jump starts and vehicle transport in Telford, Shropshire and across the UK.',
        'priceRange': '££', 'paymentAccepted': BIZ['payment'],
        'address': {'@type': 'PostalAddress', 'addressLocality': 'Telford', 'addressRegion': 'Shropshire', 'addressCountry': 'GB'},
        'areaServed': [{'@type': 'City', 'name': a['name']} for a in AREAS if a['local']] + [{'@type': 'Country', 'name': 'United Kingdom'}],
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Recovery services', 'itemListElement': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['name'], 'url': f"{DOMAIN}/services/{s['slug']}/"}} for s in SERVICES]},
    }
    if BIZ['is_24_7']:
        s['openingHoursSpecification'] = [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], 'opens': '00:00', 'closes': '23:59'}]
    same = [u for u in BIZ['socials'].values() if u]
    if same: s['sameAs'] = same
    return s

def faq_schema(faqs):
    return {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [
        {'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': strip_tags(a)}} for q, a in faqs]}

def crumbs_schema(items):
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [
        {'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': DOMAIN + p} for i, (p, n) in enumerate(items)]}

def crumbs_html(items):
    lis = ''.join(f'<li><a href="{p}">{esc(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{esc(n)}</li>' for i, (p, n) in enumerate(items))
    return f'<nav aria-label="Breadcrumb"><ol class="crumbs">{lis}</ol></nav>'

def faq_html(faqs):
    return '<div class="faq">' + ''.join(f'<details><summary>{esc(q)}</summary><div><p>{a}</p></div></details>' for q, a in faqs) + '</div>'

def cta_band(title='Need a recovery truck now?', text=None):
    text = text or (f"Call, WhatsApp or send your location. You'll get a fixed price before we set off." )
    return f'''<section class="section"><div class="container"><div class="cta reveal">
 <div><h2>{title}</h2><p>{text}</p></div>
 <div class="btn-row"><a class="btn btn--dark btn--lg" href="{TEL}">{I['phone']}{BIZ['phone_display']}</a><a class="btn btn--ghost btn--lg" href="{WA}">{I['wa']}WhatsApp us</a></div>
</div></div></section>'''

def page_hero(crumbs, h1, lead, extra=''):
    return f'''<section class="page-hero"><div class="container">
 {crumbs_html(crumbs)}
 <h1>{h1}</h1>
 <p class="lead">{lead}</p>
 <div class="btn-row"><a class="btn btn--primary btn--lg" href="{TEL}">{I['phone']}Call {BIZ['phone_display']}</a><a class="btn btn--wa btn--lg" href="{WA}">{I['wa']}WhatsApp</a><button class="btn btn--ghost btn--lg" type="button" data-share-location>{I['nav']}Send my location</button></div>
 {extra}
</div></section>'''

def aside():
    svc = ''.join(f'<li><a href="/services/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    return f'''<aside>
 <div class="aside-card">
  <h3>Need help now?</h3>
  <p>{"Answering 24/7. " if BIZ['is_24_7'] else ""}Fixed price before we set off.</p>
  <a class="num" href="{TEL}">{BIZ['phone_display']}</a>
  <a class="btn btn--primary" href="{TEL}">{I['phone']}Call now</a>
  <a class="btn btn--wa" href="{WA}">{I['wa']}WhatsApp</a>
  <button class="btn btn--ghost" style="color:#fff" type="button" data-share-location>{I['nav']}Send my location</button>
 </div>
 <div class="aside-links"><h3>Our services</h3><ul>{svc}</ul></div>
</aside>'''

def render_blocks(blocks):
    out = []
    for kind, val in blocks:
        if kind == 'h2': out.append(f'<h2>{val}</h2>')
        elif kind == 'p': out.append(f'<p>{val}</p>')
        elif kind == 'ul': out.append('<ul>' + ''.join(f'<li>{x}</li>' for x in val) + '</ul>')
        elif kind == 'callout': out.append(f'<div class="callout" role="note">{I["alert"]}<p>{val}</p></div>')
        elif kind == 'chips': out.append('<ul class="areas">' + ''.join(f'<li><span>{I["pin"]}{esc(x)}</span></li>' for x in val) + '</ul>')
    return '\n'.join(out)

def write(path, content, priority='0.7'):
    out = os.path.join(ROOT, path.strip('/'), 'index.html') if path.endswith('/') else os.path.join(ROOT, path.strip('/'))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, 'w', encoding='utf-8').write(content)
    if path.endswith('/') and path not in ('/thank-you/',):
        PAGES.append((path, priority))

def build_page(path, title, desc, main, active=None, schema=None, priority='0.7'):
    schema = [org_schema()] + (schema or [])
    write(path, head(path, title, desc, schema) + header(active) + f'<main id="main">{main}</main>' + footer(), priority)

# ---------------------------------------------------------------------------
# Visual fragments
# ---------------------------------------------------------------------------
TRUCK = open(os.path.join(ROOT, 'assets/img/truck.svg')).read()

def coverage_svg():
    towns = [('Telford', 200, 200, True, 0, 0, 'middle'), ('Shrewsbury', 86, 208, False, 0, 20, 'middle'), ('Wolverhampton', 334, 258, False, 0, 20, 'middle'),
             ('Newport', 226, 132, False, 10, 4, 'start'), ('Bridgnorth', 214, 306, False, 10, 4, 'start'), ('Shifnal', 258, 214, False, 10, 4, 'start'), ('Wellington', 166, 186, False, -10, -2, 'end')]
    dots = ''
    for n, x, y, hub, dx, dy, anchor in towns:
        if hub:
            dots += f'<circle class="hub" cx="{x}" cy="{y}" r="9"/><circle cx="{x}" cy="{y}" r="4" fill="#0E1116"/>'
            dots += f'<text x="{x}" y="{y+26}" text-anchor="middle" style="font-weight:800;font-size:13px">{n}</text>'
        else:
            dots += f'<circle class="town" cx="{x}" cy="{y}" r="4.5"/><text x="{x+dx}" y="{y+dy}" text-anchor="{anchor}">{n}</text>'
    roads = ('<path class="road-line" d="M60 212 Q120 205 166 186 L200 200 Q240 210 258 214 Q300 236 334 258"/>'
             '<path class="road-line" d="M200 200 L226 132 L232 40"/><path class="road-line" d="M200 200 L214 306 L220 380"/>')
    labels = '<text x="300" y="232" style="font-size:10px;opacity:.7">M54</text><text x="112" y="218" style="font-size:10px;opacity:.7">A5</text><text x="232" y="96" style="font-size:10px;opacity:.7">A41</text><text x="220" y="350" style="font-size:10px;opacity:.7">A442</text>'
    return f'''<div class="coverage-visual" role="img" aria-label="Map showing Telford at the centre with Shrewsbury, Wolverhampton, Newport, Bridgnorth, Shifnal and Wellington around it">
<svg viewBox="0 0 400 400"><circle class="ring" cx="200" cy="200" r="80"/><circle class="ring" cx="200" cy="200" r="160" stroke-dasharray="3 6"/>
<circle class="ring pulse" cx="200" cy="200" r="80"/>{roads}{labels}{dots}
<text x="200" y="372" text-anchor="middle" style="font-size:10px;opacity:.7">Local area · UK-wide via partner network</text></svg></div>'''

def wa_mock():
    return f'''<div class="panel reveal" style="max-width:420px;margin:0 auto;padding:0;overflow:hidden">
 <div style="background:#075E54;color:#fff;padding:14px 18px;display:flex;align-items:center;gap:12px">
  <img src="/assets/img/icon-amber.svg" width="38" height="38" alt="" style="border-radius:10px">
  <div><b style="display:block;line-height:1.2">Rapid Rescue &amp; Recovery</b><small style="opacity:.8">typically replies in minutes</small></div>
 </div>
 <div style="padding:18px;display:grid;gap:10px;background:var(--surface-2);font-size:.92rem" aria-label="Example WhatsApp conversation">
  <div class="bub me">Hi, I've broken down. Here's my location 📍<br><span class="mapchip">{I['pin']} Maps pin · ±8m</span></div>
  <div class="bub them">No problem. What's the vehicle and where would you like it taken?</div>
  <div class="bub me">Ford Focus, automatic. To my garage in Wellington please</div>
  <div class="bub them">Price agreed ✅ Driver&rsquo;s on the way. We&rsquo;ll message you when we&rsquo;re close 👍</div>
  <div class="bub them">📸 Photos of your car loaded and secured. On our way to the garage now.</div>
 </div>
 <p class="form-note" style="padding:10px 18px 14px">Example of how a job runs on WhatsApp.</p>
</div>
<style>.bub{{max-width:85%;padding:9px 12px;border-radius:12px;line-height:1.4;box-shadow:0 1px 1px rgba(0,0,0,.08)}}.bub.me{{justify-self:end;background:#D9FDD3;color:#0E1116;border-top-right-radius:4px}}.bub.them{{justify-self:start;background:var(--surface);border-top-left-radius:4px}}:root[data-theme="dark"] .bub.me{{background:#005C4B;color:#E9EDEF}}@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]) .bub.me{{background:#005C4B;color:#E9EDEF}}}}.mapchip{{display:inline-flex;align-items:center;gap:6px;margin-top:6px;padding:6px 10px;border-radius:8px;background:rgba(0,0,0,.08);font-weight:600;font-size:.82rem}}.mapchip svg{{width:14px;height:14px}}</style>'''

def service_cards(exclude=None):
    return '<div class="grid grid-3">' + ''.join(
        f'''<a class="card reveal" href="/services/{s['slug']}/"><div class="ic">{I[s['icon']]}</div><h3>{s['name']}</h3><p>{s['card']}</p><span class="more">Find out more {I['arrow']}</span></a>'''
        for s in SERVICES if s['slug'] != exclude) + '</div>'

def area_chips():
    return '<ul class="areas">' + ''.join(f'<li><a href="/areas/{a["slug"]}/">{I["pin"] if a["local"] else I["globe"]}{a["name"]}</a></li>' for a in AREAS) + '</ul>'

# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------
def build_home():
    h247 = BIZ['is_24_7']
    main = f'''
<section class="hero">
 <div class="container">
  <div>
   <span class="status-pill"><span class="live-dot" aria-hidden="true"></span>{"Answering now · 24 hours a day, 7 days a week" if h247 else "Answering now"}</span>
   <h1>{"24/7 " if h247 else ""}Car Recovery in Telford <span class="em">&amp; Across the&nbsp;UK</span></h1>
   <p class="lead">Broken down, crashed or just need a vehicle moved? Call or WhatsApp, send your location and get a <strong style="color:#fff">fixed price before we set off</strong>. No membership needed.</p>
   <div class="btn-row">
    <a class="btn btn--primary btn--lg" href="{TEL}">{I['phone']}Call now</a>
    <a class="btn btn--wa btn--lg" href="{WA}">{I['wa']}WhatsApp</a>
    <button class="btn btn--ghost btn--lg" type="button" data-share-location>{I['nav']}Send my location</button>
   </div>
   <a class="hero-phone" href="{TEL}"><span class="ring">{I['phone']}</span><span><small>Tap to call</small><strong>{BIZ['phone_display']}</strong></span></a>
   <ul class="chips">
    <li>{I['pound']}Fixed price upfront</li>
    <li>{I['msg']}Live WhatsApp updates</li>
    <li>{I['camera']}Photos of your vehicle</li>
    <li>{I['globe']}UK-wide coverage</li>
   </ul>
  </div>
  <div class="hero-art">
   <div class="hero-card">{'<span class="ic">'+I['nav']+'</span>'}<span><b>One tap location sharing</b><span>Your exact pin, straight to our WhatsApp</span></span></div>
   {TRUCK}
   <div class="road" aria-hidden="true"></div>
  </div>
 </div>
</section>

<div class="emergency"><div class="container">
 <p>{I['alert'].replace('<svg', '<svg style="width:20px;height:20px;display:inline-block;vertical-align:-4px;margin-right:6px"')} Stuck in a live lane or feel unsafe? Stay belted in, hazards on, and <a href="tel:999">call 999</a> first.</p>
 <a href="/broken-down/">What to do if you break down →</a>
</div></div>

<section class="section" id="how">
 <div class="container">
  <div class="section-head"><span class="eyebrow">How it works</span><h2>Help in three simple steps</h2><p class="lead">No call centres, no app to download and no membership. You speak to the people coming to get you.</p></div>
  <div class="steps">
   <div class="step reveal"><h3>Call, WhatsApp or send your pin</h3><p>Tap <strong>Send my location</strong> and your exact GPS pin lands in our WhatsApp. Tell us the vehicle and where it needs to go.</p></div>
   <div class="step reveal"><h3>Get a fixed price</h3><p>We give you a clear price and an honest arrival time before anyone sets off. No hidden extras.</p></div>
   <div class="step reveal"><h3>We load, carry &amp; deliver</h3><p>Your vehicle is photographed, secured on our bed and delivered home, to a garage or anywhere in the UK, with updates along the way.</p></div>
  </div>
 </div>
</section>

<section class="section section--alt" id="services">
 <div class="container">
  <div class="section-head"><span class="eyebrow">Services</span><h2>Recovery for whatever&rsquo;s gone wrong</h2><p class="lead">{BIZ['vehicles']}, all carried fully on the bed of our truck.</p></div>
  {service_cards()}
 </div>
</section>

<section class="section">
 <div class="container split">
  <div class="reveal">
   <span class="eyebrow">Why Rapid Rescue</span>
   <h2>Recovery the way it should feel: fast, clear and in your hands</h2>
   <p class="lead">Most recovery firms still make you read out a postcode at the roadside and wait for a call back. We do it differently.</p>
   <ul class="ticks">
    <li>{I['check']}<div><b>Send your exact location in one tap</b><span>GPS pin straight to WhatsApp. No guessing which lay-by you&rsquo;re in.</span></div></li>
    <li>{I['check']}<div><b>A fixed price before we set off</b><span>You agree the price upfront. No meter running, no surprise add-ons.</span></div></li>
    <li>{I['check']}<div><b>Photos at pickup and drop-off</b><span>We photograph your vehicle before and after loading and send the photos to you. Useful for insurers, and reassuring for you.</span></div></li>
    <li>{I['check']}<div><b>Live updates on WhatsApp</b><span>Know who&rsquo;s coming, when they&rsquo;re close and when your vehicle&rsquo;s been dropped off.</span></div></li>
    <li>{I['check']}<div><b>Local, with UK-wide reach</b><span>Our own truck around Telford and Shropshire, and trusted partners nationwide. One number for all of it.</span></div></li>
   </ul>
  </div>
  {wa_mock()}
 </div>
</section>

<section class="section section--alt" id="areas">
 <div class="container split">
  {coverage_svg()}
  <div class="reveal">
   <span class="eyebrow">Areas we cover</span>
   <h2>Telford-based. Covering Shropshire, the West Midlands and the UK.</h2>
   <p class="lead">We&rsquo;re next to the M54, so we can reach Shrewsbury, Wolverhampton, Newport, Bridgnorth and Shifnal quickly. Further afield, we arrange recovery through trusted partner operators, and you keep one point of contact the whole way.</p>
   {area_chips()}
  </div>
 </div>
</section>

<section class="section">
 <div class="container split">
  <div class="reveal">
   <span class="eyebrow">Pricing</span>
   <h2>Fair, fixed prices. Agreed before we move.</h2>
   <p class="lead">No two recoveries are the same, so we don&rsquo;t hide behind a one-size price list. Tell us the job and we&rsquo;ll give you one clear price, and that&rsquo;s what you pay.</p>
   <div class="btn-row" style="margin-top:24px"><a class="btn btn--primary" href="/contact/">{I['pound']}Get a quote</a><a class="btn btn--wa" href="{WA}">{I['wa']}Quote on WhatsApp</a></div>
  </div>
  <div class="factors">
   <div class="factor reveal">{I['route']}<div><b>Distance</b><span>From where you are to where it&rsquo;s going.</span></div></div>
   <div class="factor reveal">{I['clock']}<div><b>Time of day</b><span>Daytime, evening, overnight or bank holiday.</span></div></div>
   <div class="factor reveal">{I['car']}<div><b>The vehicle</b><span>Size, weight and whether it rolls, steers and brakes.</span></div></div>
   <div class="factor reveal">{I['pin']}<div><b>Where it&rsquo;s stuck</b><span>Driveway, car park, verge, ditch or motorway.</span></div></div>
  </div>
 </div>
</section>

<section class="section band" id="trade">
 <div class="container">
  <div class="section-head"><span class="eyebrow">For the trade</span><h2 style="color:#fff">Garages, dealers &amp; bodyshops: let us do the moving</h2><p class="lead">Reliable collections and deliveries, with photo condition records on every job.</p></div>
  <div class="grid grid-4">
   <div class="card reveal"><div class="ic">{I['wrench']}</div><h3 style="color:#fff">Garages &amp; MOT centres</h3><p>Customer collections, non-runners in and repaired cars back out.</p></div>
   <div class="card reveal"><div class="ic">{I['car']}</div><h3 style="color:#fff">Car dealers</h3><p>Stock moves, auction collections and customer deliveries anywhere in the UK.</p></div>
   <div class="card reveal"><div class="ic">{I['crash']}</div><h3 style="color:#fff">Bodyshops</h3><p>Accident-damaged vehicles collected and returned, with photos at every step.</p></div>
   <div class="card reveal"><div class="ic">{I['building']}</div><h3 style="color:#fff">Fleets &amp; businesses</h3><p>One number for your vans and company cars, with clear invoices for every job.</p></div>
  </div>
  <div class="btn-row" style="margin-top:28px"><a class="btn btn--primary" href="/trade-accounts/">Open a trade account {I['arrow']}</a></div>
 </div>
</section>

<section class="section" id="faq">
 <div class="container">
  <div class="section-head"><span class="eyebrow">FAQs</span><h2>Questions people ask us</h2></div>
  {faq_html(HOME_FAQS)}
 </div>
</section>
{cta_band()}
'''
    build_page('/', f"{'24/7 ' if h247 else ''}Car Recovery Telford & UK-wide | Breakdown Recovery | Rapid Rescue & Recovery",
               f"{'24/7 ' if h247 else ''}car and van recovery in Telford, Shropshire and across the UK. Breakdown, accident and motorway recovery, jump starts and vehicle transport. Fixed price before we move. Call 07376 322865.",
               main, active='/', schema=[faq_schema(HOME_FAQS), {'@context': 'https://schema.org', '@type': 'WebSite', 'name': BIZ['name'], 'url': DOMAIN + '/'}], priority='1.0')

# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------
def build_services():
    crumbs = [('/', 'Home'), ('/services/', 'Services')]
    main = page_hero(crumbs, 'Vehicle recovery services', "From roadside breakdowns to UK-wide vehicle transport, here's everything we do.") + f'''
<section class="section"><div class="container">{service_cards()}</div></section>
<section class="section section--alt"><div class="container"><div class="section-head"><span class="eyebrow">Coverage</span><h2>Where we work</h2></div>{area_chips()}</div></section>
{cta_band()}'''
    build_page('/services/', 'Recovery Services | Breakdown, Accident, Transport | Rapid Rescue & Recovery',
               'Breakdown recovery, accident recovery, motorway recovery, jump starts, vehicle transport and non-runner collection in Telford, Shropshire and UK-wide.',
               main, active='/services/', schema=[crumbs_schema(crumbs)], priority='0.9')

    for s in SERVICES:
        path = f"/services/{s['slug']}/"
        crumbs = [('/', 'Home'), ('/services/', 'Services'), (path, s['name'])]
        main = page_hero(crumbs, s['h1'], s['lead']) + f'''
<section class="section"><div class="container layout-aside">
 <div class="prose">{render_blocks(s['body'])}
  <h2>How it works</h2>
  <ol class="safety-steps ol-reset">
   <li><div><b>Get in touch</b><span>Call {BIZ['phone_display']}, WhatsApp us or tap Send my location.</span></div></li>
   <li><div><b>Agree a fixed price</b><span>We give you a clear price and an honest arrival time.</span></div></li>
   <li><div><b>We collect &amp; deliver</b><span>Photos at pickup and drop-off, and updates on WhatsApp along the way.</span></div></li>
  </ol>
  <h2>FAQs</h2>
  {faq_html(s['faqs'])}
 </div>
 {aside()}
</div></section>
<section class="section section--alt"><div class="container"><div class="section-head"><span class="eyebrow">More services</span><h2>Other ways we can help</h2></div>{service_cards(exclude=s['slug'])}</div></section>
{cta_band()}'''
        svc_schema = {'@context': 'https://schema.org', '@type': 'Service', 'name': s['name'], 'serviceType': s['name'],
                      'provider': {'@id': DOMAIN + '/#business'}, 'url': DOMAIN + path, 'description': s['desc'],
                      'areaServed': [{'@type': 'City', 'name': a['name']} for a in AREAS if a['local']] + [{'@type': 'Country', 'name': 'United Kingdom'}]}
        build_page(path, s['title'], s['desc'], main, active='/services/', schema=[crumbs_schema(crumbs), svc_schema, faq_schema(s['faqs'])], priority='0.8')

# ---------------------------------------------------------------------------
# AREAS
# ---------------------------------------------------------------------------
def build_areas():
    crumbs = [('/', 'Home'), ('/areas/', 'Areas')]
    cards = '<div class="grid grid-3">' + ''.join(
        f'''<a class="card reveal" href="/areas/{a['slug']}/"><div class="ic">{I['pin'] if a['local'] else I['globe']}</div><h3>{"Recovery in " + a['name'] if a['local'] else "Nationwide recovery"}</h3><p>{a['lead']}</p><span class="more">View area {I['arrow']}</span></a>'''
        for a in AREAS) + '</div>'
    main = page_hero(crumbs, 'Areas we cover', "Based in Telford, covering Shropshire and the West Midlands with our own truck, and the rest of the UK through trusted partners.") + f'''
<section class="section"><div class="container split">{coverage_svg()}<div><h2>Local first, nationwide when you need it</h2><p class="lead">Our base is next to the M54, so the main towns around Telford are a short drive away. Outside our patch, we arrange recovery through partner operators, and you still deal with us.</p>{area_chips()}</div></div></section>
<section class="section section--alt"><div class="container">{cards}</div></section>
{cta_band()}'''
    build_page('/areas/', 'Areas We Cover | Telford, Shropshire, West Midlands & UK | Rapid Rescue',
               'Vehicle recovery across Telford, Shrewsbury, Wolverhampton, Newport, Bridgnorth, Shifnal and UK-wide. Call 07376 322865.',
               main, active='/areas/', schema=[crumbs_schema(crumbs)], priority='0.9')

    for a in AREAS:
        path = f"/areas/{a['slug']}/"
        crumbs = [('/', 'Home'), ('/areas/', 'Areas'), (path, a['name'])]
        nm = a['name']
        svc_links = '<div class="grid grid-2">' + ''.join(
            f'<a class="card" href="/services/{s["slug"]}/" style="padding:20px"><h3 style="font-size:1.05rem;margin:0;display:flex;align-items:center;gap:10px"><span class="ic" style="width:40px;height:40px;margin:0;border-radius:10px">{I[s["icon"]]}</span>{s["name"]}{" in " + nm if a["local"] else ""}</h3></a>'
            for s in SERVICES) + '</div>'
        faqs = [
            (f"How fast can you get to me in {nm}?" if a['local'] else "How fast can help reach me?", "We'll give you an honest arrival time when you call, based on where you are and the traffic, and keep you updated on WhatsApp."),
            ("How much will it cost?", "You'll get a fixed price before we set off. The price depends on distance, time of day and the vehicle."),
            ("Can you take my car outside the area?", "Yes. We can deliver your vehicle anywhere in the UK."),
        ]
        main = page_hero(crumbs, a['h1'], a['lead']) + f'''
<section class="section"><div class="container layout-aside">
 <div class="prose">{render_blocks(a['body'])}
  <h2>Services{" in " + nm if a['local'] else ""}</h2>
  {svc_links}
  <h2>FAQs</h2>
  {faq_html(faqs)}
 </div>
 {aside()}
</div></section>
<section class="section section--alt"><div class="container"><div class="section-head"><span class="eyebrow">Nearby</span><h2>Other areas we cover</h2></div>{area_chips()}</div></section>
{cta_band(f"Broken down in {nm}?" if a['local'] else "Broken down anywhere in the UK?")}'''
        build_page(path, a['title'], a['desc'], main, active='/areas/', schema=[crumbs_schema(crumbs), faq_schema(faqs)], priority='0.8')

# ---------------------------------------------------------------------------
# BROKEN DOWN GUIDE
# ---------------------------------------------------------------------------
def build_guide():
    crumbs = [('/', 'Home'), ('/broken-down/', 'Broken down?')]
    faqs = [
        ("What should I do first if I break down on a motorway?", "Move into the left lane and onto the hard shoulder, an emergency area or a slip road if you can. Put your hazard lights on, get out on the left-hand side if it's safe, and wait behind the barrier. If you can't get out safely, stay in your vehicle with your seatbelt on and call 999."),
        ("Should I stay in my car?", "Only if it's not safe to get out, for example if you're stopped in a live lane. Otherwise, get out on the side away from the traffic and wait somewhere safe, behind a barrier if there is one."),
        ("Should I use a warning triangle on the motorway?", "No. Don't put a warning triangle out on a motorway, because it's not safe to walk along the carriageway. On other roads, use one only if it's safe to do so."),
    ]
    main = page_hero(crumbs, 'Broken down? Here&rsquo;s what to do', "Stay calm and get safe first. Then send us your location and we'll take it from there.") + f'''
<section class="section"><div class="container layout-aside">
 <div class="prose">
  <div class="callout" role="note">{I['alert']}<p><strong>If you're stopped in a live lane, or anyone is hurt or in danger, call <a href="tel:999">999</a> immediately.</strong> On a motorway, you can also call National Highways on <a href="tel:03001235000">0300 123 5000</a>.</p></div>
  <h2>On a motorway or fast A-road</h2>
  <ol class="safety-steps ol-reset">
   <li><div><b>Go left</b><span>Signal left, move into the left lane and pull onto the hard shoulder, into an emergency area or onto a slip road if you can. Put your hazard lights on.</span></div></li>
   <li><div><b>Get safe</b><span>If it's safe, get out on the left-hand side (away from traffic) with all passengers. Wait behind the safety barrier and well up the bank. Wear high-vis if you have it. Don't go back to the vehicle.</span></div></li>
   <li><div><b>Stuck in a live lane?</b><span>Stay in the vehicle with seatbelts on and hazard lights on, and call 999 straight away.</span></div></li>
   <li><div><b>Get help</b><span>Once you're safe, call us on <a href="{TEL}">{BIZ['phone_display']}</a> or tap <strong>Send my location</strong>. Tell us the road, direction, nearest junctions and the marker post number.</span></div></li>
  </ol>
  <h2>On a normal road, car park or at home</h2>
  <ol class="safety-steps ol-reset">
   <li><div><b>Get off the road if you can</b><span>Pull over somewhere safe and visible, away from bends and brows of hills. Hazard lights on.</span></div></li>
   <li><div><b>Warn other drivers</b><span>On ordinary roads, put a warning triangle about 45 metres behind your vehicle, but only if it's safe. Never use one on a motorway.</span></div></li>
   <li><div><b>Stay visible and warm</b><span>At night or in bad weather, wear something bright and stay well away from the traffic.</span></div></li>
   <li><div><b>Send us your details</b><span>Your location, the vehicle, what happened and where you want it taken. A photo on WhatsApp helps us bring the right kit.</span></div></li>
  </ol>
  <h2>What to tell us</h2>
  <ul>
   <li>Your exact location (the <strong>Send my location</strong> button does this for you)</li>
   <li>Make, model and whether it's automatic, electric or hybrid</li>
   <li>What happened, and whether it rolls, steers and brakes</li>
   <li>Where you'd like the vehicle taken</li>
   <li>How many passengers need a lift</li>
  </ul>
  <h2>Wrong fuel?</h2>
  <p><strong>Don't start the engine</strong> or turn the ignition on. Put the car in neutral, push it somewhere safe if you can do so safely, and call us. We can take it to a garage that can drain the fuel.</p>
  <h2>FAQs</h2>
  {faq_html(faqs)}
  <p class="form-note" style="margin-top:20px">This guide is based on National Highways advice. Always follow instructions from the police, traffic officers and the emergency services.</p>
 </div>
 {aside()}
</div></section>
{cta_band()}'''
    build_page('/broken-down/', 'What To Do If You Break Down | Motorway & Roadside Safety | Rapid Rescue',
               'Broken down? Step-by-step safety advice for motorways and ordinary roads, what to tell your recovery company, and how to send your exact location. Telford & UK-wide.',
               main, active='/broken-down/', schema=[crumbs_schema(crumbs), faq_schema(faqs)], priority='0.8')

# ---------------------------------------------------------------------------
# TRADE
# ---------------------------------------------------------------------------
def build_trade():
    crumbs = [('/', 'Home'), ('/trade-accounts/', 'Trade accounts')]
    main = page_hero(crumbs, 'Trade accounts for garages, dealers &amp; bodyshops', "One reliable recovery partner for collections, deliveries, auction runs and non-runners, with photo records on every job.") + f'''
<section class="section"><div class="container split">
 <div>
  <span class="eyebrow">Why trade customers use us</span>
  <h2>Moving vehicles is our job, so you can get on with yours</h2>
  <ul class="ticks">
   <li>{I['check']}<div><b>Photo condition records</b><span>Photos at collection and delivery on every job, sent straight to you.</span></div></li>
   <li>{I['check']}<div><b>WhatsApp booking</b><span>Send the reg, the addresses and the time. That's it.</span></div></li>
   <li>{I['check']}<div><b>Local and UK-wide</b><span>Shropshire and West Midlands moves with our own truck, and longer distances arranged for you.</span></div></li>
   <li>{I['check']}<div><b>Clear invoicing</b><span>Itemised invoices with the reg, route and date for every move.</span></div></li>
   <li>{I['check']}<div><b>Agreed trade rates</b><span>Regular work gets agreed pricing. Ask us for a rate card.</span></div></li>
  </ul>
 </div>
 <div class="panel">
  <h3>Who we work with</h3>
  <ul class="areas" style="margin-top:12px">
   <li><span>{I['car']}Independent car dealers</span></li><li><span>{I['wrench']}Garages &amp; MOT centres</span></li><li><span>{I['crash']}Bodyshops &amp; accident repair</span></li>
   <li><span>{I['route']}Auction buyers</span></li><li><span>{I['building']}Fleets &amp; leasing</span></li><li><span>{I['key']}Specialists &amp; tuners</span></li>
  </ul>
  <div class="btn-row" style="margin-top:22px"><a class="btn btn--primary" href="/contact/#quote">Request a trade rate card</a><a class="btn btn--wa" href="https://wa.me/{BIZ['wa']}?text={quote('Hi Rapid Rescue, I would like to set up a trade account.\n\nBusiness name: \nType of business: \nRoughly how many moves per month: ')}">{I['wa']}WhatsApp us</a></div>
 </div>
</div></section>
{cta_band('Ready to book your first move?', 'Send us the reg, pickup and drop-off, and we&rsquo;ll come back with a price.')}'''
    build_page('/trade-accounts/', 'Trade Accounts | Vehicle Collection for Dealers, Garages & Bodyshops | Rapid Rescue',
               'Trade vehicle collection and delivery for car dealers, garages, MOT centres and bodyshops in Telford, Shropshire and UK-wide. Photo records on every job. 07376 322865.',
               main, active='/trade-accounts/', schema=[crumbs_schema(crumbs)], priority='0.8')

# ---------------------------------------------------------------------------
# CONTACT (Netlify form + WhatsApp)
# ---------------------------------------------------------------------------
def build_contact():
    crumbs = [('/', 'Home'), ('/contact/', 'Contact')]
    opts = ''.join(f'<option>{s["name"]}</option>' for s in SERVICES) + '<option>Something else</option>'
    main = page_hero(crumbs, 'Get help or a quote', "For anything urgent, call or WhatsApp. For bookings and quotes, use the form. It goes straight to us.") + f'''
<section class="section" id="quote"><div class="container layout-aside">
 <div>
  <div class="panel">
   <h2 style="font-size:1.6rem">Request a recovery or quote</h2>
   <p class="muted">Fill in what you can. Send it on WhatsApp for the fastest reply, or submit it and we&rsquo;ll call you back.</p>
   <form class="form" name="recovery-request" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="bot-field" data-recovery-form>
    <input type="hidden" name="form-name" value="recovery-request">
    <p class="hidden"><label>Don&rsquo;t fill this in: <input name="bot-field"></label></p>
    <div class="row">
     <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" autocomplete="name" required></div>
     <div class="field"><label for="f-phone">Mobile number</label><input id="f-phone" name="phone" type="tel" inputmode="tel" autocomplete="tel" required></div>
    </div>
    <div class="row">
     <div class="field"><label for="f-service">What do you need?</label><select id="f-service" name="service">{opts}</select></div>
     <div class="field"><label for="f-when">When?</label><select id="f-when" name="when"><option>Right now: it&rsquo;s urgent</option><option>Later today</option><option>Book for another day</option><option>Just a price for now</option></select></div>
    </div>
    <div class="field"><label for="f-pickup">Pickup location</label>
     <div class="loc-row"><input id="f-pickup" name="pickup" placeholder="Road, town or postcode" required><button class="btn btn--dark" type="button" data-fill-location="f-pickup" aria-label="Use my current location">{I['nav']}<span class="topbar-hide-sm">Use GPS</span></button></div></div>
    <div class="field"><label for="f-dropoff">Drop-off location <span class="opt">(if known)</span></label><input id="f-dropoff" name="dropoff" placeholder="Home, garage, postcode…"></div>
    <div class="row">
     <div class="field"><label for="f-vehicle">Vehicle <span class="opt">(make, model or reg)</span></label><input id="f-vehicle" name="vehicle" placeholder="e.g. Ford Focus, automatic"></div>
     <div class="field"><label for="f-rolls">Does it roll, steer &amp; brake?</label><select id="f-rolls" name="rolls"><option>Yes</option><option>No</option><option>Not sure</option></select></div>
    </div>
    <div class="field"><label for="f-notes">Anything else? <span class="opt">(optional)</span></label><textarea id="f-notes" name="notes" placeholder="What happened, number of passengers, access issues, keys…"></textarea></div>
    <div class="form-actions">
     <button class="btn btn--wa btn--lg" type="button" data-send-wa>{I['wa']}Send on WhatsApp</button>
     <button class="btn btn--primary btn--lg" type="submit">Submit request</button>
    </div>
    <p class="form-note">By sending this you agree we can contact you about your request. See our <a href="/privacy/">privacy policy</a>. For emergencies, please call.</p>
   </form>
  </div>
 </div>
 <aside>
  <div class="methods">
   <a class="method" href="{TEL}"><span class="ic" style="background:var(--amber);color:var(--on-amber)">{I['phone']}</span><span><small>Call {"24/7" if BIZ['is_24_7'] else "us"}</small><strong>{BIZ['phone_display']}</strong></span></a>
   <a class="method" href="{WA}"><span class="ic" style="background:var(--wa);color:var(--on-wa)">{I['wa']}</span><span><small>WhatsApp</small><strong>Message us</strong></span></a>
   <button class="method" type="button" data-share-location style="cursor:pointer;text-align:left;font:inherit;color:inherit;width:100%"><span class="ic" style="background:var(--ink);color:#fff">{I['nav']}</span><span><small>Fastest</small><strong>Send my location</strong></span></button>
   <a class="method" href="mailto:{BIZ['email']}"><span class="ic" style="background:var(--surface-2);color:var(--text)">{I['mail']}</span><span><small>Email</small><strong style="font-size:.98rem">{BIZ['email']}</strong></span></a>
  </div>
  <div class="aside-links"><h3>Hours</h3><p class="muted" style="margin:0">{BIZ['hours_text'] if BIZ['is_24_7'] else 'Call for availability'}. Based in Telford, Shropshire. Covering the UK.</p></div>
 </aside>
</div></section>'''
    build_page('/contact/', 'Contact & Quotes | Call or WhatsApp 07376 322865 | Rapid Rescue & Recovery',
               'Get help or a recovery quote. Call or WhatsApp 07376 322865, send your location in one tap, or fill in our quick form. Telford, Shropshire & UK-wide.',
               main, active='/contact/', schema=[crumbs_schema(crumbs)], priority='0.9')

def build_thanks():
    main = f'''<section class="section notfound"><div class="container">
<div class="code">Got it.</div><h1 style="font-size:clamp(1.6rem,4vw,2.4rem)">Thanks, your request has been sent.</h1>
<p class="lead" style="margin:0 auto 24px">We&rsquo;ll be in touch shortly. If it&rsquo;s urgent, don&rsquo;t wait: call us now.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--primary btn--lg" href="{TEL}">{I['phone']}{BIZ['phone_display']}</a><a class="btn btn--wa btn--lg" href="{WA}">{I['wa']}WhatsApp</a></div>
</div></section>'''
    out = head('/thank-you/', 'Thank you | Rapid Rescue & Recovery', 'Your request has been sent.', [org_schema()]).replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"') + header(None) + f'<main id="main">{main}</main>' + footer()
    write('/thank-you/', out)

def build_404():
    main = f'''<section class="section notfound"><div class="container">
<div class="code">404</div><h1 style="font-size:clamp(1.6rem,4vw,2.4rem)">This page has broken down.</h1>
<p class="lead" style="margin:0 auto 24px">Unlike your car, we can&rsquo;t tow it back. Try the homepage, or get in touch if you need help.</p>
<div class="btn-row" style="justify-content:center"><a class="btn btn--primary btn--lg" href="/">Go to homepage</a><a class="btn btn--ghost btn--lg" href="{TEL}">{I['phone']}{BIZ['phone_display']}</a></div>
</div></section>'''
    out = head('/404.html', 'Page not found | Rapid Rescue & Recovery', 'Page not found.', [org_schema()]).replace('<meta name="description"', '<meta name="robots" content="noindex">\n<meta name="description"') + header(None) + f'<main id="main">{main}</main>' + footer()
    write('/404.html', out)

def build_privacy():
    crumbs = [('/', 'Home'), ('/privacy/', 'Privacy policy')]
    main = page_hero(crumbs, 'Privacy policy', 'How we look after the information you give us.') + f'''
<section class="section"><div class="container"><div class="prose">
<p><em>Last updated: {datetime.date.today().strftime('%-d %B %Y')}</em></p>
<h2>Who we are</h2><p>{esc(BIZ['name'])} provides vehicle recovery and transport services from Telford, Shropshire. Contact us at <a href="mailto:{BIZ['email']}">{BIZ['email']}</a> or on {BIZ['phone_display']}.</p>
<h2>What we collect</h2><ul><li>Details you give us by phone, WhatsApp, email or our website form: your name, phone number, locations, vehicle details and notes about the job.</li><li>Your location, <strong>only</strong> when you choose to tap &ldquo;Send my location&rdquo; or &ldquo;Use GPS&rdquo;. Your device asks for permission first, and the location is placed into a message you send yourself.</li><li>Photos of your vehicle taken at pickup and drop-off.</li></ul>
<h2>Why we use it</h2><p>To respond to your request, carry out the recovery or transport, keep you updated, invoice you and keep records for insurance and legal purposes. The lawful bases are performing a contract with you, and our legitimate interests in running and protecting our business.</p>
<h2>Who we share it with</h2><p>Only where needed to do the job: for example, a partner recovery operator if your job is outside our local area, the garage or address you ask us to deliver to, or your insurer if you ask us to. Website form submissions are processed by our hosting provider, Netlify. WhatsApp messages are handled under WhatsApp&rsquo;s own privacy policy. We never sell your data.</p>
<h2>How long we keep it</h2><p>Job records and invoices are kept for up to 6 years for accounting purposes. Enquiries that don&rsquo;t become a job are deleted within 12 months.</p>
<h2>Cookies</h2><p>This website does not use tracking or advertising cookies. It stores one small setting on your device (your light/dark theme choice), which never leaves your browser.</p>
<h2>Your rights</h2><p>You can ask to see, correct or delete your information, or object to how we use it, by emailing <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>. You also have the right to complain to the Information Commissioner&rsquo;s Office at <a href="https://ico.org.uk" rel="noopener">ico.org.uk</a>.</p>
</div></div></section>'''
    build_page('/privacy/', 'Privacy Policy | Rapid Rescue & Recovery', 'How Rapid Rescue & Recovery collects, uses and protects your information.', main, schema=[crumbs_schema(crumbs)], priority='0.3')

# ---------------------------------------------------------------------------
# SEO + platform files
# ---------------------------------------------------------------------------
def build_meta_files():
    urls = ''.join(f'<url><loc>{DOMAIN}{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>' for p, pr in PAGES)
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nDisallow: /thank-you/\n\nSitemap: {DOMAIN}/sitemap.xml\n')
    manifest = {'name': BIZ['name'], 'short_name': 'Rapid Rescue', 'start_url': '/', 'display': 'standalone',
                'background_color': '#0B0D11', 'theme_color': '#0B0D11',
                'icons': [{'src': '/assets/img/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                          {'src': '/assets/img/icon-512.png', 'sizes': '512x512', 'type': 'image/png'},
                          {'src': '/assets/img/icon-maskable-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}]}
    open(os.path.join(ROOT, 'site.webmanifest'), 'w').write(json.dumps(manifest, indent=2))
    open(os.path.join(ROOT, '..', 'netlify.toml'), 'w').write('''# Netlify config. No build step: Netlify publishes the /site folder as-is.
[build]
  publish = "site"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    X-Frame-Options = "SAMEORIGIN"
    Referrer-Policy = "strict-origin-when-cross-origin"
    Permissions-Policy = "geolocation=(self), camera=(), microphone=()"
    Strict-Transport-Security = "max-age=31536000; includeSubDomains"

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"

# Send www to the bare domain
[[redirects]]
  from = "https://www.rapidrescuerecovery.co.uk/*"
  to = "https://rapidrescuerecovery.co.uk/:splat"
  status = 301
  force = true
''')

if __name__ == '__main__':
    build_home(); build_services(); build_areas(); build_guide(); build_trade(); build_contact(); build_thanks(); build_404(); build_privacy(); build_meta_files()
    print('Built', len(PAGES), 'pages ->', os.path.abspath(ROOT))
