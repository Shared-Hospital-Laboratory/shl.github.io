---
title: Our History
layout: page
permalink: /time-line/
section: "About us"
lede: "From two founding hospitals in 1997 to a fully automated, 24/7 laboratory at Sunnybrook."
column: "col-lg-8"
---

<ol class="timeline">
  {% for entry in site.data.timeline %}
  <li class="timeline-entry">
    <span class="timeline-year">{{ entry.year }}</span>
    <ul class="timeline-events">
      {% for event in entry.events %}<li>{{ event }}</li>{% endfor %}
    </ul>
    {% if entry.photos or entry.logos %}
    <div class="timeline-media">
      {% for ph in entry.photos %}<img class="timeline-photo" src="{{ '/images/shl/timeline/' | append: ph | append: '.jpg' | relative_url }}" alt="" loading="lazy" />{% endfor %}
      {% for lg in entry.logos %}<img class="timeline-logo" src="{{ '/images/shl/partners/' | append: lg | append: '.jpg' | relative_url }}" alt="" loading="lazy" />{% endfor %}
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ol>
