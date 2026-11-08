# Ревью: четыре главы «Движки инференса»

- Предмет: `engines-llama-cpp.md`, `engines-vllm.md`, `engines-sglang.md`, `engines-comparison.md` + правки `08-batching-vllm.md`, `sources.md`, `16-glossary.md`, `SUMMARY.md`.
- Ветка `engines-chapter`, коммит `7f551b9`. Объём: 4002 + 3434 + 3577 + 2433 = **13 446 слов**.
- Дата проверки: 8 ноября 2026. Сверено с: релизами ggml-org/llama.cpp v0.9.0 (04.11.2026), vllm-project/vllm v0.33.0 (тег 01.11.2026), sgl-project/sglang v0.5.23 (02.11.2026); `tools/server/README.md` llama.cpp (master); docs.vllm.ai (APC, optimization, tool calling); docs.sglang.io (server arguments, paged experts, speculative decoding).
- Сборку `mdbook build` выполнить не удалось: `mdbook` отсутствует в окружении. Рендер оценён по `book.toml` и разметке.

**Вердикт: доработать (2 фактические правки + 3 ослабления формулировок), затем принять.** Блокеров архитектуры, публичности и структуры нет.

---

## 1. Блокеры (неверные утверждения о командах/поведении)

### Б1. SGLang: `--paged-experts-num-resident` НЕ обязателен

`engines-sglang.md:181`:

> В v0.5.23 параметр `--paged-experts-num-resident` обязателен: это число экспертов на слой, которые держатся на GPU. … в более новых сборках допускается `auto`.

Документация «Paged Experts» говорит обратное: флаг принимает `K|auto`, **`auto` — значение по умолчанию**, K подбирается автоматически после загрузки модели, в лог печатается выбранное K и подсказка для фиксации (`To pin: --paged-experts-num-resident 63`).

> `--paged-experts-num-resident K|auto` … `auto` (the default) … With `--paged-experts-num-resident auto`, or the flag omitted, K is chosen once every weight is loaded.

Исправить на: по умолчанию `auto`; явное значение — опциональная фиксация. Пример в §3.2 (`--paged-experts-num-resident 16`) корректен как пример, его не трогать.

### Б2. vLLM: методы спекуляции `dflash`, `dspark` не подтверждены

`engines-vllm.md:205–212` (таблица) и `engines-comparison.md:24` приписывают vLLM методы `dflash`, `dspark` (рядом с `draft_model`, `eagle3`, `mtp`, `ngram`, `suffix`).

По документации vLLM/SGLang на ноябрь 2026: DFlash/DFlash2/DSpark — это семейство **SGLang** (`--speculative-algorithm DFLASH`, доки SGLang; в полном списке алгоритмов SGLang: `UNO, DFLASH, EAGLE, EAGLE3, STANDALONE, NGRAM, NEXTN`). Для vLLM подтверждённых источников по `dflash`/`dspark` в `--speculative-config` я не нашёл. `suffix` и `ngram` для vLLM правдоподобны, но тоже без прямой сверки в этой проверке.

Исправить: либо дать источник на поддержку DFlash/DSpark в vLLM v0.33.0, либо убрать их из vLLM-таблицы (оставить в SGLang, где они подтверждены).

### Б3. vLLM: тулчейн «PyTorch 2.14, CUDA 13.0, ROCm 10.0» — без источника

`engines-vllm.md:9`:

> Версия на 8 ноября 2026 — **v0.33.0** (2 ноября 2026), PyTorch 2.14, CUDA 13.0, ROCm 10.0.

Страница релиза v0.33.0 содержит только тег (`4ba787e`, tagged 01 Nov — см. ниже про дату) без release notes про тулчейн. Для сравнения: у SGLang v0.5.23 тулчейн подтверждён таблицей Docker-образов релиза (CUDA 13, `lmsysorg/sglang:v0.5.23`, ROCm 10 для mi30x/mi35x). Для vLLM либо подтвердить по колёсам/докам установки v0.33.0, либо смягчить до «релизные колёса собраны под CUDA 13 / ROCm 10 (проверьте страницу установки)».

