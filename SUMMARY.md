# Оглавление

[Введение](00-README.md)

- [1. Токены, эмбеддинги и трансформер на пальцах](01-tokens-embeddings-transformer.md)
- [2. Prefill и decode: почему генерация упирается в память](02-prefill-decode-roofline.md)
- [3. Иерархия памяти: VRAM, PCIe, ОЗУ, диск и mmap](03-memory-hierarchy-mmap.md)
- [4. Квантование весов: GGUF, k-quants, imatrix](04-quantization-gguf.md)
- [5. MoE: эксперты, роутинг и выгрузка в ОЗУ](05-moe.md)
- [6. KV-кэш, контекстное окно и позиционные кодировки](06-kv-cache-context.md)
- [7. Кэш промпта и агентские нагрузки](07-prompt-cache.md)
- [8. Батчинг, слоты и PagedAttention](08-batching-vllm.md)
- [9. Спекулятивное декодирование: черновик, MTP, acceptance rate](09-speculative-decoding.md)
- [10. Сэмплинг, температура и бюджет рассуждений](10-sampling-reasoning.md)
- [11. Вызов инструментов: шаблоны чата, грамматики, JSON Schema](11-tool-calling.md)
- [12. Методика бенчмарка и тюнинга](12-benchmark-methodology.md)
- [Движки инференса: llama.cpp](engines-llama-cpp.md)
- [Движки инференса: vLLM](engines-vllm.md)
- [Движки инференса: SGLang](engines-sglang.md)
- [Движки инференса: сравнение и выбор](engines-comparison.md)
- [13. Выбор модели под железо](13-model-selection.md)
- [Как выбрать железо для локального инференса](hardware-choice.md)
- [14. Речь и OCR локально](14-speech-ocr.md)
- [Новые эксперименты: большие модели на маленьком железе](big-models-small-hardware.md)
- [15. Куда расти](15-where-to-go-next.md)
- [16. Глоссарий](16-glossary.md)
- [Приложение. Частые заблуждения](fallacies.md)
- [Приложение. Порядок анализа: шпаргалка](cheatsheet.md)

---

[Источники](sources.md)
