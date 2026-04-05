# Uso

## Texto para imagem

```bash
python3 scripts/google-nano-banana-2.py \
  --prompt "Um JARVIS futurista em tons de azul e prata, estilo holograma"
```

## Edicao de imagem

```bash
python3 scripts/google-nano-banana-2.py \
  --prompt "Deixe a imagem mais cinematografica" \
  --image ./foto.png
```

## Multiplas imagens de entrada (ate 4)

```bash
python3 scripts/google-nano-banana-2.py \
  --prompt "Combine essas imagens em uma composicao" \
  --image ./foto1.png --image ./foto2.png
```

## Resultado

A imagem gerada é salva no diretório de saída padrão do workspace e enviada no chat do OpenClaw como anexo, sem legenda, quando o fluxo estiver usando essa skill.
