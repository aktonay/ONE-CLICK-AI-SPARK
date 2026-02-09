/* =============================================================
   ONE CLICK AI SPARK — Safe RTD JavaScript Enhancements
   Non-destructive: no text wiping, no layout-breaking effects.
   ============================================================= */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    addCopyButtons();
    addProgressBar();
    addBackToTop();
  });

  /* ---------- Copy buttons on code blocks ---------- */
  function addCopyButtons() {
    document.querySelectorAll('.highlight pre, .rst-content pre').forEach(function (pre) {
      // skip if already has a button
      if (pre.querySelector('.oc-copy-btn')) return;

      var btn = document.createElement('button');
      btn.className = 'oc-copy-btn';
      btn.textContent = 'Copy';
      btn.style.cssText =
        'position:absolute;top:6px;right:6px;' +
        'background:#00b4d8;color:#fff;border:none;border-radius:4px;' +
        'padding:3px 10px;font-size:.78rem;font-weight:600;cursor:pointer;' +
        'opacity:.7;transition:opacity .2s;z-index:5;';

      btn.addEventListener('mouseenter', function () { btn.style.opacity = '1'; });
      btn.addEventListener('mouseleave', function () { btn.style.opacity = '.7'; });

      btn.addEventListener('click', function () {
        var code = pre.querySelector('code') || pre;
        var text = code.textContent || code.innerText;

        if (navigator.clipboard) {
          navigator.clipboard.writeText(text).then(function () {
            btn.textContent = 'Copied!';
            btn.style.background = '#10b981';
            setTimeout(function () { btn.textContent = 'Copy'; btn.style.background = '#00b4d8'; }, 1500);
          });
        }
      });

      // ensure relative positioning on parent
      var wrapper = pre.closest('.highlight') || pre;
      if (getComputedStyle(wrapper).position === 'static') {
        wrapper.style.position = 'relative';
      }
      wrapper.appendChild(btn);
    });
  }

  /* ---------- Reading progress bar ---------- */
  function addProgressBar() {
    var bar = document.createElement('div');
    bar.style.cssText =
      'position:fixed;top:0;left:0;height:3px;width:0;' +
      'background:linear-gradient(90deg,#00b4d8,#7c3aed,#f59e0b);' +
      'z-index:9999;transition:width .15s;pointer-events:none;';
    document.body.appendChild(bar);

    window.addEventListener('scroll', function () {
      var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
      var docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      bar.style.width = docHeight > 0 ? (scrollTop / docHeight * 100) + '%' : '0%';
    });
  }

  /* ---------- Back-to-top button ---------- */
  function addBackToTop() {
    var btn = document.createElement('button');
    btn.innerHTML = '&#8679;';  // ⇧
    btn.setAttribute('aria-label', 'Back to top');
    btn.style.cssText =
      'position:fixed;bottom:1.5rem;right:1.5rem;width:40px;height:40px;' +
      'border-radius:50%;border:none;font-size:1.3rem;line-height:1;' +
      'background:linear-gradient(135deg,#00b4d8,#7c3aed);color:#fff;' +
      'cursor:pointer;opacity:0;transition:opacity .3s,transform .2s;z-index:999;' +
      'box-shadow:0 2px 10px rgba(0,0,0,.3);';

    document.body.appendChild(btn);

    window.addEventListener('scroll', function () {
      btn.style.opacity = window.pageYOffset > 400 ? '1' : '0';
      btn.style.pointerEvents = window.pageYOffset > 400 ? 'auto' : 'none';
    });

    btn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    btn.addEventListener('mouseenter', function () { btn.style.transform = 'scale(1.1)'; });
    btn.addEventListener('mouseleave', function () { btn.style.transform = 'scale(1)'; });
  }

})();
