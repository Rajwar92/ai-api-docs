# cURL Examples

Use cURL to interact with our AI-powered API from the command line.

## Generate Text

```bash
curl -X POST https://api.example.com/v1/generate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "prompt": "Hello, world!", "model": "gpt-4" }'
```

## Generate Image

```bash
curl -X POST https://api.example.com/v1/generate/image \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "prompt": "A beautiful sunset over mountains", "model": "dall-e-3" }'
```

## Analyze Text

```bash
curl -X POST https://api.example.com/v1/analyze \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "text": "I love this API!", "tasks": ["sentiment"] }'
```

_See the [API Reference](../api-reference/index.md) for more endpoints and details._ 