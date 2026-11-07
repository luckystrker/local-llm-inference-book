// Рендер блоков ```mermaid в mdBook: mdBook выдаёт их как <code class="language-mermaid">.
// Схемы показываем в натуральную ширину и даём прокрутку внутри блока: иначе
// на телефоне mermaid сжимает широкую схему в 4–5 раз и текст не читается.
(function () {
  var blocks = document.querySelectorAll("pre > code.language-mermaid");
  if (!blocks.length) return;

  var narrow = window.matchMedia("(max-width: 760px)").matches;

  function isDark() {
    return /(navy|coal|ayu)/.test(document.documentElement.className);
  }

  function init() {
    window.mermaid.initialize({
      startOnLoad: false,
      theme: isDark() ? "dark" : "default",
      // Диаграммы Ганта вписываются в ширину колонки: на узком экране
      // уменьшаем отступы и шрифт, чтобы подписи не наезжали друг на друга.
      gantt: {
        useMaxWidth: true,
        topAxis: false,
        leftPadding: narrow ? 56 : 75,
        barHeight: narrow ? 22 : 26,
        barGap: 4,
        fontSize: narrow ? 12 : 14,
        sectionFontSize: narrow ? 12 : 14,
      },
      flowchart: { useMaxWidth: true },
      sequence: { useMaxWidth: true },
    });

    blocks.forEach(function (code) {
      var div = document.createElement("div");
      div.className = "mermaid";
      div.textContent = code.textContent;
      code.parentElement.replaceWith(div);
    });

    window.mermaid.run().then(adapt, adapt);
  }

  function adapt() {
    document.querySelectorAll(".mermaid").forEach(function (div) {
      var svg = div.querySelector("svg");
      if (!svg || !svg.viewBox || !svg.viewBox.baseVal) return;

      var width = Math.ceil(svg.viewBox.baseVal.width);
      if (!width) return;
      div.style.setProperty("--mermaid-w", width + "px");

      // Подсказка нужна только там, где схема шире колонки.
      requestAnimationFrame(function () {
        if (div.scrollWidth <= div.clientWidth + 2) return;
        var hint = document.createElement("p");
        hint.className = "mermaid-hint";
        hint.textContent = "Схему можно прокрутить вбок →";
        div.insertAdjacentElement("afterend", hint);
      });
    });
  }

  var s = document.createElement("script");
  s.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
  s.onload = init;
  document.head.appendChild(s);
})();
