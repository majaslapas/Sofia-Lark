/* Sofia Lark product page.
   One script for the product section and the sections under it: switching variants without a
   reload (price, stock, photograph, the phone bar and the delivery meter follow), adding to the
   cart through the theme's own cart (its drawer opens when the theme uses one, otherwise a short
   confirmation stays under the button), and the "wear it with" rows. Everything works without it:
   the form posts normally and the rows are plain links. */
(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function money(cents) {
    var t = window.theme;
    if (t && t.Currency && t.Currency.formatMoney && t.settings && t.settings.moneyFormat) {
      return t.Currency.formatMoney(cents, t.settings.moneyFormat);
    }
    return new Intl.NumberFormat('lv-LV', { style: 'currency', currency: 'EUR' }).format(cents / 100);
  }

  function cartRoutes() {
    var r = (window.theme && window.theme.routes) || {};
    return { add: r.cartAdd || '/cart/add.js', cart: r.cart || '/cart.js', page: r.cartPage || '/cart' };
  }

  function usesDrawer() {
    return !!(window.theme && window.theme.settings && window.theme.settings.cartType === 'drawer' &&
      document.querySelector('#CartDrawer, [data-cart-drawer], .drawer--cart'));
  }

  /* The header bubble, the same way the theme's own cart form updates it. */
  function updateHeaderCount(count) {
    document.querySelectorAll('.cart-link__bubble-num').forEach(function (el) { el.textContent = count; });
    document.querySelectorAll('.cart-link__bubble').forEach(function (el) {
      el.classList.toggle('cart-link__bubble--visible', count > 0);
    });
  }

  function refreshCart() {
    return fetch(cartRoutes().cart, { headers: { Accept: 'application/json' } })
      .then(function (r) { return r.json(); })
      .then(function (cart) {
        updateHeaderCount(cart.item_count);
        document.dispatchEvent(new CustomEvent('sl:cart-changed', { detail: { cart: cart } }));
        return cart;
      });
  }

  function addToCart(body) {
    return fetch(cartRoutes().add, {
      method: 'POST',
      body: body,
      headers: { 'X-Requested-With': 'XMLHttpRequest', Accept: 'application/json' }
    }).then(function (r) {
      return r.json().then(function (data) {
        if (!r.ok || data.status) throw data;
        return data;
      });
    });
  }

  /* Replaces a picture only if the visitor has not already moved on to another one. */
  function swapImage(img, src, srcset, alt) {
    if (!img || img.getAttribute('src') === src) return;
    var token = String(Date.now() + Math.random());
    img.dataset.slToken = token;
    img.classList.add('is-swapping');
    var pre = new Image();
    if (srcset) { pre.srcset = srcset; pre.sizes = img.sizes; }
    pre.onload = pre.onerror = function () {
      if (img.dataset.slToken !== token) return;
      if (srcset) img.srcset = srcset; else img.removeAttribute('srcset');
      img.src = src;
      if (alt != null) img.alt = alt;
      img.classList.remove('is-swapping');
    };
    pre.src = src;
  }

  /* ---------- the product section ---------- */

  function Product(root) {
    var jsonEl = root.querySelector('[data-sl-product-json]');
    if (!jsonEl) return;
    this.root = root;
    this.data = JSON.parse(jsonEl.textContent);
    this.form = root.querySelector('.sl-p__form');
    this.idInput = root.querySelector('[data-sl-variant-id]');
    this.addBtn = root.querySelector('[data-sl-add]');
    this.cartTotal = this.data.cartTotal;
    this.justAdded = false;
    this.variant = this.findById(Number(this.idInput.value)) || this.data.variants[0];

    this.bindOptions();
    this.bindForm();
    this.bindBar();
    this.bindDots();
    this.update(false);

    var self = this;
    document.addEventListener('sl:cart-changed', function (e) {
      self.cartTotal = e.detail.cart.total_price;
      self.updateMeter();
    });
  }

  Product.prototype.findById = function (id) {
    return this.data.variants.find(function (v) { return v.id === id; });
  };

  Product.prototype.selectedOptions = function () {
    return Array.prototype.map.call(this.root.querySelectorAll('[data-sl-option]'), function (fs) {
      var checked = fs.querySelector('input:checked');
      return checked ? checked.value : null;
    });
  };

  Product.prototype.bindOptions = function () {
    var self = this;
    this.root.querySelectorAll('[data-sl-option] input[type="radio"]').forEach(function (input) {
      input.addEventListener('change', function () {
        var chosen = self.selectedOptions();
        var match = self.data.variants.find(function (v) {
          return v.options.every(function (o, i) { return o === chosen[i]; });
        });
        self.variant = match || null;
        self.justAdded = false;
        self.update(true);
      });
    });
  };

  /* With more than one option, a value is crossed out when no variant with the other chosen
     values is in stock. With one option this is simply the variant's own stock. */
  Product.prototype.markAvailability = function () {
    var self = this;
    var chosen = this.selectedOptions();
    this.root.querySelectorAll('[data-sl-option]').forEach(function (fs) {
      var index = Number(fs.dataset.slOption);
      fs.querySelectorAll('input[type="radio"]').forEach(function (input) {
        var ok = self.data.variants.some(function (v) {
          if (!v.available || v.options[index] !== input.value) return false;
          return v.options.every(function (o, i) { return i === index || chosen[i] == null || o === chosen[i]; });
        });
        var label = fs.querySelector('label[for="' + input.id + '"]');
        if (label) label.classList.toggle('is-out', !ok);
      });
      var value = fs.querySelector('[data-sl-option-value]');
      if (value) value.textContent = chosen[index] || '';
    });
  };

  Product.prototype.stockLine = function (v) {
    var s = this.data.strings;
    if (!v || !v.available) return [s.soldOut, 'is-none'];
    if (v.qty === 1) return [s.last, 'is-low'];
    if (v.qty != null && v.qty <= this.data.lowStock) return [s.low.replace('[count]', v.qty), 'is-low'];
    return [s.inStock, ''];
  };

  Product.prototype.update = function (fromUser) {
    var v = this.variant;
    var root = this.root;
    this.markAvailability();

    var price = root.querySelector('[data-sl-price]');
    var was = root.querySelector('[data-sl-was]');
    var stock = root.querySelector('[data-sl-stock]');
    var label = root.querySelector('[data-sl-add-label]');
    var addPrice = root.querySelector('[data-sl-add-price]');
    var notify = root.querySelector('[data-sl-notify]');
    var available = !!(v && v.available);

    if (v) {
      this.idInput.value = v.id;
      price.textContent = money(v.price);
      var onSale = v.compare > v.price;
      was.hidden = !onSale;
      if (onSale) was.querySelector('[data-sl-was-amount]').textContent = money(v.compare);
    }

    var line = this.stockLine(v);
    stock.textContent = v ? line[0] : 'Šāda kombinācija nav pieejama';
    stock.className = 'sl-p__stock ' + line[1];

    this.addBtn.disabled = !available;
    label.textContent = available ? 'Pievienot grozam' : 'Izpārdots';
    addPrice.textContent = available ? money(v.price) : '';

    if (notify) {
      notify.hidden = available || !v;
      if (v) {
        var subject = this.data.title + ', ' + v.title + ': paziņot, kad pieejams';
        notify.href = 'mailto:' + notify.dataset.email + '?subject=' + encodeURIComponent(subject);
      }
    }

    if (fromUser && v && v.media) {
      swapImage(root.querySelector('.sl-p__media--lead img'), v.media.src, v.media.srcset, v.media.alt);
    }
    if (fromUser && v && window.history.replaceState) {
      var url = new URL(window.location.href);
      url.searchParams.set('variant', v.id);
      window.history.replaceState({}, '', url.toString());
    }

    this.updateBar();
    this.updateMeter();
  };

  Product.prototype.updateMeter = function () {
    var ship = this.root.querySelector('[data-sl-ship]');
    if (!ship || !this.data.free) return;
    var v = this.variant;
    var preview = this.cartTotal + (v && v.available && !this.justAdded ? v.price : 0);
    var left = this.data.free - preview;
    ship.querySelector('[data-sl-ship-text]').textContent = left > 0
      ? this.data.strings.freeLeft.replace('[amount]', money(left))
      : this.data.strings.freeDone;
    ship.querySelector('[data-sl-meter]').style.width = Math.min(100, preview / this.data.free * 100) + '%';
  };

  Product.prototype.bindForm = function () {
    var self = this;
    var error = this.root.querySelector('[data-sl-error]');
    var added = this.root.querySelector('[data-sl-added]');

    this.form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (self.addBtn.disabled) return;
      error.hidden = true;
      self.addBtn.classList.add('is-loading');
      self.addBtn.setAttribute('aria-busy', 'true');

      addToCart(new FormData(self.form))
        .then(function (item) {
          self.justAdded = true;
          if (usesDrawer()) {
            /* the theme's cart drawer listens for this, rebuilds itself and opens */
            self.form.dispatchEvent(new CustomEvent('ajaxProduct:added', {
              detail: { product: item, addToCartBtn: self.addBtn }, bubbles: true
            }));
          } else {
            added.querySelector('[data-sl-added-title]').textContent =
              item.product_title + (item.variant_title ? ', ' + item.variant_title : '') + ' · pievienots grozam';
            added.hidden = false;
          }
          self.addBtn.classList.add('is-done');
          setTimeout(function () { self.addBtn.classList.remove('is-done'); }, 1800);
          return refreshCart();
        })
        .catch(function (err) {
          error.textContent = (err && (err.description || err.message)) || 'Neizdevās pievienot grozam. Lūdzu, mēģini vēlreiz.';
          error.hidden = false;
        })
        .finally(function () {
          self.addBtn.classList.remove('is-loading');
          self.addBtn.removeAttribute('aria-busy');
        });
    });
  };

  Product.prototype.bindBar = function () {
    var bar = this.root.querySelector('[data-sl-bar]');
    if (!bar) return;
    var self = this;
    var barBtn = bar.querySelector('[data-sl-bar-add]');
    var footer = document.querySelector('.sl-footer, .site-footer');
    var on = false;
    var ticking = false;

    /* Measured on scroll rather than observed: a fast flick or a page restored half-way down can
       carry the button from below the screen to above it without ever crossing the edge. */
    function check() {
      ticking = false;
      if (getComputedStyle(bar).display === 'none') return;
      var pastButton = self.addBtn.getBoundingClientRect().bottom < 0;
      /* step out of the way at the footer so nothing there is ever covered */
      var atFooter = footer ? footer.getBoundingClientRect().top < window.innerHeight : false;
      var next = pastButton && !atFooter;
      if (next === on) return;
      on = next;
      bar.classList.toggle('is-shown', on);
      bar.setAttribute('aria-hidden', on ? 'false' : 'true');
      barBtn.tabIndex = on ? 0 : -1;
    }
    function queue() {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(check);
    }
    window.addEventListener('scroll', queue, { passive: true });
    window.addEventListener('resize', queue, { passive: true });
    check();

    barBtn.addEventListener('click', function () {
      if (self.variant && self.variant.available) {
        self.form.requestSubmit ? self.form.requestSubmit(self.addBtn) : self.addBtn.click();
      } else {
        self.root.querySelector('.sl-p__buy').scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth' });
      }
    });
  };

  Product.prototype.updateBar = function () {
    var bar = this.root.querySelector('[data-sl-bar]');
    if (!bar) return;
    var v = this.variant;
    var available = !!(v && v.available);
    var name = bar.querySelector('[data-sl-bar-variant]');
    if (v && v.title !== 'Default Title') name.textContent = v.title;
    bar.querySelector('[data-sl-bar-price]').textContent = v ? money(v.price) : '';
    var btn = bar.querySelector('[data-sl-bar-add]');
    btn.textContent = available ? 'Pievienot grozam' : 'Izvēlēties citu';
    btn.disabled = false;
    var img = bar.querySelector('.sl-p__bar-img');
    if (img && v && v.media) swapImage(img, v.media.thumb, null, '');
  };

  Product.prototype.bindDots = function () {
    var gallery = this.root.querySelector('[data-sl-gallery]');
    var dots = this.root.querySelector('[data-sl-dots]');
    if (!gallery || !dots) return;
    var figures = gallery.children;
    var ticking = false;
    gallery.addEventListener('scroll', function () {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(function () {
        ticking = false;
        var step = figures[0].getBoundingClientRect().width || 1;
        var i = Math.min(figures.length - 1, Math.round(gallery.scrollLeft / step));
        Array.prototype.forEach.call(dots.children, function (d, j) { d.classList.toggle('is-on', j === i); });
      });
    }, { passive: true });
  };

  /* ---------- "wear it with" rows ---------- */

  function Pair(root) {
    var photo = root.querySelector('[data-sl-pair-photo] img');
    var rows = root.querySelectorAll('[data-sl-pair-row]');
    function activate(row) {
      rows.forEach(function (r) {
        var on = r === row;
        r.classList.toggle('is-active', on);
        var head = r.querySelector('[data-sl-pair-head]');
        if (head) head.setAttribute('aria-expanded', on ? 'true' : 'false');
      });
      if (photo && row.dataset.image) swapImage(photo, row.dataset.image, row.dataset.srcset, row.dataset.alt);
    }
    rows.forEach(function (row) {
      var head = row.querySelector('[data-sl-pair-head]');
      head.addEventListener('click', function () { activate(row); });
      if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
        row.addEventListener('mouseenter', function () { activate(row); });
      }
      var form = row.querySelector('form');
      if (!form) return;
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var btn = form.querySelector('button');
        btn.classList.add('is-loading');
        addToCart(new FormData(form))
          .then(function (item) {
            btn.classList.add('is-done');
            btn.textContent = 'Pievienots grozam';
            if (usesDrawer()) {
              form.dispatchEvent(new CustomEvent('ajaxProduct:added', { detail: { product: item, addToCartBtn: btn }, bubbles: true }));
            }
            return refreshCart();
          })
          .catch(function () { btn.textContent = 'Neizdevās, mēģini vēlreiz'; })
          .finally(function () { btn.classList.remove('is-loading'); });
      });
    });
  }

  /* Products with nothing set up ask Shopify for its own recommendations once the page has
     loaded, and the section takes their place when there are any. */
  function recommend(el) {
    var url = el.dataset.slRecommend;
    if (!url) return;
    el.removeAttribute('data-sl-recommend');
    fetch(url)
      .then(function (r) { return r.ok ? r.text() : ''; })
      .then(function (text) {
        if (!text) return;
        var next = new DOMParser().parseFromString(text, 'text/html').querySelector('[data-sl-pair]');
        if (!next || !next.querySelector('[data-sl-pair-row]')) return;
        if (next.querySelectorAll('[data-sl-pair-row]').length <= el.querySelectorAll('[data-sl-pair-row]').length) return;
        next.removeAttribute('data-sl-recommend');
        el.replaceWith(next);
        init(next.parentNode);
      })
      .catch(function () {});
  }

  /* ---------- entrances: heading, then text, then picture ---------- */

  function rise(scope) {
    var items = scope.querySelectorAll('[data-sl-rise]');
    if (!items.length || reduceMotion || !('IntersectionObserver' in window)) return;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in');
        io.unobserve(e.target);
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    items.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top < window.innerHeight && r.bottom > 0) return; /* already on screen: leave it be */
      el.classList.add('is-waiting');
      io.observe(el);
    });
  }

  function init(scope) {
    scope.querySelectorAll('[data-sl-product]').forEach(function (el) {
      if (el.slProduct) return;
      el.slProduct = new Product(el);
    });
    scope.querySelectorAll('[data-sl-pair]').forEach(function (el) {
      if (el.slPair) return;
      el.slPair = true;
      Pair(el);
      recommend(el);
    });
    rise(scope);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { init(document); });
  } else {
    init(document);
  }
  document.addEventListener('shopify:section:load', function (e) { init(e.target); });
})();
