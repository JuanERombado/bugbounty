# Local LLM Recommendation

## Current Machine

- CPU: AMD Ryzen 5 7600X, 6 cores / 12 threads
- RAM: 32 GB
- GPU: AMD Radeon RX 7800 XT, 16 GB VRAM
- OS: Windows 11

## Revised Recommendation

Do not use one model for every job.

Use a tiered setup:

1. Daily worker default: `Qwen3.5-9B` GGUF at `Q6_K` or `Q8_0` if available.
2. Strong local review model: `Devstral-Small-2-24B-Instruct` GGUF at `Q4_K_M`, or `Qwen3.5-27B` GGUF at `Q4_K_M` if it runs acceptably.
3. Experimental heavyweight: `Qwen3.5-35B-A3B` low-bit GGUF only if partial offload is stable and speed is tolerable.

Run through LM Studio first, using AMD ROCm or Vulkan, because it is the lowest-friction Windows path for an AMD GPU.

## Why Not Qwen3-Coder-30B-A3B As Default

`Qwen3-Coder-30B-A3B-Instruct` is still useful, but it is no longer the clear default because newer Qwen3.5 and Devstral models exist.

It remains a fallback if the newer models are unstable in LM Studio.

## Why Not Qwen3-Coder-Next-80B-A3B

`Qwen3-Coder-Next-80B-A3B` is newer and stronger, but the official GGUF Q4 size is about 48 GB, which is not a good fit for this machine's 16 GB VRAM and 32 GB RAM.

It may run with heavy CPU offload, but it is likely too slow for a continuous worker.

## Practical Ranking For This Machine

| Rank | Model | Role | Why |
| --- | --- | --- | --- |
| 1 | `Qwen3.5-9B` high quant | Always-on worker | Fast, compact, enough for summaries and hypothesis mutation. |
| 2 | `Devstral-Small-2-24B-Instruct` Q4 | Strong coding reviewer | Built for agentic software-engineering workflows. |
| 3 | `Qwen3.5-27B` Q4 | Strong general reasoning/coding | Good quality, but may be slower with 16 GB VRAM. |
| 4 | `Qwen3.5-35B-A3B` low-bit | Experimental quality tier | Newer MoE, but likely memory tight. |
| 5 | `Qwen3-Coder-30B-A3B` Q4 | Compatibility fallback | Older but proven coding model. |

## Role In The Workbench

The local model should not decide that a bug is valid.

Use it for:

- summarizing hotspot artifacts
- generating hypothesis variants
- proposing local Foundry/Echidna tests
- writing morning digests
- classifying results as `dead`, `needs_mutation`, `promising`, or `escalate_frontier`

Use Codex/Gemini only for compact evidence packages, difficult reasoning, and report-quality review.

## Expected Limits

- Keep context tight; do not feed whole repositories.
- Prefer code slices and run artifacts under 8k to 16k tokens.
- Expect 24B+ models to be slower on Windows AMD than NVIDIA CUDA systems.
- If long-running worker throughput matters, Linux/ROCm or WSL2 may outperform native Windows.

## Next Build Step

Add an OpenAI-compatible local provider adapter for LM Studio, then point worker prompt jobs at `http://localhost:1234/v1/chat/completions`.

Start with `Qwen3.5-9B` for throughput, then benchmark `Devstral-Small-2-24B-Instruct` against the same queue artifacts before deciding the default.
