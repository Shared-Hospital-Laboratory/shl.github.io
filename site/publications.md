---
title: Publications
layout: page
permalink: /publications/
section: "Research"
lede: "Peer-reviewed publications by SHL team members with a Shared Hospital Laboratory affiliation, newest first. Team members are shown in bold; first and senior (last) authorships are labelled."
column: "col-lg-10"
---
{% assign pubs = site.data.publications_all %}
{% assign people = site.team | sort: "weight" %}

<div class="pub-filters" id="pub-filters">
  <div>
    <label for="pub-person">Team member</label>
    <select id="pub-person">
      <option value="">Everyone</option>
      {% for m in people %}{% assign slug = m.path | split: '/' | last | remove: '.md' %}
      {% assign has = pubs | where_exp: "p", "p.members contains slug" %}
      <option value="{{ slug }}">{{ m.title }}</option>{% endfor %}
    </select>
  </div>
  <div>
    <label for="pub-search">Search</label>
    <input type="search" id="pub-search" placeholder="Title, journal or author">
  </div>
  <label class="check"><input type="checkbox" id="pub-lead"> First or senior author only</label>
  <p class="pub-count" id="pub-count" aria-live="polite">{{ pubs.size }} publications</p>
</div>

{% assign by_year = pubs | group_by: "year" | sort: "name" | reverse %}
{% for y in by_year %}
<section class="pub-year-group" data-year="{{ y.name }}">
  <h2 class="pub-year">{{ y.name }}</h2>
  <ol class="pub-entries">
    {% for p in y.items %}
    {% assign member_authors = p.members | map: "author" %}
    {% assign member_slugs = p.members | map: "team" | join: " " %}
    {% assign lead_slugs = "" %}{% for m in p.members %}{% if m.role != "" %}{% assign lead_slugs = lead_slugs | append: m.team | append: " " %}{% endif %}{% endfor %}
    {% assign last_i = p.authors.size | minus: 1 %}
    <li data-members="{{ member_slugs }}" data-lead="{{ lead_slugs | strip }}" data-text="{{ p.title | append: ' ' | append: p.journal | append: ' ' | append: p.authors | join: ' ' | downcase | escape }}">
      <span class="pub-title">{% if p.doi != "" %}<a href="https://doi.org/{{ p.doi }}">{{ p.title }}</a>{% elsif p.pmid != "" %}<a href="https://pubmed.ncbi.nlm.nih.gov/{{ p.pmid }}/">{{ p.title }}</a>{% else %}{{ p.title }}{% endif %}</span>
      <span class="pub-authors">{% assign gap = false %}{% for a in p.authors %}{% assign show = false %}{% if forloop.index0 < 3 or forloop.index0 == last_i %}{% assign show = true %}{% endif %}{% if member_authors contains a %}{% assign show = true %}{% endif %}{% if show %}{% if gap %} … {% assign gap = false %}{% elsif forloop.index0 > 0 %}, {% endif %}{% if member_authors contains a %}<b>{{ a }}</b>{% else %}{{ a }}{% endif %}{% else %}{% assign gap = true %}{% endif %}{% endfor %}</span>
      <span class="pub-meta"><em>{{ p.journal }}</em>, {{ p.year }}</span>
      {% for m in p.members %}{% if m.role == "first" %}<span class="badge">First author: {{ m.name }}</span>{% elsif m.role == "last" %}<span class="badge badge-last">Senior author: {{ m.name }}</span>{% endif %}{% endfor %}
    </li>
    {% endfor %}
  </ol>
</section>
{% endfor %}
<p class="pub-empty" id="pub-empty">No publications match these filters.</p>

<p class="caption">Compiled from <a href="https://europepmc.org/">Europe PMC</a>: papers where an author lists Shared Hospital Laboratory as an affiliation. Authors are matched by name, so a paper may occasionally be missing or misattributed. To report a correction, <a href="mailto:{{ site.data.contact.email }}">email us</a>.</p>

<script>
(function () {
  var person = document.getElementById('pub-person');
  var search = document.getElementById('pub-search');
  var lead = document.getElementById('pub-lead');
  var count = document.getElementById('pub-count');
  var empty = document.getElementById('pub-empty');
  var items = Array.prototype.slice.call(document.querySelectorAll('.pub-entries > li'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.pub-year-group'));
  function apply() {
    var who = person.value, q = search.value.trim().toLowerCase(), leadOnly = lead.checked, n = 0;
    items.forEach(function (li) {
      var members = li.dataset.members.split(' '), leads = li.dataset.lead.split(' ');
      var ok = (!who || members.indexOf(who) > -1)
        && (!leadOnly || (who ? leads.indexOf(who) > -1 : li.dataset.lead !== ''))
        && (!q || li.dataset.text.indexOf(q) > -1);
      li.hidden = !ok;
      if (ok) n++;
    });
    groups.forEach(function (g) { g.hidden = !g.querySelector('.pub-entries > li:not([hidden])'); });
    count.textContent = n + (n === 1 ? ' publication' : ' publications');
    empty.style.display = n ? 'none' : 'block';
  }
  [person, lead].forEach(function (el) { el.addEventListener('change', apply); });
  search.addEventListener('input', apply);
})();
</script>
