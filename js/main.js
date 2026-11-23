/* ==========================================================================
   Mega Sale Lương Về — Tương tác trang
   1. Menu điều hướng mobile (mở/đóng, tự đóng khi chọn mục)
   2. Đồng bộ URL hai cổng đăng ký từ cấu hình tập trung (js/config.js)
   ========================================================================== */

(function () {
  "use strict";

  /* ---------- 1. Menu mobile ---------- */
  var navToggle = document.querySelector(".nav-toggle");
  var primaryNav = document.getElementById("primary-nav");

  if (navToggle && primaryNav) {
    navToggle.addEventListener("click", function () {
      var isOpen = primaryNav.classList.toggle("open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    // Đóng menu khi người dùng chọn một mục điều hướng
    primaryNav.querySelectorAll(".nav-link").forEach(function (link) {
      link.addEventListener("click", function () {
        primaryNav.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });

    // Đóng menu khi nhấn Esc
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && primaryNav.classList.contains("open")) {
        primaryNav.classList.remove("open");
        navToggle.setAttribute("aria-expanded", "false");
        navToggle.focus();
      }
    });
  }

  /* ---------- 2. Đồng bộ URL đăng ký từ config.js ---------- */
  var config = window.CAMPAIGN_CONFIG;
  if (config && config.REGISTRATION_URLS) {
    var gateMap = [
      { id: "gate-1", key: "GATE_1" },
      { id: "gate-2", key: "GATE_2" },
    ];

    gateMap.forEach(function (item) {
      var button = document.getElementById(item.id);
      var url = config.REGISTRATION_URLS[item.key];
      if (button && url) {
        button.setAttribute("href", url);
        // Luôn mở tab mới và chặn cửa sổ mới truy cập lại tab gốc
        button.setAttribute("target", "_blank");
        button.setAttribute("rel", "noopener noreferrer");
      }
    });
  }
})();
