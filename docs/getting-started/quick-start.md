# Quick Start Guide

Get up and running with our AI-powered API in minutes!

## Prerequisites

- An API key (get one from your [dashboard](https://dashboard.example.com))
- Basic knowledge of HTTP requests
- Your preferred programming language

## Step 1: Get Your API Key

1. Sign up at [our platform](https://example.com/signup)
2. Navigate to the [API Keys section](https://dashboard.example.com/api-keys)
3. Create a new API key
4. Copy and securely store your key

<div class="admonition warning" markdown="1">
  <p class="admonition-title">Security Note</p>
  <p>Never expose your API key in client-side code or public repositories. Always use environment variables or secure configuration management.</p>
</div>

## Step 2: Make Your First Request

### Using cURL

```bash
curl -X POST https://api.example.com/v1/generate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Hello, how are you?",
    "model": "gpt-4",
    "max_tokens": 100
  }'
```

### Using JavaScript

```javascript
const response = await fetch('https://api.example.com/v1/generate', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    prompt: 'Hello, how are you?',
    model: 'gpt-4',
    max_tokens: 100
  })
});

const data = await response.json();
console.log(data.content);
```

### Using Python

```python
import requests

response = requests.post(
    'https://api.example.com/v1/generate',
    headers={
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
    },
    json={
        'prompt': 'Hello, how are you?',
        'model': 'gpt-4',
        'max_tokens': 100
    }
)

print(response.json()['content'])
```

## Step 3: Handle the Response

A successful response will look like this:

```json
{
  "id": "gen_1234567890",
  "content": "Hello! I'm doing well, thank you for asking. How can I help you today?",
  "model": "gpt-4",
  "usage": {
    "prompt_tokens": 7,
    "completion_tokens": 15,
    "total_tokens": 22
  },
  "created": 1640995200
}
```

## Step 4: Error Handling

Always handle potential errors in your requests:

```javascript
try {
  const response = await fetch('https://api.example.com/v1/generate', {
    method: 'POST',
    headers: {
      'Authorization': 'Bearer YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      prompt: 'Hello, how are you?',
      model: 'gpt-4',
      max_tokens: 100
    })
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(`API Error: ${error.error.message}`);
  }

  const data = await response.json();
  console.log(data.content);
} catch (error) {
  console.error('Error:', error.message);
}
```

## Common Error Codes

| Code | Description | Solution |
|------|-------------|----------|
| `401` | Unauthorized | Check your API key |
| `429` | Rate limit exceeded | Wait and retry |
| `400` | Bad request | Check your request format |
| `500` | Server error | Contact support |

## Next Steps

- [Authentication Guide](authentication.md) - Learn about different auth methods
- [Rate Limits](rate-limits.md) - Understand usage limits
- [API Reference](../api-reference/index.md) - Complete endpoint documentation
- [Examples](../examples/javascript.md) - More code examples

## Need Help?

- Check our [FAQ](../support/faq.md)
- Join our [Discord community](https://discord.gg/your-community)
- [Contact support](../support/contact.md) 