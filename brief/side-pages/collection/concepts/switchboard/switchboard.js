/* THE SWITCHBOARD — collection concept.
   Progressive enhancement only. With JS off every lamp renders lit and every
   switch is a plain <a href="?on=..."> the server (Liquid) resolves itself. */
(function () {
  'use strict';
  var rm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- 1. lamps light on arrival ---------------------------------------- */
  function lightAll(root) {
    (root || document).querySelectorAll('.lamp,.feature').forEach(function (l) { l.classList.add('lit'); });
  }
  if (rm || !('IntersectionObserver' in window)) {
    lightAll();
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('lit'); io.unobserve(e.target); }
      });
    }, { threshold: 0.25, rootMargin: '0px 0px -6% 0px' });
    document.querySelectorAll('.lamp,.feature').forEach(function (l) { io.observe(l); });
  }

  /* ---- 2. the board ------------------------------------------------------ */
  var board = document.querySelector('[data-board]');
  if (!board) return;
  var lamps = Array.prototype.slice.call(document.querySelectorAll('.lamp[data-sw]'));
  var boardLamps = Array.prototype.slice.call(board.querySelectorAll('.lamp'));
  var switches = Array.prototype.slice.call(document.querySelectorAll('[data-sw-key]'));
  var meterN = document.querySelector('[data-meter-n]');
  var meterT = document.querySelector('[data-meter-total]');
  var meterLab = document.querySelector('[data-meter-label]');
  var resetBtn = document.querySelector('[data-reset]');
  var spans = (board.getAttribute('data-spans') || '').split('|');
  var spansM = (board.getAttribute('data-spans-m') || '').split('|');
  var ars = (board.getAttribute('data-ars') || '').split('|');

  function keysOf(l) { return (l.getAttribute('data-sw') || '').split(' ').filter(Boolean); }
  function groupOf(k) { return k.split('-')[0]; }

  var active = [];

  function apply() {
    var groups = {};
    active.forEach(function (k) { (groups[groupOf(k)] = groups[groupOf(k)] || []).push(k); });
    var gnames = Object.keys(groups);
    var lit = 0;
    lamps.forEach(function (l) {
      var ks = keysOf(l);
      var ok = gnames.every(function (g) {
        return groups[g].some(function (k) { return ks.indexOf(k) > -1; });
      });
      if (ok) { l.removeAttribute('data-off'); lit++; } else { l.setAttribute('data-off', ''); }
    });
    if (meterN) meterN.textContent = String(lit);
    if (meterLab) meterLab.textContent = active.length ? 'דולקות' : 'כל הלוח דולק';
    switches.forEach(function (s) {
      s.setAttribute('aria-pressed', active.indexOf(s.getAttribute('data-sw-key')) > -1 ? 'true' : 'false');
    });
    if (resetBtn) resetBtn.hidden = active.length === 0;
    var url = new URL(window.location.href);
    if (active.length) url.searchParams.set('on', active.join(',')); else url.searchParams.delete('on');
    try { history.replaceState(null, '', url.pathname + url.search); } catch (e) { /* file:// */ }
  }

  /* ---- 3. the pips: which lamps each switch lights ----------------------- */
  switches.forEach(function (s) {
    var key = s.getAttribute('data-sw-key');
    var host = s.querySelector('[data-pips]');
    if (!host) return;
    lamps.forEach(function (l) {
      var i = document.createElement('i');
      if (keysOf(l).indexOf(key) > -1) i.className = 'on';
      host.appendChild(i);
    });
  });

  /* ---- 4. flipping ------------------------------------------------------- */
  switches.forEach(function (s) {
    s.addEventListener('click', function (ev) {
      ev.preventDefault();
      var key = s.getAttribute('data-sw-key');
      var i = active.indexOf(key);
      if (i > -1) active.splice(i, 1); else active.push(key);
      apply();
    });
    // preview on hover: dim what this switch does not light
    s.addEventListener('mouseenter', function () {
      if (active.length) return;
      var key = s.getAttribute('data-sw-key');
      lamps.forEach(function (l) {
        if (keysOf(l).indexOf(key) === -1) l.setAttribute('data-off', '');
      });
    });
    s.addEventListener('mouseleave', function () { if (!active.length) apply(); });
  });
  if (resetBtn) resetBtn.addEventListener('click', function (ev) { ev.preventDefault(); active = []; apply(); });

  /* ---- 5. server-side sort, mirrored in the browser ---------------------- */
  function priceOf(l) { return parseFloat(l.getAttribute('data-price') || '0'); }
  function restamp() {
    Array.prototype.slice.call(board.querySelectorAll('.lamp')).forEach(function (l, i) {
      if (spans[i]) l.style.setProperty('--sp', spans[i]);
      if (spansM[i]) l.style.setProperty('--spm', spansM[i]);
      if (ars[i]) l.style.setProperty('--ar', ars[i]);
      var n = l.querySelector('.lamp__num');
      if (n) n.textContent = ('0' + (i + numStart)).slice(-2);
    });
  }
  var numStart = parseInt(board.getAttribute('data-num-start') || '1', 10);
  var order = boardLamps.slice();
  function sortBy(mode) {
    var list = order.slice();
    if (mode === 'price-ascending') list.sort(function (a, b) { return priceOf(a) - priceOf(b); });
    else if (mode === 'price-descending') list.sort(function (a, b) { return priceOf(b) - priceOf(a); });
    list.forEach(function (l) { board.appendChild(l); });
    restamp();
    document.querySelectorAll('[data-sort]').forEach(function (a) {
      if (a.getAttribute('data-sort') === mode) a.setAttribute('aria-current', 'true');
      else a.removeAttribute('aria-current');
    });
    var url = new URL(window.location.href);
    if (mode && mode !== 'manual') url.searchParams.set('sort_by', mode); else url.searchParams.delete('sort_by');
    try { history.replaceState(null, '', url.pathname + url.search); } catch (e) {}
    lightAll(board);
  }
  document.querySelectorAll('[data-sort]').forEach(function (a) {
    a.addEventListener('click', function (ev) { ev.preventDefault(); sortBy(a.getAttribute('data-sort')); });
  });

  /* ---- 6. read the URL (this is what Liquid does server-side) ------------ */
  var q = new URLSearchParams(window.location.search);
  var on = (q.get('on') || '').split(',').filter(Boolean);
  var valid = switches.map(function (s) { return s.getAttribute('data-sw-key'); });
  active = on.filter(function (k) { return valid.indexOf(k) > -1; });
  if (meterT) meterT.textContent = String(lamps.length);
  apply();
  var sb = q.get('sort_by');
  if (sb) sortBy(sb);
})();
