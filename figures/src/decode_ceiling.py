"""Теоретический потолок скорости декода против пропускной способности памяти.

Формула главы 2: ток/с ≈ пропускная способность ÷ байт весов, читаемых на токен.
Размеры — конвенция книги для Q4_K_M (0,60 байта на параметр): 7B ≈ 4,2 ГБ,
13B ≈ 7,8 ГБ, 70B ≈ 42 ГБ; MoE с 3B активных ≈ 1,8 ГБ на токен (гл. 5).
Полоса — «реалистично 50–75 % потолка» из главы 2.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # запуск через python -I
from _style import setup, save, SERIES, INK
import matplotlib.pyplot as plt

setup()

MODELS = [  # (подпись, ГБ на токен)
    ("MoE, 3B активных (1,8 ГБ)", 1.8),
    ("7B (4,2 ГБ)", 4.2),
    ("13B (7,8 ГБ)", 7.8),
    ("70B (42 ГБ)", 42.0),
]
bw = np.linspace(40, 1800, 400)
fig, ax = plt.subplots()
for (label, gb), color in zip(MODELS, SERIES):
    top = bw / gb
    ax.plot(bw, top, color=color, label=label)
    ax.fill_between(bw, 0.5 * top, 0.75 * top, color=color, alpha=0.12, lw=0)

# Ориентиры по пропускной способности — диапазоны из таблицы главы 3
for x, text in [(80, "ОЗУ DDR\n40–100"), (500, "VRAM\nсредняя карта"),
                (1000, "VRAM\n~1 ТБ/с")]:
    ax.axvline(x, color=INK, ls=":", lw=1.1)
    ax.text(x + 12, 2.2, text, fontsize=8.5, color=INK, va="bottom")

ax.set_yscale("log")
ax.set_xlim(0, 1800)
ax.set_ylim(1, 1500)
ax.set_xlabel("Пропускная способность памяти, ГБ/с")
ax.set_ylabel("Потолок декода, ток/с (лог. шкала)")
ax.set_title("Потолок декода = пропускная способность ÷ байт на токен, Q4_K_M",
             fontsize=11.5, loc="left")
ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1.0), fontsize=9)
save(fig, "decode_ceiling.svg",
     "Расчёт по формуле гл. 2. Линия — потолок, полоса — 50–75 % от него.")
