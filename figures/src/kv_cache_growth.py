"""Рост KV-кэша с длиной контекста.

Формула главы 6: KV-байт = 2 × L_full × n_kv_heads × d_head × ctx × байт_на_элемент.
Условная модель класса 8B: 32 слоя, 32 Q-головы, d_head = 128.
  - обычное multi-head внимание: 32 KV-головы;
  - GQA: 8 KV-голов;
  - гибрид: из 32 слоёв только 8 с полным вниманием (остальные линейные), GQA 8.
f16 = 2 байта на элемент, q8_0 = 1,0625 байта (34 байта на блок из 32).
"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # запуск через python -I
from _style import setup, save, SERIES, INK
import matplotlib.pyplot as plt

setup()
GIB = 2**30
D_HEAD = 128
ARCH = [  # (подпись, слоёв с полным вниманием, KV-голов)
    ("обычное внимание (32 KV-головы)", 32, 32),
    ("GQA (8 KV-голов)", 32, 8),
    ("гибрид: 8 из 32 слоёв полные, GQA", 8, 8),
]
DTYPES = [("f16", 2.0, "-"), ("q8_0", 1.0625, "--")]

ctx = np.logspace(np.log2(1024), np.log2(131072), 200, base=2)
fig, ax = plt.subplots(figsize=(8.4, 5))
for (label, layers, kv_heads), color in zip(ARCH, SERIES):
    for dname, nbytes, ls in DTYPES:
        kv = 2 * layers * kv_heads * D_HEAD * ctx * nbytes / GIB
        ax.plot(ctx, kv, ls, color=color, label=f"{label}, {dname}")
    end = 2 * layers * kv_heads * D_HEAD * 131072 * 2.0 / GIB
    ax.annotate(f"{end:.0f} ГиБ", (131072, end), xytext=(6, 0), textcoords="offset points",
                va="center", fontsize=9, color=INK)

weights = 8e9 * 0.6 / GIB  # 8B в Q4_K_M
ax.axhline(weights, color=INK, ls=":", lw=1.2)
ax.text(1100, weights * 1.12, f"для сравнения: веса 8B в Q4_K_M ≈ {weights:.1f} ГиБ",
        fontsize=8.5, color=INK)

ticks = [1024, 4096, 8192, 16384, 32768, 65536, 131072]
ax.set_xscale("log", base=2)
ax.set_xticks(ticks)
ax.set_xticklabels(["1k", "4k", "8k", "16k", "32k", "64k", "128k"])
ax.set_yscale("log")
ax.set_yticks([0.01, 0.1, 1, 10, 64])
ax.set_yticklabels(["0,01", "0,1", "1", "10", "64"])
ax.set_xlim(1024, 131072 * 1.6)
ax.set_xlabel("Длина контекста, токенов (лог. шкала)")
ax.set_ylabel("KV-кэш на один слот, ГиБ (лог. шкала)")
ax.set_title("KV-кэш условной 8B-модели: архитектура внимания и точность кэша",
             fontsize=11.5, loc="left")
ax.legend(loc="lower right", fontsize=8.5)
save(fig, "kv_cache_growth.svg",
     "Расчёт по формуле §6.2: сплошные — f16, пунктир — q8_0. Конфигурация условная.")
