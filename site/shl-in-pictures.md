---
title: SHL In Pictures
layout: page
permalink: /shl-in-pictures/
gallery:
  - file: lab-screens-and-techs.jpg
    alt: "Technologists at their workstations in the SHL lab"
  - file: lab-pipette.jpg
    alt: "A technologist pipetting next to a BD Kiestra instrument"
  - file: lab-screen.jpg
    alt: "Reviewing digital culture plate images on screen"
  - file: lab-agar-ids.jpg
    alt: "Digital image of a blood agar plate with colonies marked for identification"
  - file: lab-tubes-and-plates.jpg
    alt: "Automated plate handling inside the BD Kiestra system"
  - file: lab-tubes.jpg
    alt: "Specimen tubes racked in the automated processor"
section: "About us"
---

![The SHL team]({{ '/images/shl/group.jpg' | relative_url }}){: .shadow-two .img-full}

## Lab in pictures

See inside our lab.

<div class="gallery">
  {% for photo in page.gallery %}
  <a href="{{ '/images/shl/' | append: photo.file | relative_url }}"><img class="shadow-two" src="{{ '/images/shl/' | append: photo.file | relative_url }}" alt="{{ photo.alt }}" loading="lazy" /></a>
  {% endfor %}
</div>
