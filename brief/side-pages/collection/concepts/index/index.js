/* THE INDEX — lamps light as each row is reached. No JS / reduced motion = everything lit. */
(function () {
  var rm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var lamps = [].slice.call(document.querySelectorAll('[data-lamp]'));
  function lightAll() { lamps.forEach(function (l) { l.classList.add('lit'); }); }
  if (rm || !('IntersectionObserver' in window)) { lightAll(); return; }
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) { e.target.classList.add('lit'); io.unobserve(e.target); }
    });
  }, { threshold: 0.25, rootMargin: '0px 0px -6% 0px' });
  lamps.forEach(function (l) { io.observe(l); });
  // safety net: anything still dark after 6s (image never decoded, observer never fired) lights anyway
  setTimeout(lightAll, 6000);
})();
