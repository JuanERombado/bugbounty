# Local LLM Recommendation

## Current Machine

- CPU: AMD Ryzen 5 7600X, 6 cores / 12 threads
- RAM: 32 GB
- GPU: AMD Radeon RX 7800 XT, 16 GB VRAM
- OS: Windows 11

## Recommended Default

Use `Qwen3-Coder-30B-A3B-Instruct` at `Q4_K_M` or similar 4-bit GGUF as the high-quality local coding/security model.

Run it through LM Studio first, using the AMD ROCm or Vulkan runtime, because it is the lowest-friction Windows path for an AMD GPU.

## Practical Fallback

If the 30B-A3B model feels slow, unstable, or cannot hold enough context, use `Qwen2.5-Coder-14B-Instruct` or `Qwen3-14B` at `Q5_K_M`/`Q4_K_M`.

This should be the daily worker model for summarizing hotspots, generating local hypotheses, and classifying artifacts.

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
- Expect 30B-class models to be slower on Windows AMD than NVIDIA CUDA systems.
- If long-running worker throughput matters, Linux/ROCm or WSL2 may outperform native Windows.

## Next Build Step

Add an OpenAI-compatible local provider adapter for LM Studio, then point worker prompt jobs at `http://localhost:1234/v1/chat/completions`.
