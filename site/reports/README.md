Standalone Plotly HTML reports live here (one file per report). The site keeps a
single copy of Plotly at `assets/js/vendor/plotly.min.js` (v2.35.2); reports load
it with a relative path instead of embedding their own copy.

To add a report:

1. Export your figure from Python, pointing at the shared Plotly copy:

       fig.write_html("site/reports/my-report.html",
                      include_plotlyjs="../assets/js/vendor/plotly.min.js",
                      full_html=True)

   (A string ending in `.js` makes Plotly write a `<script src=...>` tag
   rather than inlining 4.5 MB of JavaScript.)

2. Add `_reports/my-report.md` with front matter: `title`, `date`, `summary`
   and `file: "reports/my-report.html"` (optional `height:` in px for the
   embedded frame). Any Markdown below the front matter
   is shown above the figure.

3. The report appears at /genomics/reports/my-report/ and on the Genomic
   Surveillance Reports page.

The two `*-placeholder` reports use synthetic data; delete them (and their
`_reports/` entries) once real reports exist.
