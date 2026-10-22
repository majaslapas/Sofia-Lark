/* Sofia Lark filter bar (snippets/sl-filters.liquid): a choice reloads the page with it at once;
   one panel open at a time, closed by Esc, a click outside or its close button; on phones the page
   behind an open sheet does not scroll. */
(() => {
  const root = document.querySelector('[data-sl-filters]');
  if (!root) return;
  const form = root.querySelector('[data-sl-filters-form]');
  const groups = Array.from(root.querySelectorAll('[data-sl-filter]'));
  const phone = window.matchMedia('(max-width: 768px)');

  // empty price fields are left out of the address, so they do not count as a filter
  const tidy = () => {
    form.querySelectorAll('input[type="number"]').forEach((input) => {
      input.disabled = input.value.trim() === '';
    });
  };
  const submit = () => {
    tidy();
    root.classList.add('is-loading');
    form.submit();
  };

  form.addEventListener('submit', tidy);
  form.addEventListener('change', (event) => {
    if (event.target.matches('input[type="checkbox"], select')) submit();
  });

  const lock = () => {
    document.documentElement.classList.toggle('sl-fl-lock', phone.matches && groups.some((g) => g.open));
  };
  const close = (group, focus) => {
    if (!group.open) return;
    group.open = false;
    if (focus) group.querySelector('summary').focus();
  };

  groups.forEach((group) => {
    group.addEventListener('toggle', () => {
      if (group.open) {
        groups.forEach((other) => other !== group && close(other));
        // a panel that would run off the right edge opens towards the left instead
        group.classList.remove('is-right');
        const panel = group.querySelector('.sl-fl__panel');
        if (!phone.matches && panel.getBoundingClientRect().right > document.documentElement.clientWidth - 8) {
          group.classList.add('is-right');
        }
      }
      lock();
    });
    const button = group.querySelector('[data-sl-filter-close]');
    if (button) button.addEventListener('click', () => close(group, true));
  });

  document.addEventListener('click', (event) => {
    groups.forEach((group) => {
      if (group.open && !group.contains(event.target)) close(group);
    });
  });
  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    groups.forEach((group) => {
      if (group.open) close(group, true);
    });
  });

  // the Veids links open another address (/collections/<handle>/<kind>); they keep the price,
  // material and other choices and the sort already made, but not the page number
  root.querySelectorAll('[data-sl-keep]').forEach((link) => {
    link.addEventListener('click', () => {
      const params = new URLSearchParams(window.location.search);
      params.delete('page');
      const url = new URL(link.href);
      url.search = params.toString();
      link.href = url.toString();
      root.classList.add('is-loading');
    });
  });

  // coming back with the browser's back button shows the page as it was, not dimmed
  window.addEventListener('pageshow', () => root.classList.remove('is-loading'));
})();
