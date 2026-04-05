# Instalação

## Opção 1: copiar a skill para um OpenClaw existente

```bash
cp -r skill/google-nano-banana-2 ~/.openclaw/workspace/skills/
```

Depois, reinicie ou abra uma nova sessão do OpenClaw para carregar a skill.

## Opção 2: empacotar como `.skill`

```bash
python3 /usr/lib/node_modules/openclaw/skills/skill-creator/scripts/package_skill.py \
  skill/google-nano-banana-2 \
  ./dist
```

Isso gera um arquivo como:

```bash
./dist/google-nano-banana-2.skill
```

Então instale no outro ambiente seguindo o método aceito por ele para skills locais ou empacotadas.

## Estrutura esperada
- `SKILL.md`
- `scripts/google-nano-banana-2.py`

Não incluir tokens, chaves ou arquivos temporários.
