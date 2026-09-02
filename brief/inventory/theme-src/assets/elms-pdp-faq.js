/**
 * ElmsNest PDP — accordion a11y bridge.
 *
 * The markup is native <details>/<summary>, so opening and closing already
 * works with Tab + Enter/Space and keeps working if this file never loads.
 * What <details> does NOT do is expose aria-expanded, which some screen
 * readers still rely on to announce state. This mirrors the open property
 * onto aria-expanded on the summary.
 *
 * Delegated from the document and guarded by a flag, so any number of
 * accordion sections on the page share one listener and a re-render from the
 * theme editor never stacks duplicates.
 */
(function () {
  if (window.__elmsPdpFaqBound) return;
  window.__elmsPdpFaqBound = true;

  var SELECTOR = '.elms-faq__item';

  function sync(details) {
    if (!details) return;
    var summary = details.querySelector('.elms-faq__summary');
    if (!summary) return;
    summary.setAttribute('aria-expanded', details.open ? 'true' : 'false');
  }

  function syncAll(root) {
    var scope = root && root.querySelectorAll ? root : document;
    var items = scope.querySelectorAll(SELECTOR);
    for (var i = 0; i < items.length; i++) sync(items[i]);
  }

  // The toggle event does not bubble, so capture it instead of listening on
  // each <details> individually.
  document.addEventListener(
    'toggle',
    function (event) {
      var details = event.target;
      if (details && details.matches && details.matches(SELECTOR)) sync(details);
    },
    true
  );

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      syncAll(document);
    });
  } else {
    syncAll(document);
  }

  // Theme editor re-renders a section without a page load.
  document.addEventListener('shopify:section:load', function (event) {
    syncAll(event.target);
  });
})();
