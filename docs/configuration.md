# Configuracao

## Variavel obrigatoria

```bash
GEMINI_API_KEY=<sua-chave>
```

Configure no ambiente do OpenClaw (config ou `.env`).

## Modelo

Padrao: `gemini-3.1-flash-image-preview`

Override via variavel de ambiente:

```bash
GOOGLE_NANO_BANANA_MODEL=outro-modelo
```

## Diretorio de saida

Padrao: `generated/google-nano-banana-2/` relativo ao workspace do OpenClaw.

Override com `--outdir`:

```bash
python3 scripts/google-nano-banana-2.py --prompt "..." --outdir /custom/path
```

## API base

Override (raro):

```bash
GOOGLE_GEMINI_API_BASE=https://custom-endpoint.example.com
```
