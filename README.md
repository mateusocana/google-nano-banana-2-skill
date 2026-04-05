# Google Nano Banana 2 — OpenClaw Skill

Skill para geração e edição de imagens via API oficial Google Gemini (`gemini-3.1-flash-image-preview`).

## Requisitos
- OpenClaw instalado
- `GEMINI_API_KEY` configurada no ambiente do OpenClaw
- Quota ativa no Google AI Studio

## Instalação

Copie a skill para o workspace do OpenClaw:

```bash
cp -r skill/google-nano-banana-2 ~/.openclaw/workspace/skills/
```

Ou empacote para distribuição:

```bash
python3 "$(openclaw skills path)/skill-creator/scripts/package_skill.py" \
  skill/google-nano-banana-2 ./dist
```

## Uso

Dentro do OpenClaw, peça para gerar ou editar imagens:

- "gera uma imagem de um robô futurista"
- "edita essa foto e deixa mais cinematográfica"

A skill será ativada automaticamente pelo agente.
