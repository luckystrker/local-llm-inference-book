"""Размер весов модели против бит на параметр для форматов квантования.

Формула главы 4: размер ≈ параметры × бит на вес / 8. Биты на вес — конвенция
таблицы §4.4 (средние с учётом масштабов; точный размер зависит от рецепта).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # запуск через python -I
from _style import setup, save, SERIES, INK
import matplotlib.pyplot as plt

setup()

FORMATS = [("IQ2_XXS", 2.1), ("IQ3_XXS", 3.1), ("IQ4_XS", 4.45), ("Q4_K_M", 4.8),
           ("Q5_K_M", 5.7), ("Q6_K", 6.6), ("Q8_0", 8.5), ("FP16", 16.0)]
MODELS = [("7B", 7), ("13B", 13), ("35B", 35), ("70B", 70)]

fig, ax = plt.subplots(figsize=(8.4, 5))
bits = np.array([b for _, b in FORMATS])
for (label, params), color in zip(MODELS, SERIES):
    size = params * bits / 8
    ax.plot(bits, size, "-o", color=color, ms=4.5, label=label)

for name, b in FORMATS:
    ax.axvline(b, color=INK, lw=0.6, alpha=0.35)
    ax.text(b, 1.02, name, transform=ax.get_xaxis_transform(), rotation=60,
            ha="left", va="bottom", fontsize=8.5, color=INK)

for vram in (12, 16, 24):
    ax.axhline(vram, color=INK, ls="--", lw=1)
    ax.text(17.2, vram, f"карта {vram} ГБ", va="center", fontsize=8.5, color=INK)

ax.set_xscale("log", base=2)
ax.set_xticks([2, 3, 4, 5, 6, 8, 12, 16])
ax.set_xticklabels(["2", "3", "4", "5", "6", "8", "12", "16"])
ax.set_yscale("log")
ax.set_yticks([2, 5, 10, 20, 50, 100])
ax.set_yticklabels(["2", "5", "10", "20", "50", "100"])
ax.set_xlim(1.9, 22)
ax.set_ylim(1.5, 170)
ax.set_xlabel("Бит на вес (лог. шкала)")
ax.set_ylabel("Размер весов, ГБ (лог. шкала)")
ax.legend(loc="upper left", fontsize=9)
ax.set_title("Размер весов = параметры × бит на вес ÷ 8", fontsize=11.5,
             loc="left", pad=58)
save(fig, "model_size_bits.svg",
     "Расчёт по таблице §4.4. Без KV-кэша и буферов; для планирования +10–20 %.")
