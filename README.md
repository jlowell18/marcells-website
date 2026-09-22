# marcellspaper.com

The public website for Marcells Paper & Metal, served by Cloudflare Pages.

- Page text lives in `tools/content.py`; `tools/build_site.py` turns it into `site/*.html`.
- `site/styles.css` is the whole design. `site/assets/` holds the images.
- Every push to `main` deploys (`.github/workflows/deploy.yml`). Preview: https://marcells-website.pages.dev
- `.github/workflows/cloudflare-check.yml` verifies the Cloudflare secrets and writes the result to the `status` branch.
- Client Login points at the customer portal: https://portal.marcellspaper.com
