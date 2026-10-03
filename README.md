# Rapid Rescue & Recovery: website

Static website for **rapidrescuerecovery.co.uk**. Plain HTML/CSS/JS, so there's no build step on Netlify and nothing to break.

```
netlify.toml   ← Netlify settings (publishes the /site folder, security headers, www → non-www)
site/          ← the live website (20 pages)
generator/     ← Python script that generates /site from one content file (optional, for edits)
brand-kit/     ← logo files, social profile picture, share image
```

## Deploy (GitHub → Netlify)

1. Create a new **private** GitHub repo, e.g. `rapid-rescue-recovery`.
2. Upload **everything in this folder** (keep the folder structure; `netlify.toml` must sit at the top level).
3. Netlify → **Add new site → Import an existing project → GitHub** → pick the repo.
   - Build command: *leave empty*
   - Publish directory: `site` (it's already set in `netlify.toml`)
4. Netlify → **Domain management** → add `rapidrescuerecovery.co.uk` and `www.rapidrescuerecovery.co.uk`. Point DNS at Netlify (or switch nameservers to Netlify DNS). HTTPS is automatic.
   - **Don't touch the MX records**, or the info@ email will stop working.
5. Netlify → **Forms** → enable form detection, then redeploy. Then go to **Forms → Notifications** → add an email notification to info@rapidrescuerecovery.co.uk for the `recovery-request` form.
6. Google Search Console → add the domain → submit `https://rapidrescuerecovery.co.uk/sitemap.xml`.

Every push to GitHub redeploys automatically.

## Before launch: confirm with the client

The site states these as facts. Change any that aren't true (they're all in `generator/content.py`):

- [ ] **24/7**: the site says open 24 hours, 7 days a week. If it isn't true, set `is_24_7 = False`.
- [ ] **Vehicles**: cars, vans up to 3.5t, 4x4s, SUVs, EVs and hybrids, all carried on the bed (assumes a flatbed/beavertail truck).
- [ ] **Payment methods**: card, Apple Pay, Google Pay, bank transfer and cash.
- [ ] **Passengers in the cab**: the site says "in most cases".
- [ ] **Photos at pickup and drop-off, and WhatsApp updates**: these are promises in the copy, so they need to actually happen on every job.
- [ ] **UK-wide partner network**: the site says out-of-area jobs go to trusted partner operators.
- [ ] **Trade accounts**: the site mentions agreed trade rates.

## Deliberately left out (add once real)

- **Reviews / testimonials**: none invented. Once the Google Business Profile is verified, paste the review link into `google_review_url` and add real reviews.
- **Social links**: fill in `socials` in `content.py` once the handles are claimed. Empty ones stay hidden.
- **Job photos**: real photos of the truck and jobs are the biggest trust upgrade. Add a gallery once there are 6+ good shots.
- **Accreditations** (PAS 43, IVR, AVRO): add badges only once they hold them.

## Editing content

Easiest: edit `generator/content.py` (phone, email, services, areas, FAQs), then run:

```
cd generator && python3 build.py
```

It rebuilds every page in `/site`. Commit and push. Small text fixes can also be made directly in the HTML files.

## What's built in

- **One-tap "Send my location"**: grabs the visitor's GPS and opens WhatsApp with a Google Maps pin already filled in. None of the competitor sites have this.
- Sticky Call / WhatsApp / Location bar on phones (iPhone safe-area aware), and a floating WhatsApp button on desktop.
- Quote form that sends **either** as a WhatsApp message **or** to email via Netlify Forms (with spam honeypot).
- Light and dark mode: follows the phone's setting automatically, with a manual toggle (auto → light → dark).
- SEO: unique title and description on every page, 6 service pages, 7 area pages (Telford, Shrewsbury, Wolverhampton, Newport, Bridgnorth, Shifnal, Nationwide), a "What to do if you break down" guide, TowingService + FAQ + Breadcrumb structured data, sitemap, robots.txt, Open Graph share image.
- Fast: no frameworks, no tracking, self-hosted fonts (~65KB total), all graphics as SVG.
- Accessibility: skip link, keyboard focus states, reduced-motion support, AA contrast in both themes.
