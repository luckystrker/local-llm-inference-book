"""Общий стиль графиков книги.

Прозрачный фон и нейтрально-серые подписи читаются и в светлой, и в тёмной
теме GitHub. Цвета серий — средние по светлоте шаги категориальной палитры,
различимые на обоих фонах.
"""
import os
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

INK = "#8b8b8b"        # текст и оси: середина между светлым и тёмным фоном
GRID = "#8b8b8b"
SERIES = ["#3987e5", "#d95926", "#199e70", "#9085e9", "#c98500", "#d55181"]

OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def setup():
    plt.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "text.color": INK,
        "axes.labelcolor": INK,
        "axes.edgecolor": INK,
        "axes.titlecolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.alpha": 0.25,
        "grid.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "legend.frameon": False,
        "lines.linewidth": 2,
        "svg.fonttype": "path",
        "svg.hashsalt": "book",
        "figure.figsize": (8, 4.8),
        "figure.dpi": 100,
    })


def save(fig, name, note="Расчёт по формулам книги, не замер."):
    fig.text(0.995, -0.04, note, ha="right", va="top", fontsize=8.5,
             color=INK, alpha=0.9)
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight",
                metadata={"Date": None, "Creator": None})
    preview = os.environ.get("BOOK_PREVIEW_DIR")
    if preview:  # PNG на светлом и тёмном фоне GitHub — только для проверки глазами
        base = os.path.join(preview, name[:-4])
        for suffix, bg in (("light", "#ffffff"), ("dark", "#0d1117")):
            fig.savefig(f"{base}-{suffix}.png", format="png", facecolor=bg,
                        bbox_inches="tight", dpi=80)
    plt.close(fig)
    print("wrote", path)
