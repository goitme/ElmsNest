/* lamps light on arrival — one shared IntersectionObserver, never unlit again. */
(function () {
  var rm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var all = [].slice.call(document.querySelectorAll('[data-lamp]'));
  function light(el) { el.classList.add('lit'); }
  if (rm || !('IntersectionObserver' in window)) { all.forEach(light); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) { if (e.isIntersecting) { light(e.target); io.unobserve(e.target); } });
  }, { threshold: 0.25, rootMargin: '0px 0px -6% 0px' });
  all.forEach(function (el) { io.observe(el); });
  // sweep: anything already on screen at load lights immediately
  function sweep() {
    all.forEach(function (el) {
      if (el.classList.contains('lit')) return;
      var r = el.getBoundingClientRect();
      if (r.top < innerHeight * 0.94 && r.bottom > 0) light(el);
    });
  }
  addEventListener('load', sweep);
  addEventListener('scroll', sweep, { passive: true });
  sweep();
})();
