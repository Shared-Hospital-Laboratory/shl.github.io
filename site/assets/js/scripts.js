var body = document.querySelector('body');
var menuTrigger = document.querySelector('#toggle-main-menu-mobile');
var menuContainer = document.querySelector('#main-menu-mobile');

menuTrigger.onclick = function () {
  menuContainer.classList.toggle('open');
  menuTrigger.classList.toggle('is-active');
  body.classList.toggle('lock-scroll');
};

// Desktop "About us" dropdown: click/keyboard toggle (hover is handled in CSS)
document.querySelectorAll('.main-menu .has-children').forEach(function (item) {
  var toggle = item.querySelector('.submenu-toggle');
  toggle.addEventListener('click', function (e) {
    e.stopPropagation();
    var open = item.classList.toggle('open');
    toggle.setAttribute('aria-expanded', open);
  });
});
document.addEventListener('click', function () {
  document.querySelectorAll('.main-menu .has-children.open').forEach(function (item) {
    item.classList.remove('open');
    item.querySelector('.submenu-toggle').setAttribute('aria-expanded', 'false');
  });
});
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') document.dispatchEvent(new Event('click'));
});