Дополнительно: дата тега — **1 ноября**, не 2-е (`khluu tagged this 01 Nov`). Мелочь, но в трёх главах даты заявлены с точностью до дня — исправить на 1 ноября или «начало ноября».

---

## 2. Важно (вводящие в заблуждение формулировки, поведение по умолчанию)

### В1. llama.cpp: пример `--load-mode none` с неверным объяснением

`engines-llama-cpp.md:410–424` (пример, строка 424):

> `--load-mode none` — не полагаться на mmap для весов, которые считаются на CPU (глава 3).

По `tools/server/README.md`: `--load-mode` — `auto` (mmap, unless a device does not support it), `none` = **no special loading mode**, далее `mmap`, `mlock`, `mmap+mlock`, `dio`. `none` — это «без специального режима», а не «отключить mmap для CPU-весов». Формулировка приписывает флагу несуществующую семантику. Предлагаю: убрать `--load-mode none` из примера (дефолт `auto` и так корректен) или заменить объяснение дословным из README.

### В2. llama.cpp: `/v1/rerank` и `/v1/embeddings` требуют оговорок

`engines-llama-cpp.md:318–327` (таблица маршрутов) перечисляет `/v1/embeddings`, `/v1/rerank`, `/rerank` без условий. По README сервера:

- `--rerank, --reranking`: «enable reranking endpoint on server (**default: disabled**)» — без флага маршрут не работает;
- `--embedding, --embeddings`: «restrict to only support embedding use case; use only with dedicated embedding models».

Читатель, скопировавший минимальный запуск из §7, получит 404 на `/v1/rerank`. Добавить одну строку-оговорку под таблицей.

### В3. SGLang: `--quantization awq` vs «определяется автоматически»

`engines-sglang.md:109–111` показывает `--quantization awq # если чекпойнт уже AWQ`, а `engines-sglang.md:437` (пример §9.2) правильно замечает, что «метод уже записан в конфиге чекпойнта и определяется автоматически». Эти два места противоречат друг другу: для предквантованного чекпойнта флаг не нужен (и в главе про vLLM, `engines-vllm.md:400`, это сказано явно: «Если в `config.json` уже указан AWQ, `--quantization awq` можно опустить»). Унифицировать: в §2 SGLang поправить комментарий на «для готового AWQ флаг обычно не нужен».

### В4. Дубли источника в `sources.md`

Новый блок «Движки инференса» добавляет `vLLM, «Tool Calling» … Зачем: --tool-call-parser, strict schema`, а в файле уже есть старый `vLLM, «Tool Calling» … Зачем: strict schema и tool_choice`. Два entries на один URL. Объединить в один.

---

## 3. Мелочь

1. **Глоссарий**: новые термины ссылаются как «(Гл. „Движки инференса“)», остальные — «(Гл. 8)». Единообразия ради лучше «(Гл. „Движки инференса“, 4 гл.)» или оставить как есть — на усмотрение автора, сборку не ломает.
2. **`llama-bench -lm none`** (`engines-llama-cpp.md:370`): флаг `-lm` в README сервера не встречается (это флаг bench-утилиты, не сервера). Не проверен; предложить сверить с `--help` `llama-bench` той же сборки.
3. **Имена метрик Prometheus** (`llamacpp:*` в §8 llama, `vllm:*`, `sglang:*`) выборочно не сверены с живым `/metrics` (проверены только семейства: `vllm:num_requests_waiting`, `prefix_cache_*` упоминаются в доках; `sglang:cache_hit_rate`/`token_usage` правдоподобны). Рекомендую автору один прогон `curl /metrics` по каждому движку перед финалом — это 15 минут и закрывает класс ошибок «опечатка в имени метрики».
4. **`guided_*` «удалены в v0.12.0»** (`engines-vllm.md:262`): версия удаления не подтверждена в этой проверке (deprecated — да, `lm-format-enforcer` объявлен устаревшим — правдоподобно). Либо подтвердить, либо «удалены в недавних версиях, используйте `structured_outputs`».
5. **`--api-key` vLLM «не защищает часть служебных endpoints»** (`engines-vllm.md:314`): согласуется с известным поведением, прямой цитаты из доков в проверке нет. Оставить, но желательно ссылка на issue/доки.
6. **EAGLE-3 конвертация `--target-model-dir`** (`engines-llama-cpp.md:255`): правдоподобно, не сверено с `docs/speculative.md`. См. п.3.
7. Самая широкая таблица (`engines-comparison.md:13–31`, 4 колонки × 17 строк) на мобильных уйдёт в горизонтальный скролл — приемлемо для mdBook, разбивать не обязательно.

