// Paperwork dashboard — tabs, theme toggle, library card expansion.
// No frameworks, no build step. All state local to the browser.

(function () {
  'use strict';

  // ============================================================
  // Tabs (WAI-ARIA Tabs Pattern)
  // ============================================================
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role="tab"]'));
  var validTabs = new Set(tabs.map(function (t) { return t.id.replace('tab-', ''); }));

  function showTab(name) {
    if (!validTabs.has(name)) name = tabs[0] && tabs[0].id.replace('tab-', '');
    if (!name) return;
    tabs.forEach(function (tab) {
      var isActive = tab.id === 'tab-' + name;
      tab.setAttribute('aria-selected', isActive ? 'true' : 'false');
      tab.tabIndex = isActive ? 0 : -1;
    });
    document.querySelectorAll('[role="tabpanel"]').forEach(function (panel) {
      panel.hidden = panel.id !== 'panel-' + name;
    });
    var current = '#' + name;
    if (location.hash !== current) history.replaceState(null, '', current);
  }

  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () {
      showTab(tab.id.replace('tab-', ''));
    });
    tab.addEventListener('keydown', function (e) {
      var i = tabs.indexOf(tab);
      var next;
      if (e.key === 'ArrowLeft')  next = tabs[(i - 1 + tabs.length) % tabs.length];
      if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      if (e.key === 'Home')       next = tabs[0];
      if (e.key === 'End')        next = tabs[tabs.length - 1];
      if (next) {
        next.focus();
        showTab(next.id.replace('tab-', ''));
        e.preventDefault();
      }
    });
  });

  window.addEventListener('hashchange', function () {
    showTab(location.hash.slice(1));
  });

  if (tabs.length > 0) {
    showTab(location.hash.slice(1) || tabs[0].id.replace('tab-', ''));
  }

  // ============================================================
  // Theme toggle (System / Light / Dark)
  // ============================================================
  var themeButtons = Array.prototype.slice.call(
    document.querySelectorAll('.theme-toggle [data-theme-choice]')
  );

  function applyThemeChoice(choice) {
    if (choice === 'light' || choice === 'dark') {
      document.documentElement.dataset.theme = choice;
      document.documentElement.style.colorScheme = choice;
      localStorage.setItem('theme', choice);
    } else {
      delete document.documentElement.dataset.theme;
      document.documentElement.style.colorScheme =
        matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
      localStorage.removeItem('theme');
    }
    themeButtons.forEach(function (b) {
      b.setAttribute('aria-checked',
        b.dataset.themeChoice === (choice || 'system') ? 'true' : 'false');
    });
  }

  themeButtons.forEach(function (btn) {
    btn.addEventListener('click', function () {
      applyThemeChoice(btn.dataset.themeChoice);
    });
  });

  applyThemeChoice(localStorage.getItem('theme') || 'system');

  matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
    if (!localStorage.getItem('theme')) applyThemeChoice('system');
  });

  // ============================================================
  // Library card expansion
  // ============================================================
  document.querySelectorAll('.library-card').forEach(function (card) {
    card.addEventListener('click', function () {
      var slug = card.dataset.docSlug;
      var body = document.getElementById('doc-' + slug);
      if (!body) return;
      var nowOpen = body.hidden;
      document.querySelectorAll('.doc-body').forEach(function (d) {
        if (d !== body) d.hidden = true;
      });
      document.querySelectorAll('.library-card').forEach(function (c) {
        if (c !== card) c.setAttribute('aria-expanded', 'false');
      });
      body.hidden = !nowOpen;
      card.setAttribute('aria-expanded', nowOpen ? 'true' : 'false');
      if (nowOpen) body.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  document.querySelectorAll('.doc-close').forEach(function (closeBtn) {
    closeBtn.addEventListener('click', function (e) {
      e.stopPropagation();
      var body = closeBtn.closest('.doc-body');
      if (!body) return;
      body.hidden = true;
      var slug = body.id.replace('doc-', '');
      var card = document.querySelector('.library-card[data-doc-slug="' + slug + '"]');
      if (card) {
        card.setAttribute('aria-expanded', 'false');
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });
})();
