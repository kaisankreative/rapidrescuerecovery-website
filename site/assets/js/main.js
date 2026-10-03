/* Rapid Rescue & Recovery — main.js (no dependencies) */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");

  var CFG = window.RRR || {};
  var WA_NUMBER = CFG.wa || "447376322865";

  /* ---------- Theme: auto (device) / light / dark ---------- */
  var KEY = "rrr-theme";
  function getMode() { try { return localStorage.getItem(KEY) || "auto"; } catch (e) { return "auto"; } }
  function applyMode(mode) {
    if (mode === "light" || mode === "dark") doc.setAttribute("data-theme", mode);
    else doc.removeAttribute("data-theme");
    var isDark = mode === "dark" || (mode === "auto" && window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches);
    var meta = document.querySelector('meta[name="theme-color"]:not([media])');
    if (meta) meta.setAttribute("content", isDark ? "#0B0D11" : "#F6F5F1");
    document.querySelectorAll(".theme-toggle").forEach(function (b) {
      b.setAttribute("data-mode", mode);
      var label = { auto: "Theme: matches your device", light: "Theme: light", dark: "Theme: dark" }[mode];
      b.setAttribute("aria-label", label + " (tap to change)");
      b.setAttribute("title", label);
    });
  }
  applyMode(getMode());
  document.querySelectorAll(".theme-toggle").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var order = ["auto", "light", "dark"];
      var next = order[(order.indexOf(getMode()) + 1) % order.length];
      try { localStorage.setItem(KEY, next); } catch (e) {}
      applyMode(next);
      toast(next === "auto" ? "Theme follows your device" : (next === "dark" ? "Dark mode on" : "Light mode on"));
    });
  });

  /* ---------- Mobile menu ---------- */
  var menu = document.getElementById("mobile-menu");
  function setMenu(open) {
    if (!menu) return;
    menu.classList.toggle("open", open);
    document.body.classList.toggle("menu-open", open);
    menu.setAttribute("aria-hidden", open ? "false" : "true");
    document.querySelectorAll(".menu-btn").forEach(function (b) { b.setAttribute("aria-expanded", open ? "true" : "false"); });
    if (open) { var c = menu.querySelector(".menu-close"); if (c) c.focus(); }
  }
  document.querySelectorAll(".menu-btn").forEach(function (b) { b.addEventListener("click", function () { setMenu(true); }); });
  document.querySelectorAll(".menu-close").forEach(function (b) { b.addEventListener("click", function () { setMenu(false); }); });
  if (menu) menu.querySelectorAll("a").forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") setMenu(false); });

  /* ---------- Toast ---------- */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; toastEl.setAttribute("role", "status"); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastEl._t); toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 2600);
  }

  /* ---------- WhatsApp helpers ---------- */
  function waLink(text) { return "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text); }
  function mapsLink(lat, lng) { return "https://www.google.com/maps?q=" + lat.toFixed(6) + "," + lng.toFixed(6); }

  function getLocation(cb, fail) {
    if (!("geolocation" in navigator)) { fail("unsupported"); return; }
    navigator.geolocation.getCurrentPosition(function (p) { cb(p.coords); }, function (err) { fail(err && err.code); },
      { enableHighAccuracy: true, timeout: 12000, maximumAge: 30000 });
  }

  /* "Send my location" buttons: grab GPS, open WhatsApp with a Google Maps pin */
  document.querySelectorAll("[data-share-location]").forEach(function (btn) {
    btn.addEventListener("click", function (e) {
      e.preventDefault();
      toast("Finding your location…");
      getLocation(function (c) {
        var msg = "Hi Rapid Rescue, I need recovery.\n\nMy location: " + mapsLink(c.latitude, c.longitude) +
          " (accurate to about " + Math.round(c.accuracy) + "m)\n\nVehicle: \nWhat's wrong: \nWhere it needs to go: ";
        window.location.href = waLink(msg);
      }, function () {
        toast("Couldn't get your location — opening WhatsApp. Tap 📎 → Location to send your pin.");
        setTimeout(function () {
          window.location.href = waLink("Hi Rapid Rescue, I need recovery. I'll send my location pin now.\n\nVehicle: \nWhat's wrong: \nWhere it needs to go: ");
        }, 1200);
      });
    });
  });

  /* Form: fill pickup with current location */
  document.querySelectorAll("[data-fill-location]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var target = document.getElementById(btn.getAttribute("data-fill-location"));
      if (!target) return;
      var old = btn.innerHTML; btn.disabled = true; btn.textContent = "Locating…";
      getLocation(function (c) {
        target.value = "GPS pin: " + mapsLink(c.latitude, c.longitude);
        btn.disabled = false; btn.innerHTML = old; toast("Location added ✓");
      }, function () {
        btn.disabled = false; btn.innerHTML = old;
        toast("Location blocked — please type the road, town or postcode.");
        target.focus();
      });
    });
  });

  /* Form: send the details as a WhatsApp message instead of submitting */
  document.querySelectorAll("form[data-recovery-form]").forEach(function (form) {
    var waBtn = form.querySelector("[data-send-wa]");
    if (!waBtn) return;
    waBtn.addEventListener("click", function () {
      var f = new FormData(form);
      var name = (f.get("name") || "").toString().trim();
      var phone = (f.get("phone") || "").toString().trim();
      var pickup = (f.get("pickup") || "").toString().trim();
      if (!name || !phone || !pickup) { form.reportValidity ? form.reportValidity() : null; toast("Add your name, number and pickup location"); return; }
      var lines = [
        "Hi Rapid Rescue, I'd like a recovery quote.",
        "",
        "Name: " + name,
        "Phone: " + phone,
        "Service: " + (f.get("service") || ""),
        "When: " + (f.get("when") || ""),
        "Pickup: " + pickup,
        "Drop-off: " + (f.get("dropoff") || "—"),
        "Vehicle: " + (f.get("vehicle") || "—"),
        "Rolls / steers / brakes: " + (f.get("rolls") || "—"),
        "Notes: " + (f.get("notes") || "—")
      ];
      window.location.href = waLink(lines.join("\n"));
    });
  });

  /* ---------- Reveal on scroll ---------- */
  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); } });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add("in"); }); }

  /* ---------- Footer year ---------- */
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