---

## 4. Таблица верификации (34 утверждения)

Легенда: ✅ верно · ⚠️ не подтверждено (требует источника/проверки) · ❌ неверно.

| # | Утверждение (глава:строка) | Источник | Итог |
|---|---|---|---|
| 1 | llama.cpp v0.9.0 от 04.11.2026, ggml 0.29.0 | Релиз v0.9.0 GitHub: «released this 04 Nov», «ggml is updated to v0.29.0» | ✅ |
| 2 | Вопрос автора: «версионируется ли как v0.9.0» | Тот же релиз: тег `v0.9.0`, `bump version to 0.9.0 (#31646)` | ✅ да, v0.9.0 реален |
| 3 | FP8 E4M3 добавлен в v0.9.0; NVFP4 для LFM3; NCCL multi-node TP | Релиз: «OCP FP8 E4M3 quantization support», «enable NVFP4 LFM3 ggufs», «Add nccl support for multi-node tensor parallelism (#28967)» | ✅ |
| 4 | Unified KV + `flash_attn_ext_rows` в v0.9.0 | Релиз: «a new `flash_attn_ext_rows` op that makes the unified KV cache efficient» | ✅ |
| 5 | Порт llama-server по умолчанию `127.0.0.1:9931` (гл. llama:339) | README: «default: 127.0.0.1», «port to listen (default: 9931)» | ✅ |
| 6 | `-b` default 2048, `-ub` default 512 (гл. llama:199) | README: «batch-size (default: 2048)», «ubatch-size (default: 512)» | ✅ |
| 7 | `--fit` default `on` (гл. llama:114) | README: «whether to adjust unset arguments … (default: 'on')» | ✅ |
| 8 | KV-типы `f32…q5_1`, default `f16` (гл. llama:82) | README: `-ctk/-ctv`, allowed values, «(default: f16)» | ✅ |
| 9 | `--cache-ram` default 8192 (гл. llama:211) | README: «set the maximum cache size in MiB (default: 8192…)» | ✅ |
| 10 | `--kv-unified` default enabled при auto-слотах; `--kv-unified-per-slot` default unset (гл. llama:190) | README: «(default: enabled if number of slots is auto)», «(default: unset…)» | ✅ |
| 11 | `--cache-prompt` default enabled; `--cache-reuse` default 0 (гл. llama:209–214) | README: «(default: enabled)», «(default: 0)» | ✅ |
| 12 | `--jinja` default enabled (гл. llama:295–296, 336) | README: «whether to use jinja … (default: enabled)» | ✅ |
| 13 | spec-типы `draft-simple/eagle3/mtp/dflash/dspark/ngram-*` (гл. llama:236–244) | README: `--spec-type … draft-simple,draft-eagle3,draft-mtp,draft-dflash,draft-dspark,ngram-simple,ngram-map-k,ngram-map-k4v,ngram-mod,ngram-cache` | ✅ |
| 14 | `--spec-draft-n-max` default 3; `--spec-draft-p-min` default 0.00 (гл. llama:252) | README: «(default: 3)», «(default: 0.00)» | ✅ |
| 15 | `-ngl`/`-sm`/`-ts`/`-ot`/`-ncmoe`/`-cmoe`/`-ncffn`/`--moe-cache-mib` существуют (гл. llama §3) | README: все флаги присутствуют с теми же именами | ✅ |
| 16 | Установщик `curl -LsSf https://llama.app/install.sh \| sh`, единый CLI `llama serve` (гл. llama:42, 377–381) | llama.app/docs/installation; README llama.cpp quickstart (`llama cli`, `llama serve`) | ✅ |
| 17 | Docker-теги `ghcr.io/ggml-org/llama.cpp:server[-cuda]` (гл. llama:386) | README Docker: `ghcr.io/ggml-org/llama.cpp:server`, `:server-cuda` | ✅ |
| 18 | Q4_K_M ≈ 0,60 Б/вес (гл. llama:58) vs гл.4 «≈4,8 бита» | 0,60×8 = 4,8 бит — сходится; `04-quantization-gguf.md:6–7` | ✅ |
| 19 | MoE 35B-A3B Q4_K_M ≈ 21 ГБ (гл. llama:143, 402) | 35e9 × 0,6 Б ≈ 21 ГБ — сходится | ✅ |
| 20 | vLLM v0.33.0, тег 01.11.2026 (гл. vllm:9 «2 ноября») | Релиз: `4ba787e`, «tagged this 01 Nov» — дата съехала на день | ❌ мелочь: исправить на 1 ноября |
| 21 | vLLM тулчейн PyTorch 2.14 / CUDA 13.0 / ROCm 10.0 (гл. vllm:9) | На странице релиза нет notes; независимого подтверждения нет | ⚠️ подтвердить или смягчить (см. Б3) |
| 22 | `--enable-prefix-caching` default True; `--block-size` 16; хеш-алго `sha256/sha256_cbor/xxhash/xxhash_cbor` (гл. vllm:137, 154–159) | `vllm/config/cache.py`: `enable_prefix_caching: bool = True`, `DEFAULT_BLOCK_SIZE = 16`, `PrefixCachingHashAlgo = Literal[…]`; engine_args docs | ✅ |
| 23 | Chunked prefill включён по умолчанию; decode приоритетнее; RECOMPUTE в V1 (гл. vllm:38–40, 166) | docs «Optimization and Tuning»: «enabled by default whenever possible», «prioritizes decode», «default preemption mode is RECOMPUTE» | ✅ |
| 24 | `max_num_batched_tokens` база 2048, рекомендация > 8192 (гл. vllm:140) | Те же доки: «Smaller values (e.g. 2048)… we recommend setting max_num_batched_tokens > 8192» | ✅ |
| 25 | `--kv-cache-dtype-skip-layers sliding_window` (гл. vllm:85–86) | `cache.py`: «Accepts layer indices … or attention type names (e.g. 'sliding_window')» | ✅ |
| 26 | KV-математика 70B FP8: 160 КиБ/ток, 32k ≈ 5 ГиБ, 4×48 ГБ ≈ 24 запроса (гл. vllm:176–190) | 80 слоёв × 8 KV-голов × 128 × 2 Б = 163 840 Б ≈ 160 КиБ; 32768 × 160 КиБ ≈ 5 ГиБ; (192−70)/5 ≈ 24 — арифметика сходится | ✅ |
| 27 | vLLM spec-методы: draft/eagle3/mtp/ngram/suffix/**dflash/dspark** (гл. vllm:205–212) | Подтверждения dflash/dspark для vLLM нет; DFlash — семейство SGLang | ❌/⚠️ убрать или дать источник (см. Б2) |
| 28 | `--enable-auto-tool-choice` + `--tool-call-parser hermes` + `tool_choice auto/required/none` + `--tool-strict-level` (гл. vllm:266–279) | docs «Tool Calling»: флаги, `required (as of vllm>=0.8.3)`, таблица `--tool-strict-level auto/function/parameter` | ✅ |
| 28 | SGLang v0.5.23 от 02.11.2026; Paged Experts; «до 30× быстрее CPU offload» (гл. sglang:9, 183) | Релиз: «released this 02 Nov», «Paged Experts (opt-in)… up to 30x faster than CPU offload (#42557)» — в главе подано как заявка авторов с оговоркой | ✅ |
| 30 | SGLang CUDA 13 / Docker `lmsysorg/sglang:v0.5.23` / ROCm 10 (гл. sglang:9, 407) | Релиз, таблица Docker: NVIDIA (CUDA 13) `lmsysorg/sglang:v0.5.23`, `v0.5.23-rocm10-mi35x/mi30x` | ✅ |
| 31 | `--paged-experts-num-resident` обязателен (гл. sglang:181) | Доки: `K\|auto`, `auto (the default)`; «or the flag omitted» | ❌ неверно (см. Б1) |
| 32 | Ограничения Paged Experts: 1 GPU, без spec, без TP/EP/PP/DP (гл. sglang:164–169) | Доки: «Single GPU: tensor, expert, pipeline and data parallelism… rejected», «Speculative decoding is rejected» | ✅ |
| 33 | `--page-size` default 1; `--schedule-policy` default `fcfs`; eviction `lru/lfu/slru/priority` (гл. sglang:66, 199, 207) | Server Arguments: page-size `1`, schedule-policy `fcfs`, radix-eviction-policy `lru`, options `lru/lfu/slru/priority` | ✅ |
| 34 | Spec SGLang: EAGLE3/NEXTN(=EAGLE)/STANDALONE/NGRAM/UNO/DFLASH (гл. sglang:263–271) | Доки Speculative Decoding: методы + «`NEXTN` (alias of `EAGLE`)»; MTP-пример через `EAGLE` | ✅ |
| 35 | `--tool-call-parser auto`, `--reasoning-parser`, `--chat-template`, `--enable-metrics`, `--enable-cache-report`, `--enable-hierarchical-cache` существуют (гл. sglang) | Server Arguments: все флаги присутствуют (таблица выше) | ✅ |
| 36 | Арифметика Radix-выигрыша 50×(16+3,75)→988с vs 50×(0,27+3,75)→201с (гл. sglang:239–256) | 24000/1500=16; 150/40=3,75; 987,5≈988; 400/1500≈0,27; 201с; экономия ≈787с — сходится | ✅ |

Дополнительно (без номеров): `--cpu-offload-gb`, `--enable-expert-parallel`, `--data-parallel-size` у vLLM подтверждены доками; env `SGLANG_USE_MLX=1` и install-команда `uv pip install --prerelease=allow sglang` согласуются с релизом/доками.

---

## 5. Согласованность с книгой

- **Гл. 4**: Q4_K_M ~4,8 бит ↔ 0,60 Б/вес в таблице llama (§2) — сходится. i-quants/imatrix отсылают к §4.6 — корректно.
- **Гл. 6**: формула KV и GQA/MLA — движковые главы формулу не дублируют, только ссылаются («Формула размера KV и влияние GQA/MLA — в главе 6») — правильно, дублирования теории нет.
- **Гл. 7**: стабильный префикс, LCP, агентские нагрузки — примеры «время в начало промпта» в трёх главах дословно опираются на правило гл.7 — противоречий нет.
- **Гл. 8**: ссылки на §8.2 (`-b`/`-ub` — раздел существует), §8.4 (Литтл — существует), §8.5 (PagedAttention — существует), §8.6 (TP/PP — раздел «vLLM против llama.cpp» + «Параллелизм и разделение фаз», релевантно). Формула `b*` и `N = λT` используются корректно.
- **Гл. 9**: `E[N]`, acceptance rate, «черновик должен стоить дешевле» — движковые главы ссылаются, не перевыводят — правильно.
- **Гл. 11**: шаблон+парсер как причина ломающихся tool calls — все три главы повторяют этот диагноз единообразно — противоречий нет.
- **Гл. 12**: «один параметр за раз, 3–5 повторов, медиана» — повторено в трёх тюнинг-разделах дословно — консистентно.
- **hardware-choice / fallacies**: «vLLM Linux-first/WSL», «llama.cpp — layer split, vLLM — tensor parallel», «`-c` включает сгенерированные токены» — противоречий с новыми главами нет.
- Перекрёстные ссылки: правка `08-batching-vllm.md` (+2 строки) ведёт в четыре новые главы; глоссарий добавляет 13 терминов, дублирования определений с гл. 5/8 нет (RadixAttention, HiCache, Paged Experts, Unified KV — новые).

---

## 6. Публичность

Чисто. Поиск по `home/`, `/tmp/`, `opencode`, именам/никам в четырёх главах и правках — совпадений нет. Пути в примерах обобщённые (`./models/…`, `~/.cache/huggingface`, `$PWD`, `0.0.0.0`); внешние URL — только официальные (github.com/ggml-org, docs.vllm.ai, docs.sglang.io, llama.app, arXiv). Персональных данных, внутренних путей, привязки к конкретному проекту нет.

---

## 7. Читаемость и рендер

- Объём 13,4 тыс. слов на 4 главы — не перегружен: структура четырёх глав зеркальная (§1–9, ключевые идеи, проверь себя, источники), сравнение — 2,4 тыс. слов без воды. Сжимать принудительно нечего; кандидат на сокращение при желании — таблицы квантов (§2 в каждой главе частично повторяют гл.4), но как «выбор движка» они уместны.
- `mdbook build` проверить не удалось (нет `mdbook` в окружении) — **автору прогнать локально**. По разметке рисков мало: admonitions (`> [!NOTE/WARNING/TIP]`) включены в `book.toml` (`admonitions = true`); Mermaid-блоки оформлены как в остальных главах (`theme/mermaid-init.js` подключён); таблицы широкие, но в пределах обычной практики книги.
- `SUMMARY.md`: главы вставлены ненумерованными между гл.12 и гл.13 — нумерация старых глав не поехала, оглавление корректно. Отчёт ревью в `reviews/` в SUMMARY не включается (согласно заданию) — при `create-missing = false` несопровождаемый файл сборку не ломает, т.к. mdBook строит только файлы из SUMMARY.

---

## 8. Что делать автору (чек-лист)

1. [ ] SGLang §3.2: `auto` — дефолт `--paged-experts-num-resident`, не «обязателен» (Б1).
2. [ ] vLLM §5: убрать `dflash/dspark` или дать источник под v0.33.0 (Б2).
3. [ ] vLLM §«За 30 секунд»: подтвердить тулчейн или смягчить + дата 1 ноября (Б3).
4. [ ] llama §9.2: убрать/переформулировать `--load-mode none` (В1).
5. [ ] llama §7: оговорка про `--rerank`/`--embedding` под таблицей маршрутов (В2).
6. [ ] SGLang §2 vs §9.2: унифицировать `--quantization awq` для готового чекпойнта (В3).
7. [ ] `sources.md`: объединить дубль `vLLM Tool Calling` (В4).
8. [ ] По желанию: `curl /metrics` по трём движкам, сверка имён метрик и `llama-bench -lm`.
9. [ ] Прогнать `mdbook build` локально.

---

*Проверено выборочно, 36 пунктов таблицы + сквозная сверка перекрёстных ссылок, арифметики примеров и публичности. Независимых замеров производительности в главах нет — и главы честно фиксируют это в §«Что здесь не проверено», что считаю правильным решением.*
