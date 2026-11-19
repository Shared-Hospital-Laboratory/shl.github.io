---
title: Genomics
layout: page
permalink: /genomics/
section: "Research"
lede: "Whole genome sequencing and bioinformatics at SHL support infection prevention and control, antimicrobial resistance testing and outbreak investigation across our member hospitals."
column: "col-lg-9"
---

SHL expanded into genomics in 2022. Sequencing is done on site and analyzed by SHL's bioinformatics team, so results can feed directly into clinical and infection-control decisions.

## What genomics is used for

<ul class="service-list">
  <li><h3>Transmission and outbreak investigation</h3><p>Comparing bacterial genomes to tell whether patients' infections are linked, for example in suspected hospital transmission of carbapenemase-producing organisms.</p></li>
  <li><h3>Antimicrobial resistance</h3><p>Detecting resistance genes and mutations, and comparing genotypic with phenotypic susceptibility testing for difficult-to-treat organisms.</p></li>
  <li><h3>Pathogen surveillance</h3><p>Characterizing circulating strains, such as invasive group A <em>Streptococcus</em>, to understand local epidemiology.</p></li>
  <li><h3>Viral genomics</h3><p>Sequencing respiratory viruses, including SARS-CoV-2, to investigate outbreaks and look for antiviral resistance.</p></li>
</ul>

## Genomics team

<ul class="people-inline">
  {% assign bio = site.team | where_exp: "m", "m.jobtitle contains 'Bioinformatic' or m.jobtitle contains 'Sequencing'" | sort: "weight" %}
  {% for m in bio %}
  <li><img src="{{ m.image | default: '/images/shl/team-placeholder.svg' | relative_url }}" alt="" /><span><strong>{{ m.title }}</strong><br>{{ m.jobtitle }}{% if m.email %}<br><a href="mailto:{{ m.email }}">{{ m.email }}</a>{% endif %}</span></li>
  {% endfor %}
</ul>

## Genomic Surveillance Reports

Interactive summaries of SHL's genomic surveillance data.

{% assign reports = site.reports | where_exp: "r", "r.published != false" | sort: "date" | reverse %}
{% if reports.size > 0 %}
<ul class="pub-list">
  {% for r in reports limit: 5 %}
  <li>
    <span class="pub-title"><a href="{{ r.url | relative_url }}">{{ r.title }}</a></span>
    <span class="pub-meta">{{ r.date | date: "%B %-d, %Y" }}{% if r.summary %} · {{ r.summary }}{% endif %}</span>
  </li>
  {% endfor %}
</ul>
{% else %}
<p>No reports have been published yet.</p>
{% endif %}

<p class="button-row"><a class="text-link" href="{{ '/genomics/reports/' | relative_url }}">All Genomic Surveillance Reports</a> <a class="text-link" href="{{ '/publications/' | relative_url }}">Publications by SHL team members</a></p>
