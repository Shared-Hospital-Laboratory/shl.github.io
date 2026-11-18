# Shared Hospital Laboratory website (Jekyll)

A Jekyll port of https://www.sharedhospitallab.ca/ (originally built in Webflow),
based on the MIT-licensed [Jekyll Serif theme](https://github.com/zerostaticthemes/jekyll-serif-theme)
by zerostatic (see `LICENSE`).

## Run locally

    bundle install
    bundle exec jekyll serve      # http://localhost:4000

## Where to edit things

| What                         | File                                   |
| ---------------------------- | -------------------------------------- |
| Navigation & "About us" menu | `_data/menus.yml`                      |
| Contact email / phone        | `_data/contact.yml`                    |
| News items                   | `_data/news.yml`                       |
| Team members                 | `_team/*.md` (order by `weight`)       |
| Home page text               | `index.md`                             |
| Other pages                  | `shl-governance.md`, `certification.md`, `our-partners.md`, `time-line.md`, `shl-in-pictures.md`, `contact-us.md` |
| Colours & site-specific CSS  | `assets/css/style.scss`, `_sass/pages/_page-shl.scss` |
| Images / PDFs                | `images/shl/`, `docs/`                 |

URLs match the original site (`/shl-team/`, `/news/`, `/contact-us/`, …).

## Deploying to GitHub Pages

The `Gemfile` uses Jekyll 4, so deploy with the "GitHub Actions → Jekyll" workflow
(Settings → Pages → Source: GitHub Actions). If the site is served from a project
path (e.g. `user.github.io/shl-website/`), set `baseurl: '/shl-website'` in `_config.yml`.
