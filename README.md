# Google Nano Banana 2 Skill for OpenClaw

Skill oficial-lizada no formato de workspace para usar a API oficial da Google com o modelo Nano Banana 2 (`gemini-3.1-flash-image-preview`).

## O que tem aqui
- `skill/google-nano-banana-2/` - skill OpenClaw pronta para copiar ou instalar
- `docs/` - instalação, configuração e uso
- sem tokens ou segredos no repositório

## Requisitos
- OpenClaw instalado
- `GEMINI_API_KEY` configurada no ambiente do OpenClaw de destino
- acesso ao Gemini API / Google AI Studio com quota ativa

## Instalação rápida
```bash
cp -r skill/google-nano-banana-2 ~/.openclaw/workspace/skills/
```

Ou empacote para distribuição com o OpenClaw:
```bash
python3 /usr/lib/node_modules/openclaw/skills/skill-creator/scripts/package_skill.py \
  skill/google-nano-banana-2 \
  ./dist
```

## Docs
- [Instalação](docs/installation.md)
- [Configuração](docs/configuration.md)
- [Uso](docs/usage.md)
