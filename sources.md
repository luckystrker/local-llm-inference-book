# Источники

Аннотированная библиография книги. Ссылки проверены на момент написания: для статей — через arXiv, для курсов и документации — через HTTP-доступ, для видео — через YouTube oEmbed (название и канал). Где источник самозаявленный (карточка модели, блог вендора, документация проекта), это указано.

Уровни:

- **новичок** — можно читать без специальной подготовки;
- **средний** — нужно понимать трансформеры и базовую математику;
- **продвинутый** — нужны системы, CUDA или глубокое знание архитектур.

## Курсы

- **Stanford CS336: Language Modeling from Scratch** — Stanford, 2024–2026. [stanford-cs336.github.io](https://stanford-cs336.github.io/). Уровень: продвинутый. Зачем: полный путь от токенизации и трансформера до обучения и масштабирования; задания заставляют писать код, а не только читать.
- **Stanford CS224n: Natural Language Processing with Deep Learning** — Stanford, 2024–2025. [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/). Уровень: средний. Зачем: классический курс по NLP и трансформерам; полезен для понимания attention и эмбеддингов.
- **CMU 11-868: Large Language Model Systems** — Lei Li, CMU, Fall 2026. [llmsystem.github.io](https://llmsystem.github.io/llmsystem2026fall/). Уровень: продвинутый. Зачем: GPU-программирование, kernels, serving, quantization, paged attention; ближе всего к теме этой книги.
- **MIT 6.5940: TinyML and Efficient Deep Learning Computing** — Song Han, MIT, Fall 2024. [hanlab.mit.edu](https://hanlab.mit.edu/courses/2024-fall-65940). Уровень: продвинутый. Зачем: эффективные модели, квантование, pruning, ускорение inference.
- **Hugging Face LLM Course** — Hugging Face, постоянно обновляется. [huggingface.co/learn/llm-course](https://huggingface.co/learn/llm-course/chapter1/1). Уровень: новичок. Зачем: практическое введение в модели, токенизаторы и fine-tuning.
- **Hugging Face Agents Course** — Hugging Face, 2025. [huggingface.co/learn/agents-course](https://huggingface.co/learn/agents-course/unit0/introduction). Уровень: средний. Зачем: практика агентов, инструментов и оркестрации.

## Книги

- **Dive into Deep Learning** — Aston Zhang, Zachary Lipton, Mu Li, Alex Smola, 2023. [d2l.ai](https://d2l.ai/). Уровень: новичок–средний. Зачем: бесплатный учебник с кодом; главы про attention и трансформеры хорошо дополняют главу 1.
- **Speech and Language Processing (3-е изд., черновик)** — Daniel Jurafsky, James Martin, 2024–2026. [web.stanford.edu/~jurafsky/slp3](https://web.stanford.edu/~jurafsky/slp3/). Уровень: средний. Зачем: фундаментальный учебник по NLP; разделы про языковые модели и decoding.
- **Deep Learning** — Ian Goodfellow, Yoshua Bengio, Aaron Courville, 2016. [deeplearningbook.org](https://www.deeplearningbook.org/). Уровень: средний–продвинутый. Зачем: база по нейросетям, оптимизации и представлениям; местами устарела, но фундамент хороший.
- **The Little Book of Deep Learning** — François Fleuret, 2023. [PDF](https://fleuret.org/public/lbdl.pdf). Уровень: новичок. Зачем: короткое и плотное введение; хороший «освежитель» перед курсом.
- **Build a Large Language Model (From Scratch)** — Sebastian Raschka, Manning, 2024. [manning.com](https://www.manning.com/books/build-a-large-language-model-from-scratch). Уровень: средний. Зачем: пошаговая реализация GPT; связывает теорию с кодом.
- **Hands-On Large Language Models** — Jay Alammar, Maarten Grootendorst, O'Reilly, 2024. [O'Reilly](https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/). Уровень: новичок–средний. Зачем: визуальное введение в LLM и практические примеры; страница может требовать подписки.
- **AI Engineering** — Chip Huyen, O'Reilly, 2025. [huyenchip.com/books](https://huyenchip.com/books/). Уровень: средний. Зачем: как строить приложения на моделях: оценка, RAG, агенты, эксплуатация.
- **Designing Machine Learning Systems** — Chip Huyen, O'Reilly, 2022. [huyenchip.com/books](https://huyenchip.com/books/). Уровень: средний. Зачем: системное мышление про данные, деплой и мониторинг; полезно для серверной части.
- **«AI Infra in Depth: Quantitative Analysis and System Design»** — Bojie Li (Боцзе Ли), 2026, Apache-2.0. [GitHub](https://github.com/bojieli/ai-infra-book). Уровень: продвинутый. Зачем: следующий уровень после одного ПК — количественные оценки памяти и roofline, батчинг и KV, несколько GPU и сеть, распределённый инференс, обучение. Из неё адаптированы §12.7, приложения о заблуждениях и порядке анализа, метрики TTFT/ITL, закон Литтла, `b*`, `E[N]` и безубыточный черновик.
- **«AI-инфраструктура изнутри»** — русский перевод community edition, организатор [@ilkruglov](https://github.com/ilkruglov), Apache-2.0. [GitHub](https://github.com/ilkruglov/ai-infra-book). Уровень: продвинутый. Зачем: тот же текст с сохранённой нумерацией глав и разделов; использован для сверки терминов и цитат. Неофициальное издание сообщества, не замена авторской редактуре.
- **«Designing AI Infra» (скилл)** — [@ilkruglov](https://github.com/ilkruglov), Apache-2.0. [GitHub](https://github.com/ilkruglov/designing-ai-infra-skill). Уровень: продвинутый. Зачем: каталог заблуждений, шпаргалка порядка анализа и плейбук диагностики сервинга; послужили основой для приложений и §12.7, пересказаны и пересчитаны под локальный масштаб.

## Архитектура и основы

- **«Attention Is All You Need»** — Vaswani et al., 2017. [arXiv:1706.03762](https://arxiv.org/abs/1706.03762). Уровень: средний. Зачем: первоисточник трансформера; читать после главы 1.
- **«The Transformer Family Version 2.0»** — Lilian Weng, 2023. [lilianweng.github.io](https://lilianweng.github.io/posts/2023-01-27-the-transformer-family-v2/). Уровень: средний. Зачем: обзор вариантов attention, нормализаций и позиционных кодировок.
- **«Attention? Attention!»** — Lilian Weng, 2018. [lilianweng.github.io](https://lilianweng.github.io/posts/2018-06-24-attention/). Уровень: новичок–средний. Зачем: интуиция attention до погружения в формулы.
- **«Transformers, the tech behind LLMs» (Deep Learning, глава 5)** — 3Blue1Brown, 2024. [YouTube](https://www.youtube.com/watch?v=wjZofJX0v4M). Уровень: новичок. Зачем: визуальное объяснение архитектуры.
- **«Attention in transformers, step-by-step» (глава 6)** — 3Blue1Brown, 2024. [YouTube](https://www.youtube.com/watch?v=eMlx5fFNoYc). Уровень: новичок. Зачем: пошаговая визуализация attention.
- **«Let's build GPT: from scratch, in code, spelled out»** — Andrej Karpathy, 2023. [YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY). Уровень: средний. Зачем: лучший переход от формул к коду.
- **«Let's reproduce GPT-2 (124M)»** — Andrej Karpathy, 2024. [YouTube](https://www.youtube.com/watch?v=l8pRSuU81PU). Уровень: средний–продвинутый. Зачем: обучение и генерация реальной модели, оптимизации.
- **«Deep Dive into LLMs like ChatGPT»** — Andrej Karpathy, 2025. [YouTube](https://www.youtube.com/watch?v=7xTGNNLPyMI). Уровень: новичок–средний. Зачем: общая картина обучения и инференса без кода.
- **«Intro to Large Language Models»** — Andrej Karpathy, 2023. [YouTube](https://www.youtube.com/watch?v=zjkBMFhNj_g). Уровень: новичок. Зачем: короткое введение в LLM.
- **«Neural Networks: Zero to Hero»** — Andrej Karpathy, 2022–2024. [плейлист](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ). Уровень: новичок–средний. Зачем: от backprop до GPT, последовательно.
- **«Coding LLaMA 2 from scratch in PyTorch»** — Umar Jamil, 2023. [YouTube](https://www.youtube.com/watch?v=oM4VmoabDAI). Уровень: средний. Зачем: KV-кэш, RoPE, GQA и сэмплинг в коде.
- **«Flash Attention derived and coded from first principles with Triton»** — Umar Jamil, 2024. [YouTube](https://www.youtube.com/watch?v=zy8ChVd_oTM). Уровень: продвинутый. Зачем: IO-aware attention и Triton-кернел шаг за шагом.
- **nanoGPT** — Andrej Karpathy, 2022–2024. [GitHub](https://github.com/karpathy/nanoGPT). Уровень: средний. Зачем: минимальная кодовая база для экспериментов с GPT.
- **llm.c** — Andrej Karpathy, 2024. [GitHub](https://github.com/karpathy/llm.c). Уровень: продвинутый. Зачем: обучение LLM на C/CUDA; полезно для понимания низкого уровня.

## Производительность, память, roofline

- **«Efficiently Scaling Transformer Inference»** — Pope et al., 2022. [arXiv:2211.05102](https://arxiv.org/abs/2211.05102). Уровень: продвинутый. Зачем: формальный анализ памяти, вычислений и батчинга.
- **«Making Deep Learning Go Brrrr From First Principles»** — Horace He, 2022. [horace.io](https://horace.io/brrr_intro.html). Уровень: средний. Зачем: compute-bound vs memory-bound на пальцах.
- **«Transformer Inference Arithmetic»** — kipply, 2022. [kipp.ly](https://kipp.ly/transformer-inference-arithmetic/). Уровень: средний–продвинутый. Зачем: детальные расчёты FLOPs, байт и задержек.
- **«LLM Inference Performance Engineering: Best Practices»** — Databricks, 2023. [блог](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices). Уровень: средний. Зачем: метрики TTFT/ITL и практика продакшена.
- **«What Every Programmer Should Know About Memory»** — Ulrich Drepper, 2007. [PDF](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf). Уровень: продвинутый. Зачем: классика про кэши, задержки и пропускную способность.
- **«LLM in a flash»** — Alizadeh et al., 2023. [arXiv:2312.11514](https://arxiv.org/abs/2312.11514). Уровень: продвинутый. Зачем: выгрузка весов на флеш-память и цена чтения с диска.
- **NVIDIA H100** — NVIDIA. [nvidia.com](https://www.nvidia.com/en-us/data-center/h100/). Уровень: справка. Зачем: пример спецификации HBM (3,35 ТБ/с у SXM).
- **GeForce RTX 5090** — NVIDIA. [nvidia.com](https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/). Уровень: справка. Зачем: пример потребительской карты; точную пропускную способность смотрите в спецификации.
- **Mac Studio — Technical Specifications** — Apple, 2026. [apple.com](https://www.apple.com/mac-studio/specs/). Уровень: справка. Зачем: пропускная способность объединённой памяти M5 Max/Ultra (460–614 ГБ/с и до 1,2 ТБ/с).

## Квантование

- **«GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers»** — Frantar et al., 2022. [arXiv:2210.17323](https://arxiv.org/abs/2210.17323). Уровень: продвинутый. Зачем: пост-тренировочное квантование с компенсацией ошибки.
- **«AWQ: Activation-aware Weight Quantization»** — Lin et al., 2023. [arXiv:2306.00978](https://arxiv.org/abs/2306.00978). Уровень: продвинутый. Зачем: защита важных каналов по активациям.
- **«SmoothQuant»** — Xiao et al., 2022. [arXiv:2211.10438](https://arxiv.org/abs/2211.10438). Уровень: продвинутый. Зачем: перенос сложности квантования с активаций на веса.
- **«LLM.int8()»** — Dettmers et al., 2022. [arXiv:2208.07339](https://arxiv.org/abs/2208.07339). Уровень: продвинутый. Зачем: 8-битное умножение с обработкой выбросов.
- **«The case for 4-bit precision: k-bit Inference Scaling Laws»** — Dettmers, Zettlemoyer, 2022. [arXiv:2212.09720](https://arxiv.org/abs/2212.09720). Уровень: средний–продвинутый. Зачем: эмпирика о том, когда 4 бита достаточны.
- **llama.cpp PR #1684, «k-quants»** — ggml-org, 2023. [GitHub](https://github.com/ggml-org/llama.cpp/pull/1684). Уровень: продвинутый. Зачем: исходное обсуждение k-quants.
- **llama.cpp PR #4861, «Importance Matrix calculation»** — ggml-org, 2024. [GitHub](https://github.com/ggml-org/llama.cpp/pull/4861). Уровень: продвинутый. Зачем: как работает imatrix.
- **llama.cpp, `tools/quantize/README.md`** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md). Уровень: средний. Зачем: практические команды квантования.
- **llama.cpp Discussion #5063, «Even more quantization types?»** — ggml-org, 2023. [GitHub](https://github.com/ggml-org/llama.cpp/discussions/5063). Уровень: продвинутый. Зачем: эволюция типов и компромиссы.
- **«Unsloth Dynamic GGUFs»** — Unsloth. [docs.unsloth.ai](https://docs.unsloth.ai/basics/dynamic-3.0-ggufs). Уровень: средний. Зачем: динамические кванты; заявления авторов, не независимая проверка.
- **«Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA»** — Hugging Face, 2023. [блог](https://huggingface.co/blog/4bit-transformers-bitsandbytes). Уровень: новичок–средний. Зачем: доступное введение в 4-битное квантование.
- **Transformers quantization overview** — Hugging Face. [docs](https://huggingface.co/docs/transformers/main/en/quantization/overview). Уровень: средний. Зачем: карта форматов и библиотек.

## MoE

- **«Switch Transformers»** — Fedus, Zoph, Shazeer, 2021. [arXiv:2101.03961](https://arxiv.org/abs/2101.03961). Уровень: продвинутый. Зачем: top-1 роутинг и балансировка.
- **«Mixtral of Experts»** — Jiang et al., 2024. [arXiv:2401.04088](https://arxiv.org/abs/2401.04088). Уровень: средний. Зачем: популярная MoE и её поведение.
- **«DeepSeekMoE»** — Dai et al., 2024. [arXiv:2401.06066](https://arxiv.org/abs/2401.06066). Уровень: продвинутый. Зачем: fine-grained эксперты и shared experts.
- **«Mixture of Experts Explained»** — Hugging Face, 2022. [блог](https://huggingface.co/blog/moe). Уровень: новичок–средний. Зачем: лучшее визуальное введение в MoE.
- **«Performant local mixture-of-experts CPU inference with GPU acceleration in llama.cpp»** — Doctor-Shotgun, Hugging Face, 2024. [блог](https://huggingface.co/blog/Doctor-Shotgun/llamacpp-moe-offload-guide). Уровень: средний. Зачем: схема «attention на GPU, эксперты в RAM».
- **«DeepSeek-V3 Technical Report»** — DeepSeek-AI, 2024. [arXiv:2412.19437](https://arxiv.org/abs/2412.19437). Уровень: продвинутый. Зачем: большая MoE, shared experts, MTP.

## KV-кэш, контекст, позиционные кодировки

- **«RoFormer: Enhanced Transformer with Rotary Position Embedding»** — Su et al., 2021. [arXiv:2104.09864](https://arxiv.org/abs/2104.09864). Уровень: продвинутый. Зачем: первоисточник RoPE.
- **«YaRN: Efficient Context Window Extension»** — Peng et al., 2023. [arXiv:2309.00071](https://arxiv.org/abs/2309.00071). Уровень: продвинутый. Зачем: расширение контекста.
- **«Extending Context Window via Positional Interpolation»** — Chen et al., 2023. [arXiv:2306.15595](https://arxiv.org/abs/2306.15595). Уровень: продвинутый. Зачем: простой способ растянуть позиции.
- **«Train Short, Test Long: ALiBi»** — Press, Smith, Lewis, 2021. [arXiv:2108.12409](https://arxiv.org/abs/2108.12409). Уровень: продвинутый. Зачем: альтернатива RoPE с линейным штрафом.
- **«GQA»** — Ainslie et al., 2023. [arXiv:2305.13245](https://arxiv.org/abs/2305.13245). Уровень: продвинутый. Зачем: групповые KV-головы.
- **«Fast Transformer Decoding: One Write-Head is All You Need»** — Shazeer, 2019. [arXiv:1911.02150](https://arxiv.org/abs/1911.02150). Уровень: продвинутый. Зачем: MQA.
- **«DeepSeek-V2»** — DeepSeek-AI, 2024. [arXiv:2405.04434](https://arxiv.org/abs/2405.04434). Уровень: продвинутый. Зачем: MLA и сжатие KV.
- **«Gated Delta Networks: Improving Mamba2 with Delta Rule»** — Yang, Kautz, Hatamizadeh, 2024. [arXiv:2412.06464](https://arxiv.org/abs/2412.06464). Уровень: продвинутый. Зачем: гибридное линейное внимание; в тексте книги — Gated DeltaNet.
- **«Transformers are RNNs»** — Katharopoulos et al., 2020. [arXiv:2006.16236](https://arxiv.org/abs/2006.16236). Уровень: продвинутый. Зачем: линейное внимание.
- **«Mamba»** — Gu, Dao, 2023. [arXiv:2312.00752](https://arxiv.org/abs/2312.00752). Уровень: продвинутый. Зачем: state-space модели.
- **«H2O: Heavy-Hitter Oracle»** — Zhang et al., 2023. [arXiv:2306.14048](https://arxiv.org/abs/2306.14048). Уровень: продвинутый. Зачем: вытеснение неважных токенов из KV.
- **«Efficient Streaming Language Models with Attention Sinks»** — Xiao et al., 2023. [arXiv:2309.17453](https://arxiv.org/abs/2309.17453). Уровень: продвинутый. Зачем: StreamingLLM и attention sinks.
- **«KIVI»** — Liu et al., 2024. [arXiv:2402.02750](https://arxiv.org/abs/2402.02750). Уровень: продвинутый. Зачем: 2-битное квантование KV.
- **«SnapKV»** — Li et al., 2024. [arXiv:2404.14469](https://arxiv.org/abs/2404.14469). Уровень: продвинутый. Зачем: выбор важных позиций.
- **«A Survey on KV Cache Management»** — Li et al., 2024. [arXiv:2412.19442](https://arxiv.org/abs/2412.19442). Уровень: продвинутый. Зачем: карта методов сжатия и управления KV.

## Serving, кэш, батчинг

- **«Prompt Cache: Modular Attention Reuse»** — Gim et al., 2023. [arXiv:2311.04934](https://arxiv.org/abs/2311.04934). Уровень: продвинутый. Зачем: переиспользование частей промпта.
- **«SGLang: Efficient Execution of Structured Language Model Programs»** — Zheng et al., 2023. [arXiv:2312.07104](https://arxiv.org/abs/2312.07104). Уровень: продвинутый. Зачем: RadixAttention и разделяемый кэш.
- **«PagedAttention / vLLM»** — Kwon et al., 2023. [arXiv:2309.06180](https://arxiv.org/abs/2309.06180). Уровень: продвинутый. Зачем: управление KV блоками.
- **vLLM blog, «Easy, Fast, and Cheap LLM Serving»** — vLLM, 2023. [blog.vllm.ai](https://blog.vllm.ai/2023/06/20/vllm.html). Уровень: средний. Зачем: доступное объяснение PagedAttention.
- **vLLM, «Automatic Prefix Caching»** — vLLM. [docs.vllm.ai](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching.html). Уровень: средний. Зачем: как устроен кэш префиксов в vLLM.
- **vLLM, «Paged Attention» design doc** — vLLM. [docs.vllm.ai](https://docs.vllm.ai/en/latest/design/paged_attention.html). Уровень: продвинутый. Зачем: детали реализации.
- **«Orca: A Distributed Serving System»** — Yu et al., OSDI 2022. [USENIX](https://www.usenix.org/conference/osdi22/presentation/yu). Уровень: продвинутый. Зачем: итеративный батчинг.
- **«How continuous batching enables 23x throughput»** — Anyscale, 2022. [блог](https://www.anyscale.com/blog/continuous-batching-llm-inference). Уровень: средний. Зачем: наглядный разбор continuous batching.
- **llama.cpp Discussion #10260** — ggml-org, 2024. [GitHub](https://github.com/ggml-org/llama.cpp/discussions/10260). Уровень: средний. Зачем: разница `-b` и `-ub`.
- **llama.cpp, `tools/server/README.md`** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md). Уровень: средний. Зачем: флаги сервера, KV, MoE, tools.
- **llama.cpp, `docs/speculative.md`** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md). Уровень: средний. Зачем: типы спекуляции и флаги.
- **llama.cpp PR #22673, «MTP Support»** — ggml-org, 2026. [GitHub](https://github.com/ggml-org/llama.cpp/pull/22673). Уровень: продвинутый. Зачем: поддержка MTP-голов.
- **llama.cpp, `tools/llama-bench/README.md`** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md). Уровень: средний. Зачем: методика микробенчмарка.
- **GGUF specification** — ggml-org. [GitHub](https://github.com/ggml-org/ggml/blob/master/docs/gguf.md). Уровень: продвинутый. Зачем: формат файла модели.
- **ggml** — ggml-org. [GitHub](https://github.com/ggml-org/ggml). Уровень: продвинутый. Зачем: тензорная библиотека под llama.cpp.
- **llama.cpp Discussion #4167** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/discussions/4167). Уровень: средний. Зачем: примеры замеров на Apple Silicon.
- **llama.cpp, `docs/function-calling.md`** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/blob/master/docs/function-calling.md). Уровень: средний. Зачем: `--jinja`, `tool_choice`, параллельные вызовы.
- **llama.cpp, `grammars/README.md`** — ggml-org. [GitHub](https://github.com/ggml-org/llama.cpp/blob/master/grammars/README.md). Уровень: средний. Зачем: синтаксис GBNF.
- **vLLM, «Tool Calling»** — vLLM. [docs.vllm.ai](https://docs.vllm.ai/en/latest/features/tool_calling.html). Уровень: средний. Зачем: strict schema и `tool_choice`.

## Спекулятивное декодирование

- **«Fast Inference from Transformers via Speculative Decoding»** — Leviathan, Kalman, Matias, 2022. [arXiv:2211.17192](https://arxiv.org/abs/2211.17192). Уровень: продвинутый. Зачем: формализация и анализ.
- **«Accelerating Large Language Model Decoding with Speculative Sampling»** — Chen et al., 2023. [arXiv:2302.01318](https://arxiv.org/abs/2302.01318). Уровень: продвинутый. Зачем: схема с сохранением распределения.
- **«Medusa»** — Cai et al., 2024. [arXiv:2401.10774](https://arxiv.org/abs/2401.10774). Уровень: продвинутый. Зачем: множественные головы и дерево.
- **«EAGLE»** — Li et al., 2024. [arXiv:2401.15077](https://arxiv.org/abs/2401.15077). Уровень: продвинутый. Зачем: черновик на признаках.
- **«EAGLE-2»** — Li et al., 2024. [arXiv:2406.16858](https://arxiv.org/abs/2406.16858). Уровень: продвинутый. Зачем: динамическое дерево.
- **«EAGLE-3»** — Li et al., 2025. [arXiv:2503.01840](https://arxiv.org/abs/2503.01840). Уровень: продвинутый. Зачем: обучение с test-time scaling.

## Сэмплинг и рассуждение

- **«The Curious Case of Neural Text Degeneration»** — Holtzman et al., 2019. [arXiv:1904.09751](https://arxiv.org/abs/1904.09751). Уровень: средний. Зачем: nucleus sampling.
- **«Hierarchical Neural Story Generation»** — Fan, Lewis, Dauphin, 2018. [arXiv:1805.04833](https://arxiv.org/abs/1805.04833). Уровень: средний. Зачем: top-k sampling.
- **«Turning Up the Heat: Min-p Sampling»** — Nguyen et al., 2024. [arXiv:2407.01082](https://arxiv.org/abs/2407.01082). Уровень: средний. Зачем: адаптивная обрезка.
- **«Chain-of-Thought Prompting»** — Wei et al., 2022. [arXiv:2201.11903](https://arxiv.org/abs/2201.11903). Уровень: средний. Зачем: почему промежуточные рассуждения помогают.
- **«Self-Consistency Improves Chain of Thought Reasoning»** — Wang et al., 2022. [arXiv:2203.11171](https://arxiv.org/abs/2203.11171). Уровень: средний. Зачем: несколько траекторий и голосование.
- **«s1: Simple test-time scaling»** — Muennighoff et al., 2025. [arXiv:2501.19393](https://arxiv.org/abs/2501.19393). Уровень: продвинутый. Зачем: бюджетное управление рассуждением.
- **«DeepSeek-R1»** — DeepSeek-AI, 2025. [arXiv:2501.12948](https://arxiv.org/abs/2501.12948). Уровень: продвинутый. Зачем: рассуждающая модель и RL.

## Инструменты и структурированный вывод

- **«Gorilla: Large Language Model Connected with Massive APIs»** — Patil et al., 2023. [arXiv:2305.15334](https://arxiv.org/abs/2305.15334). Уровень: средний. Зачем: обучение вызову API.
- **«Toolformer»** — Schick et al., 2023. [arXiv:2302.04761](https://arxiv.org/abs/2302.04761). Уровень: средний. Зачем: модель учится вызывать инструменты.
- **«Efficient Guided Generation for Large Language Models»** — Willard, Louf, 2023. [arXiv:2307.09702](https://arxiv.org/abs/2307.09702). Уровень: продвинутый. Зачем: Outlines и маскирование логитов.
- **«XGrammar»** — Dong et al., 2024. [arXiv:2411.15100](https://arxiv.org/abs/2411.15100). Уровень: продвинутый. Зачем: быстрая структурированная генерация.
- **Berkeley Function Calling Leaderboard** — UC Berkeley. [gorilla.cs.berkeley.edu](https://gorilla.cs.berkeley.edu/leaderboard.html). Уровень: средний. Зачем: публичный бенчмарк tool calling.

## Оценка моделей и бенчмарки

- **«Model Cards for Model Reporting»** — Mitchell et al., 2018. [arXiv:1810.03993](https://arxiv.org/abs/1810.03993). Уровень: новичок–средний. Зачем: что должно быть в карточке модели.
- **«Holistic Evaluation of Language Models»** — Liang et al., 2022. [arXiv:2211.09110](https://arxiv.org/abs/2211.09110). Уровень: средний. Зачем: почему один бенчмарк не описывает модель.
- **«Measuring Massive Multitask Language Understanding»** — Hendrycks et al., 2020. [arXiv:2009.03300](https://arxiv.org/abs/2009.03300). Уровень: средний. Зачем: MMLU и его ограничения.
- **«Chatbot Arena»** — Chiang et al., 2024. [arXiv:2403.04132](https://arxiv.org/abs/2403.04132). Уровень: средний. Зачем: что измеряют предпочтения людей.
- **«Adding Error Bars to Evals»** — Evan Miller, 2024. [arXiv:2411.00640](https://arxiv.org/abs/2411.00640). Уровень: средний. Зачем: статистика для оценок.
- **MLPerf Inference** — MLCommons. [mlcommons.org](https://mlcommons.org/benchmarks/inference-datacenter/). Уровень: продвинутый. Зачем: пример строгой методологии бенчмарка.

## Речь и OCR

- **«Robust Speech Recognition via Large-Scale Weak Supervision»** — Radford et al., 2022. [arXiv:2212.04356](https://arxiv.org/abs/2212.04356). Уровень: продвинутый. Зачем: оригинальная статья Whisper.
- **whisper.cpp** — ggml-org. [GitHub](https://github.com/ggml-org/whisper.cpp). Уровень: средний. Зачем: локальный запуск Whisper без Python.
- **«GigaAM: Efficient Self-Supervised Learner for Speech Recognition»** — Kutsakov et al., 2025. [arXiv:2506.01192](https://arxiv.org/abs/2506.01192). Уровень: продвинутый. Зачем: ASR-модель, обученная преимущественно на русской речи по данным авторов, и сравнение с Whisper-large-v3.
- **Silero VAD** — Silero. [GitHub](https://github.com/snakers4/silero-vad). Уровень: средний. Зачем: лёгкий детектор речи.
- **Tesseract documentation** — Tesseract OCR. [tesseract-ocr.github.io](https://tesseract-ocr.github.io/). Уровень: новичок. Зачем: установка и языковые пакеты.
- **«PP-OCR: A Practical Ultra Lightweight OCR System»** — Du et al., 2020. [arXiv:2009.09941](https://arxiv.org/abs/2009.09941). Уровень: продвинутый. Зачем: архитектура PP-OCR.
- **RapidOCR** — RapidAI. [GitHub](https://github.com/RapidAI/RapidOCR). Уровень: средний. Зачем: ONNX-порт для практического запуска.
- **PaddleOCR** — PaddlePaddle. [GitHub](https://github.com/PaddlePaddle/PaddleOCR). Уровень: средний. Зачем: полный инструментарий OCR.

## Блоги и практика

- **Tim Dettmers, «The Best GPUs for Deep Learning in 2023»** — 2023. [timdettmers.com](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/). Уровень: средний. Зачем: как выбирать GPU под нагрузку и память.
- **Chip Huyen, «Building A Generative AI Platform»** — 2024. [huyenchip.com](https://huyenchip.com/2024/07/25/genai-platform.html). Уровень: средний. Зачем: архитектура приложений вокруг моделей.

## Ограничения проверки

- **Самозаявленные числа.** Бенчмарки моделей, скорость в карточках и заявления вендоров не проверялись независимо. В книге они либо не используются как факты, либо помечены.
- **Версии рантаймов.** Флаги llama.cpp и поведение сервера меняются между сборками. Сверяйте `--help` своей версии и документацию.
- **Железо.** Точные значения пропускной способности и объёма памяти зависят от конкретной модели карты, драйвера и охлаждения. В книге — порядки величин.
- **Даты.** Для некоторых постов и документации точная дата не указана; приведён год или «постоянно обновляется».
- **Языковые модели.** Русскоязычные бенчмарки (MERA, ruBFCL и др.) существуют, но независимых сравнений на технических документах мало; в книге нет утверждений, которые опирались бы на такие неполные данные.
- **O'Reilly.** Страницы книг могут требовать подписки; метаданные (автор, год, название) проверены по каталогу.
