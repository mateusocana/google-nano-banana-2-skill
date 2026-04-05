# Instalacao

## Copiar para workspace OpenClaw

```bash
cp -r skill/google-nano-banana-2 ~/.openclaw/workspace/skills/
```

Reinicie ou abra uma nova sessao do OpenClaw para carregar a skill.

## Empacotar como .skill

```bash
python3 "$(openclaw skills path)/skill-creator/scripts/package_skill.py" \
  skill/google-nano-banana-2 ./dist
```

Gera `./dist/google-nano-banana-2.skill` para distribuicao.

## Estrutura da skill

```
google-nano-banana-2/
├── SKILL.md
└── scripts/
    └── google-nano-banana-2.py
```
