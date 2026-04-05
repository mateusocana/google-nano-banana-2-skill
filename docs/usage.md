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

A imagem gerada e salva no diretorio de saida (padrao: `generated/google-nano-banana-2/` no workspace). O caminho e impresso em stdout para uso pelo agente.
