# Configuração

## Variável obrigatória

A skill usa a variável de ambiente:

```bash
GEMINI_API_KEY
```

Exemplo:

```bash
export GEMINI_API_KEY="SUA_CHAVE_AQUI"
```

## Modelo usado

Padrão:

```bash
gemini-3.1-flash-image-preview
```

Se a sua conta/projeto usar outro identificador aceito pela Google, ajuste a variável:

```bash
export GOOGLE_NANO_BANANA_MODEL="outro-modelo"
```

## Saída padrão

As imagens são salvas por padrão em:

```bash
/srv/obsidian-sync/openclaw/generated/google-nano-banana-2/
```

Isso facilita o envio automático da imagem no chat do OpenClaw.

## Observações
- A quota do projeto Google precisa estar liberada.
- Se a API responder `429`, é limite/quota e não erro da skill.
