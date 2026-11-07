"""Карта «объём памяти — пропускная способность — цена» для главы о выборе железа.

Точки — устройства из таблиц главы. По осям логарифмы: объём памяти (ГБ) и
пропускная способность (ГБ/с). Размер маркера — уличная цена в США (ноябрь
2026), цвет — класс устройства. Для универсальных боксов и CPU цена базовой
конфигурации, поэтому сравнение с «голой» видеокартой условное.
"""
import os
import sys

import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # запуск через python -I
from _style import setup, save, INK

setup()

# (подпись, память ГБ, ПСП ГБ/с, цена USD, группа, место подписи, куда стрелка)
DEVICES = [
    ("RTX 5060 Ti 16", 16, 448, 500, "NVIDIA", None, None),
    ("RTX 5070 12", 12, 672, 779, "NVIDIA", None, None),
    ("RTX 5070 Ti 16", 16, 896, 990, "NVIDIA", None, None),
    ("RTX 5080 16", 16, 960, 1290, "NVIDIA", None, None),
    ("5090 32 ГБ\n$5–6,9 тыс.", 32, 1792, 4999, "NVIDIA", (28, 2300), (32, 1792)),
    ("3090/4090 б/у\n$1,6–2,5 тыс.", 24, 936, 1586, "NVIDIA", (8.2, 1220), (24, 970)),
    ("A6000 48 ГБ", 48, 768, 3750, "NVIDIA PRO", None, None),
    ("RTX 6000 Ada 48 ГБ", 48, 960, 5225, "NVIDIA PRO", None, None),
    ("RTX PRO 4000", 24, 672, 3049, "NVIDIA PRO", None, None),
    ("RTX PRO 4500", 32, 896, 5726, "NVIDIA PRO", None, None),
    ("PRO 5000 48 ГБ\n$7,3 тыс.", 48, 1344, 7299, "NVIDIA PRO", (50, 1650), (48, 1344)),
    ("PRO 6000 96 ГБ\n$16 тыс.", 96, 1792, 16000, "NVIDIA PRO", (100, 2320), (96, 1792)),
    ("R9700 32 ГБ\n$1,3 тыс.", 32, 640, 1320, "AMD", (34, 700), (32, 640)),
    ("RX 9070 XT", 16, 640, 760, "AMD", None, None),
    ("B60 24 ГБ\n$0,9 тыс.", 24, 456, 934, "Intel", (28, 395), (24, 456)),
    ("B70 32 ГБ", 32, 608, 1932, "Intel", None, None),
    ("Mac mini M6 16 ГБ", 16, 153, 899, "Apple", None, None),
    ("Mac mini M5 Pro", 24, 307, 1699, "Apple", None, None),
    ("M5 Max 36 ГБ", 36, 460, 2499, "Apple", None, None),
    ("M5 Ultra 96 ГБ\n$5,5 тыс.", 96, 1200, 5499, "Apple", (100, 1400), (96, 1200)),
    ("DGX Spark 128 ГБ\n$7 тыс.", 128, 273, 6950, "Unified x86/ARM", (102, 220), (128, 273)),
    ("Strix Halo 128 ГБ\n$3,4 тыс.", 128, 256, 3449, "Unified x86/ARM", (78, 430), (128, 256)),
    ("DDR5, 2 канала\n$1,5 тыс.", 128, 80, 1500, "CPU", (145, 103), (128, 80)),
    ("CPU, 8 каналов", 256, 410, 12000, "CPU", None, None),
    ("CPU, 12 каналов\n$50 тыс.+", 768, 614, 50000, "CPU", (480, 720), (768, 614)),
]

COLORS = {
    "NVIDIA": "#3987e5",
    "NVIDIA PRO": "#9085e9",
    "AMD": "#d95926",
    "Intel": "#c98500",
    "Apple": "#199e70",
    "Unified x86/ARM": "#d55181",
    "CPU": "#8b8b8b",
}

fig, ax = plt.subplots(figsize=(8.2, 5.6))

for label, mem, bw, price, group, text_xy, target in DEVICES:
    ax.scatter(mem, bw, s=40 + 18 * (price / 500) ** 0.55, color=COLORS[group],
               alpha=0.85, edgecolors="none", zorder=3)
    if text_xy:
        ax.annotate(label, xy=target, xytext=text_xy, textcoords="data",
                    fontsize=7.2, color=INK, zorder=4, linespacing=1.15,
                    ha="left", va="center",
                    arrowprops=dict(arrowstyle="-", lw=0.6, color=INK,
                                    shrinkA=0, shrinkB=3))

# Сетка по характерным объёмам памяти и полосам
for x in (8, 12, 16, 24, 32, 48, 96, 128, 256, 512):
    ax.axvline(x, color=INK, ls=":", lw=0.7, alpha=0.22, zorder=0)
for y in (100, 300, 600, 1200):
    ax.axhline(y, color=INK, ls=":", lw=0.7, alpha=0.22, zorder=0)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(7.5, 1000)
ax.set_ylim(60, 3000)
ax.set_xticks([8, 12, 16, 24, 32, 48, 96, 128, 256, 512, 768])
ax.set_xticklabels(["8", "12", "16", "24", "32", "48", "96", "128", "256", "512", "768"])
ax.set_yticks([80, 150, 300, 600, 1200, 1800])
ax.set_yticklabels(["80", "150", "300", "600", "1200", "1800"])
ax.set_xlabel("Память, доступная весам, ГБ", labelpad=6)
ax.set_ylabel("Пропускная способность памяти, ГБ/с", labelpad=13, fontsize=9.5)
ax.set_title("Память, пропускная способность и цена: ноябрь 2026",
             fontsize=11.5, loc="left", pad=14)

handles = [plt.Line2D([], [], marker="o", ls="", color=c, label=g, markersize=7)
           for g, c in COLORS.items()]
ax.legend(handles=handles, loc="lower left", fontsize=6.3,
          ncol=1, title="Класс; размер — цена", title_fontsize=6.3,
          handletextpad=0.3, borderaxespad=0.8)

save(fig, "hardware_map.svg",
     "Данные: таблицы главы; цена — минимальная уличная в США, ноябрь 2026; цены CPU — оценка. "
     "Размер маркера — цена, поэтому сравнение «голых» карт и готовых боксов условное.")
