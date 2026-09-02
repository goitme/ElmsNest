/* המתג — shared plumbing: lamps on arrival, the drawn string, the counting price,
   the sticky buy bar, and the mockup form interception. Vanilla, offline. */
window.SW = (function () {
  var rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';
  function el(n, a) { var e = document.createElementNS(NS, n); for (var k in a) e.setAttribute(k, a[k]); return e; }

  /* ---------- lamps: dim → lit once, never back ---------- */
  var lamps = [];
  function light(node) {
    if (node.classList.contains('lit')) return;
    node.classList.add('lit');
    node.dispatchEvent(new CustomEvent('lamp', { bubbles: false }));
  }
  function sweep() {
    var vh = window.innerHeight;
    lamps.forEach(function (n) {
      if (n.classList.contains('lit')) return;
      var r = n.getBoundingClientRect();
      if (r.top < vh * 0.82 && r.bottom > vh * 0.1) light(n);
    });
  }
  function observeLamps(root) {
    var list = (root || document).querySelectorAll('[data-lamp]');
    if (rm || !('IntersectionObserver' in window)) { list.forEach(light); return; }
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { light(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.25, rootMargin: '0px 0px -6% 0px' });
    list.forEach(function (n) { lamps.push(n); io.observe(n); });
  }

  /* ---------- the drawn string: bulbs hung along a cord ---------- */
  var PAL = {
    yellow: { core: '#fff1d6', halo: 'gold' },
    blue: { core: '#dbe9ff', halo: 'blue' },
    white: { core: '#ffffff', halo: 'white' },
    multi: [{ core: '#ffd6d4', halo: 'red' }, { core: '#dcffe4', halo: 'green' }, { core: '#dbe9ff', halo: 'blue' }, { core: '#fff1d6', halo: 'gold' }]
  };
  var GRADS = { gold: '#ffd394', blue: '#5b9dff', white: '#e9f0ff', red: '#ff7a6b', green: '#7dffa0' };

  function makeString(svg, o) {
    o = Object.assign({ max: 200, spacing: 28, sag: 70, rowGap: 96, area: null, mobile: { spacing: 15, sag: 26, rowGap: 34 }, haloR: 16, coreR: 4.2, drop: 8 }, o || {});
    var id = svg.id || ('s' + Math.random().toString(36).slice(2, 7));
    var defs = el('defs');
    for (var k in GRADS) {
      var g = el('radialGradient', { id: id + '-' + k, cx: '50%', cy: '50%', r: '50%' });
      g.appendChild(el('stop', { offset: '0', 'stop-color': GRADS[k], 'stop-opacity': '.8' }));
      g.appendChild(el('stop', { offset: '.45', 'stop-color': GRADS[k], 'stop-opacity': '.28' }));
      g.appendChild(el('stop', { offset: '1', 'stop-color': GRADS[k], 'stop-opacity': '0' }));
      defs.appendChild(g);
    }
    var cord = el('path', { 'class': 'cord' });
    var gb = el('g');
    svg.appendChild(defs); svg.appendChild(cord); svg.appendChild(gb);
    var bulbs = [], n = 0, col = 'yellow', total = 0, sp = o.spacing, measure = el('path');

    function layout() {
      var W = svg.clientWidth, H = svg.clientHeight;
      if (!W || !H) return;
      var mob = W < 720, m = mob ? o.mobile : o;
      sp = m.spacing;
      var area = o.area ? o.area(W, H) : { top: 60, bottom: H * 0.55 };
      var S = Math.max(170, Math.min(470, W / 3.2));
      var x = W, y = area.top, dir = -1, d = 'M' + x + ' ' + y, need = (o.max + 1) * sp;
      for (var r = 0; r < 40; r++) {
        var cols = Math.ceil(W / S);
        for (var c = 0; c < cols; c++) {
          var x1 = dir < 0 ? Math.max(0, x - S) : Math.min(W, x + S), xm = (x + x1) / 2;
          d += ' Q' + xm.toFixed(1) + ' ' + (y + m.sag) + ' ' + x1.toFixed(1) + ' ' + y;
          x = x1;
        }
        measure.setAttribute('d', d);
        if (measure.getTotalLength() >= need || y + m.rowGap > area.bottom) break;
        y += m.rowGap; d += ' L' + x + ' ' + y; dir = -dir;
      }
      cord.setAttribute('d', d);
      total = measure.getTotalLength();
      gb.innerHTML = ''; bulbs = [];
      var hr = mob ? o.haloR * 0.62 : o.haloR, cr = mob ? o.coreR * 0.62 : o.coreR, drop = mob ? o.drop * 0.6 : o.drop;
      for (var i = 0; i < o.max; i++) {
        var L = Math.min(total - 1, sp * (i + 0.6)), pt = measure.getPointAtLength(L);
        var b = el('g', { 'class': 'b', transform: 'translate(' + pt.x.toFixed(1) + ' ' + (pt.y + drop).toFixed(1) + ')' });
        b.appendChild(el('circle', { 'class': 'halo', r: hr }));
        b.appendChild(el('circle', { 'class': 'core', r: cr }));
        gb.appendChild(b); bulbs.push(b);
      }
      applyColour(); applyN(false, 0);
    }
    function applyColour() {
      bulbs.forEach(function (b, i) {
        var p = col === 'multi' ? PAL.multi[i % 4] : PAL[col];
        b.firstChild.setAttribute('fill', 'url(#' + id + '-' + p.halo + ')');
        b.lastChild.setAttribute('fill', p.core);
      });
    }
    function applyN(anim, from) {
      var grow = Math.max(1, n - from), step = Math.min(70, 1500 / grow);
      bulbs.forEach(function (b, i) {
        var on = i < n, dl = 0;
        if (anim && !rm && on && i >= from) dl = Math.round((i - from) * step);
        b.style.setProperty('--dl', dl + 'ms');
        b.classList.toggle('on', on);
      });
      var vis = Math.min(total, sp * (n + 0.6));
      cord.style.strokeDasharray = vis.toFixed(1) + ' ' + (total + 10).toFixed(1);
    }
    var t;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(layout, 160); });
    layout();
    return {
      set: function (count, anim) { var from = n; n = Math.max(0, Math.min(o.max, count)); applyN(anim !== false, from < n ? from : 0); },
      colour: function (name) { col = name; applyColour(); },
      dark: function (on) {
        if (on) {
          if (rm) { svg.classList.add('dark'); return; }
          svg.classList.add('try');
          setTimeout(function () { svg.classList.add('dark'); svg.classList.remove('try'); }, 900);
        } else { svg.classList.remove('dark', 'try'); }
      },
      relayout: layout,
      count: function () { return n; }
    };
  }


  /* ---------- the drawn path: bollards standing along a receding line ---------- */
  function makePath(svg, o) {
    o = Object.assign({ max: 8, line: null }, o || {});
    var id = svg.id || ('p' + Math.random().toString(36).slice(2, 7));
    var defs = el('defs');
    var g1 = el('radialGradient', { id: id + '-pool', cx: '50%', cy: '50%', r: '50%' });
    g1.appendChild(el('stop', { offset: '0', 'stop-color': '#ffd394', 'stop-opacity': '.75' }));
    g1.appendChild(el('stop', { offset: '.5', 'stop-color': '#ffd394', 'stop-opacity': '.22' }));
    g1.appendChild(el('stop', { offset: '1', 'stop-color': '#ffd394', 'stop-opacity': '0' }));
    var g2 = el('linearGradient', { id: id + '-cone', x1: '0', y1: '0', x2: '0', y2: '1' });
    g2.appendChild(el('stop', { offset: '0', 'stop-color': '#ffd394', 'stop-opacity': '.5' }));
    g2.appendChild(el('stop', { offset: '1', 'stop-color': '#ffd394', 'stop-opacity': '0' }));
    var g3 = el('radialGradient', { id: id + '-glow', cx: '50%', cy: '50%', r: '50%' });
    g3.appendChild(el('stop', { offset: '0', 'stop-color': '#fff1d6', 'stop-opacity': '.9' }));
    g3.appendChild(el('stop', { offset: '.4', 'stop-color': '#ffd394', 'stop-opacity': '.35' }));
    g3.appendChild(el('stop', { offset: '1', 'stop-color': '#ffd394', 'stop-opacity': '0' }));
    defs.appendChild(g1); defs.appendChild(g2); defs.appendChild(g3);
    var ground = el('path', { 'class': 'ground' }), gb = el('g');
    svg.appendChild(defs); svg.appendChild(ground); svg.appendChild(gb);
    var items = [], n = 0;
    function layout() {
      var W = svg.clientWidth, H = svg.clientHeight; if (!W || !H) return;
      var L = o.line(W, H, W < 720);
      ground.setAttribute('d', 'M' + L.x0 + ' ' + L.y0 + ' L' + L.x1 + ' ' + L.y1);
      gb.innerHTML = ''; items = [];
      for (var i = o.max - 1; i >= 0; i--) {
        var t = i / (o.max - 1) * 0.94, s = 1 - 0.7 * t;
        var x = L.x0 + (L.x1 - L.x0) * t, y = L.y0 + (L.y1 - L.y0) * t, h = L.h * s, w = Math.max(5, L.h * 0.13 * s);
        var b = el('g', { 'class': 'b', transform: 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ')' });
        b.appendChild(el('ellipse', { 'class': 'halo', cx: 0, cy: 0, rx: (h * .8).toFixed(1), ry: (h * .17).toFixed(1), fill: 'url(#' + id + '-pool)' }));
        b.appendChild(el('polygon', { 'class': 'halo', points: (-w * .5) + ',' + (-h * .7) + ' ' + (w * .5) + ',' + (-h * .7) + ' ' + (h * .5) + ',0 ' + (-h * .5) + ',0', fill: 'url(#' + id + '-cone)' }));
        b.appendChild(el('rect', { 'class': 'post', x: -w / 2, y: -h * .7, width: w, height: h * .7 }));
        b.appendChild(el('circle', { 'class': 'halo', cx: 0, cy: -h * .85, r: (h * .5).toFixed(1), fill: 'url(#' + id + '-glow)' }));
        b.appendChild(el('rect', { 'class': 'core', x: -w / 2, y: -h, width: w, height: h * .3, fill: '#fff1d6' }));
        b.appendChild(el('rect', { 'class': 'cap', x: -w / 2 - 1, y: -h - 2.5, width: w + 2, height: 2.5 }));
        gb.appendChild(b); items[i] = b;
      }
      applyN(false, 0);
    }
    function applyN(anim, from) {
      items.forEach(function (b, i) {
        var on = i < n, dl = 0;
        if (anim && !rm && on && i >= from) dl = (i - from) * 140;
        b.style.setProperty('--dl', dl + 'ms');
        b.classList.toggle('on', on);
      });
    }
    var t;
    window.addEventListener('resize', function () { clearTimeout(t); t = setTimeout(layout, 160); });
    layout();
    return {
      set: function (count, anim) { var from = n; n = Math.max(0, Math.min(o.max, count)); applyN(anim !== false, from < n ? from : 0); },
      dark: function (on) {
        if (on) { if (rm) { svg.classList.add('dark'); return; } svg.classList.add('try'); setTimeout(function () { svg.classList.add('dark'); svg.classList.remove('try'); }, 900); }
        else { svg.classList.remove('dark', 'try'); }
      },
      relayout: layout, count: function () { return n; }
    };
  }

  /* ---------- the price counts up ---------- */
  function fmt(v) { return v.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
  function countTo(node, to, dur) {
    var from = parseFloat(node.dataset.v != null ? node.dataset.v : to);
    node.dataset.v = to;
    if (rm || from === to) { node.textContent = fmt(to); return; }
    var t0 = performance.now(); dur = dur || 560;
    (function f(t) {
      var k = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - k, 3);
      node.textContent = fmt(from + (to - from) * e);
      if (k < 1) requestAnimationFrame(f);
    })(t0);
  }

  /* ---------- sticky buy bar: shows once the stage's buy scrolls out above ---------- */
  function stickyBar(anchor, bar) {
    if (!anchor || !bar) return;
    document.body.classList.add('has-sbar');
    var limit = 0, tick = false;
    function measure() { var r = anchor.getBoundingClientRect(); limit = r.bottom + window.scrollY; }
    function check() {
      if (tick) return; tick = true;
      requestAnimationFrame(function () {
        var show = window.scrollY > limit && window.scrollY > 10;
        bar.classList.toggle('show', show); bar.setAttribute('aria-hidden', String(!show)); tick = false;
      });
    }
    measure(); check();
    window.addEventListener('scroll', check, { passive: true });
    window.addEventListener('resize', function () { measure(); check(); });
    window.addEventListener('load', function () { measure(); check(); });
  }

  /* ---------- mockup: forms don't post anywhere ---------- */
  function mockForms() {
    document.querySelectorAll('form[action="/cart/add"]').forEach(function (f) {
      f.addEventListener('submit', function (e) {
        e.preventDefault();
        var btns = document.querySelectorAll('button[form="' + f.id + '"], #' + f.id + ' button[type=submit]');
        btns.forEach(function (btn) { var t = btn.textContent; btn.textContent = 'נוסף לסל'; setTimeout(function () { btn.textContent = t; }, 1600); });
      });
    });
  }

  /* smooth anchors (kept out of CSS so scripted scrolls stay instant) */
  function anchors() {
    document.querySelectorAll('a[href^="#"]').forEach(function (a) {
      a.addEventListener('click', function (e) {
        var t = document.querySelector(a.getAttribute('href'));
        if (!t) return; e.preventDefault();
        t.scrollIntoView({ behavior: rm ? 'auto' : 'smooth', block: 'start' });
      });
    });
  }

  window.addEventListener('scroll', function () { requestAnimationFrame(sweep); }, { passive: true });

  return { rm: rm, el: el, NS: NS, observeLamps: observeLamps, light: light, sweep: sweep, makeString: makeString, makePath: makePath, countTo: countTo, fmt: fmt, stickyBar: stickyBar, mockForms: mockForms, anchors: anchors };
})();
