"""Пересобрать все графики книги.

Запуск из любого каталога:
    MPLBACKEND=Agg python3 -I docs/learning/book/figures/src/build_all.py
"""
import glob
import os
import runpy

HERE = os.path.dirname(os.path.abspath(__file__))
for path in sorted(glob.glob(os.path.join(HERE, "*.py"))):
    name = os.path.basename(path)
    if name.startswith("_") or name == "build_all.py":
        continue
    runpy.run_path(path, run_name="__main__")
