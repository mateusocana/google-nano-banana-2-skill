---
name: google-nano-banana-2
description: Generate and edit images via Google Gemini Image API (Nano Banana 2). Use when the user asks to generate an image, create a picture, make an illustration, edit a photo, modify an image, text-to-image, image generation, AI image, or any visual content creation using Google's official API. Triggers on "generate image", "create image", "edit image", "make a picture", "illustration", "image from text", "nano banana", "gemini image".
metadata:
  openclaw:
    emoji: "🎨"
    os: ["linux", "macos", "windows"]
    requires:
      config:
        - env.GEMINI_API_KEY
---

# Google Nano Banana 2

Generate or edit images via `scripts/google-nano-banana-2.py` using the Gemini Image API.

- Model: `gemini-3.1-flash-image-preview`
- Output: saved to `--outdir` (default: `generated/google-nano-banana-2/` in workspace)

## Workflow

1. Determine mode: text-to-image or image edit (with `--image`).
2. Run the script. Use the user's exact prompt — do not embellish.
3. Return saved path(s). Send the image in chat unless user opts out.

## Commands

```bash
# Text to image
python3 scripts/google-nano-banana-2.py --prompt "<prompt>"

# Image edit (up to 4 images)
python3 scripts/google-nano-banana-2.py --prompt "<edit instruction>" --image /path/to/input.png

# Custom output directory
python3 scripts/google-nano-banana-2.py --prompt "<prompt>" --outdir /custom/path
```

## Error handling

- `401` → invalid `GEMINI_API_KEY`, report directly.
- `429` → quota/rate limit, not a skill failure. Script retries automatically.
- Other errors → report raw API message, suggest adjusting model or prompt.
