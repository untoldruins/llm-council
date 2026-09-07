/* Sekaidao — progressive enhancement only. The site is fully usable without JS. */
(function () {
  "use strict";

  // ---- mobile navigation ---------------------------------------------------
  var toggle = document.querySelector("[data-nav-toggle]");
  var nav = document.querySelector("[data-nav]");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.getAttribute("data-open") === "true";
      nav.setAttribute("data-open", String(!open));
      toggle.setAttribute("aria-expanded", String(!open));
    });

    // Close the drawer when a link is followed or the viewport grows.
    nav.addEventListener("click", function (e) {
      if (e.target.closest("a")) {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      }
    });

    window.addEventListener("resize", function () {
      if (window.innerWidth > 900) {
        nav.setAttribute("data-open", "false");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // ---- FAQ accordions ------------------------------------------------------
  // <details> already works on its own; this just keeps one item open per group.
  document.querySelectorAll("[data-faq-group]").forEach(function (group) {
    var items = group.querySelectorAll("details.faq-item");
    items.forEach(function (item) {
      item.addEventListener("toggle", function () {
        if (!item.open) return;
        items.forEach(function (other) {
          if (other !== item) other.open = false;
        });
      });
    });
  });

  // ---- contact form (no backend in this static build) ----------------------
  var form = document.querySelector("[data-quote-form]");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var note = form.querySelector("[data-form-note]");
      if (note) {
        note.textContent =
          "Thanks — this is a static demo build, so nothing was sent. " +
          "Wire the form action up to your form handler or CRM to go live.";
        note.style.color = "#1f5ce0";
      }
    });
  }
})();
