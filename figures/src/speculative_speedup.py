"""Ускорение спекулятивного декодирования от acceptance rate и длины черновика γ.

Формула Leviathan, Kalman, Matias (2022), arXiv:2211.17192:
    speedup = (1 − α^(γ+1)) / ((1 − α)(γ·d + 1)),
где α — вероятность принять токен черновика, d — стоимость шага черновика
относительно шага целевой модели. Это идеализация: накладные расходы проверки
не учтены, поэтому реальные числа ниже (гл. 9).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # запуск через python -I
from _style import setup, save, SERIES, INK
import matplotlib.pyplot as plt

setup()


def speedup(alpha, gamma, d):
    return (1 - alpha ** (gamma + 1)) / ((1 - alpha) * (gamma * d + 1))


alpha = np.linspace(0.05, 0.95, 300)
fig, axes = plt.subplots(1, 2, figsize=(10, 4.6), sharey=True)
for ax, d in zip(axes, (0.05, 0.2)):
    for gamma, color in zip((1, 2, 4, 8), SERIES):
        ax.plot(alpha, speedup(alpha, gamma, d), color=color, label=f"γ = {gamma}")
    ax.axhline(1, color=INK, ls=":", lw=1.2)
    ax.text(0.93, 0.93, "ниже 1 — замедление", fontsize=8.5, color=INK,
                ha="right", va="top")
    ax.set_title(f"черновик стоит d = {d:g} шага целевой модели".replace(".", ","),
                 fontsize=10.5, loc="left")
    ax.set_xlabel("Acceptance rate α")
    ax.set_xlim(0.05, 0.95)
    ax.set_xticks([0.1, 0.3, 0.5, 0.7, 0.9])
    ax.set_xticklabels(["0,1", "0,3", "0,5", "0,7", "0,9"])
axes[0].set_ylabel("Ожидаемое ускорение, раз")
axes[0].set_ylim(0.5, 6.5)
axes[0].legend(loc="upper left", fontsize=9)
axes[0].annotate("α = 0,8, γ = 4: 2,8×\n(пример §9.3)", (0.8, speedup(0.8, 4, 0.05)),
                 xytext=(-110, 30), textcoords="offset points", fontsize=8.5, color=INK,
                 arrowprops=dict(arrowstyle="-", color=INK, lw=0.8))
fig.suptitle("Спекулятивное декодирование: идеальное ускорение по Leviathan et al.",
             x=0.01, y=1.03, ha="left", fontsize=11.5, color=INK)
save(fig, "speculative_speedup.svg",
     "Расчёт: (1 − α^(γ+1)) / ((1 − α)(γd + 1)), Leviathan et al., arXiv:2211.17192. "
     "Реальное ускорение ниже.")
