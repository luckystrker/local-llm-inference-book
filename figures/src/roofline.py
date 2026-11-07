"""Roofline: достижимая производительность против арифметической интенсивности.

Формула главы 2: достижимые FLOP/s = min(пик FLOP/s, пропускная способность × I).
Параметры устройств — условные примеры из главы 2 (карты 50 TFLOP/s при 1 ТБ/с
и 20 TFLOP/s при 500 ГБ/с) и условный настольный CPU; это не паспортные данные
конкретных моделей.
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # запуск через python -I
from _style import setup, save, SERIES, INK
import matplotlib.pyplot as plt

setup()

DEVICES = [  # (подпись, пик FLOP/s, пропускная способность байт/с)
    ("GPU A: 50 TFLOP/s, 1 ТБ/с", 50e12, 1000e9),
    ("GPU B: 20 TFLOP/s, 500 ГБ/с", 20e12, 500e9),
    ("CPU: 1,5 TFLOP/s, 80 ГБ/с", 1.5e12, 80e9),
]

I = np.logspace(-1, 4.2, 400)
fig, ax = plt.subplots()
for (label, peak, bw), color in zip(DEVICES, SERIES):
    perf = np.minimum(peak, bw * I) / 1e12
    ax.plot(I, perf, color=color, label=label)
    istar = peak / bw
    ax.plot([istar], [peak / 1e12], "o", color=color, ms=6)
    ax.annotate(f"I* ≈ {istar:.0f}", (istar, peak / 1e12), textcoords="offset points",
                xytext=(6, 6), fontsize=9, color=INK)

# Рабочие точки нагрузок: I = 2B/b (глава 2)
marks = [
    (2 / 2.0, "decode\nFP16\nI ≈ 1", "right"),
    (2 / 0.60, "decode\nQ4_K_M\nI ≈ 3,3", "left"),
    (2 * 2048 / 0.60, "prefill\nB = 2048,\nQ4_K_M\nI ≈ 6800", "right"),
]
for x, text, side in marks:
    ax.axvline(x, color=INK, ls=":", lw=1.2)
    ax.text(x * (0.9 if side == "right" else 1.1), 0.012, text, fontsize=9,
            color=INK, va="bottom", ha=side)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.1, 16000)
ax.set_ylim(0.008, 120)
ax.set_xlabel("Арифметическая интенсивность I, FLOP на байт (лог. шкала)")
ax.set_ylabel("Достижимая производительность, TFLOP/s (лог.)")
ax.set_title("Roofline: слева от I* упираемся в память, справа — в вычисления",
             fontsize=11.5, loc="left")
ax.legend(loc="upper left", fontsize=9)
save(fig, "roofline.svg",
     "Расчёт: min(пик, пропускная способность × I), гл. 2. Параметры устройств условные.")
