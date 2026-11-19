---
title: Our Partners
layout: page
permalink: /our-partners/
section: "About us"
lede: "SHL is jointly operated by four Toronto hospitals and also provides microbiology services to client hospitals elsewhere in Ontario."
column: "col-12"
---

<ul class="partner-grid">
  {% for p in site.data.partners.members %}{% include partner-card.html p=p %}{% endfor %}
  {% for p in site.data.partners.clients %}{% include partner-card.html p=p %}{% endfor %}
</ul>
