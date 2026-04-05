---
name: google-nano-banana-2
description: Generate or edit images with Google's official Gemini 3.1 Flash Image API (Nano Banana 2). Use when the user wants image generation or image editing through the official Google API, not third-party gateways.
metadata:
  openclaw:
    os: ["linux", "macos", "windows"]
    requires:
      config:
        - env.GEMINI_API_KEY
---

# Google Nano Banana 2

Use the bundled script `scripts/google-nano-banana-2.py` for official Google image generation.

## Defaults
- Model: `gemini-3.1-flash-image-preview`
- Official API only
- Save outputs under `/srv/obsidian-sync/openclaw/generated/google-nano-banana-2/` unless the user asks otherwise

## Workflow
1. Confirm whether the user wants:
   - text-to-image
   - edit an existing image
2. For text-to-image, run the script with `--prompt`.
3. For image edit, pass one or more `--image` paths plus `--prompt`.
4. Return the saved output path(s).
5. Send the generated image back in chat by default unless the user explicitly asks not to. Use the workspace path from the script output as the media path.
6. If the API returns 429, treat it as quota/rate limiting, not a skill failure, and retry only if the request was clearly transient.

## Commands

Text to image:
```bash
python3 /srv/obsidian-sync/openclaw/skills/google-nano-banana-2/scripts/google-nano-banana-2.py \
  --prompt "<prompt>" \
  [--model gemini-3.1-flash-image-preview] \
  [--outdir /tmp/google-nano-banana-2]
```

Image edit:
```bash
python3 /srv/obsidian-sync/openclaw/skills/google-nano-banana-2/scripts/google-nano-banana-2.py \
  --prompt "<edit instruction>" \
  --image /path/to/input.png \
  [--image /path/to/second.png] \
  [--model gemini-3.1-flash-image-preview] \
  [--outdir /tmp/google-nano-banana-2]
```

## Notes
- The script reads the API key from `GEMINI_API_KEY`.
- Prefer exact user prompts; do not silently embellish unless asked.
- If Google returns `401`, report the key issue directly.
- If Google returns `429`, report quota/rate limit directly and do not pretend the skill is broken.
- If Google returns another API/model error, report the raw reason briefly and suggest adjusting the model or prompt.
