---
title: Genomic Surveillance Reports
layout: page
permalink: /genomics/reports/
section: "Research"
lede: "Interactive summaries of SHL's genomic surveillance data."
---

{% assign reports = site.reports | where_exp: "r", "r.published != false" | sort: "date" | reverse %}
{% if reports.size > 0 %}
<ul class="pub-list">
  {% for r in reports %}
  <li>
    <span class="pub-title"><a href="{{ r.url | relative_url }}">{{ r.title }}</a></span>
    <span class="pub-meta">{{ r.date | date: "%B %-d, %Y" }}{% if r.summary %} · {{ r.summary }}{% endif %}</span>
  </li>
  {% endfor %}
</ul>
{% else %}
<div class="empty-state">
  <p>No reports have been published yet. Check back soon.</p>
</div>
{% endif %}
