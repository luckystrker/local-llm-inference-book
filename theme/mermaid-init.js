// Рендер блоков ```mermaid в mdBook: mdBook выдаёт их как <code class="language-mermaid">.
(function () {
  var blocks = document.querySelectorAll("pre > code.language-mermaid");
  if (!blocks.length) return;
  var s = document.createElement("script");
  s.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
  s.onload = function () {
    var dark = /(navy|coal|ayu)/.test(document.documentElement.className);
    window.mermaid.initialize({ startOnLoad: false, theme: dark ? "dark" : "default" });
    blocks.forEach(function (code) {
      var div = document.createElement("div");
      div.className = "mermaid";
      div.textContent = code.textContent;
      code.parentElement.replaceWith(div);
    });
    window.mermaid.run();
  };
  document.head.appendChild(s);
})();
