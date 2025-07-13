# API Reference

Welcome to the complete API reference for our AI-powered platform. This documentation covers all available endpoints, request/response formats, and authentication methods.

## Base URL

```
https://api.example.com/v1
```

## Authentication

All API requests require authentication using your API key in the Authorization header:

```
Authorization: Bearer YOUR_API_KEY
```

## Rate Limits

- **Free Tier**: 1,000 requests per month
- **Pro Tier**: 10,000 requests per month
- **Enterprise**: Custom limits

Rate limits are applied per API key and reset monthly.

## Response Format

All API responses follow a consistent JSON format:

```json
{
  "success": true,
  "data": {
    // Response data here
  },
  "meta": {
    "request_id": "req_1234567890",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## Error Responses

Error responses include detailed information:

```json
{
  "success": false,
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The request was invalid",
    "details": {
      "field": "prompt",
      "issue": "Required field is missing"
    }
  },
  "meta": {
    "request_id": "req_1234567890",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## Endpoints

### Content Generation

#### Generate Text

Creates text content using AI models.

**Endpoint:** `POST /generate`

**Request Body:**

```json
{
  "prompt": "Write a blog post about artificial intelligence",
  "model": "gpt-4",
  "max_tokens": 500,
  "temperature": 0.7,
  "top_p": 1.0,
  "frequency_penalty": 0.0,
  "presence_penalty": 0.0
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | The input text to generate from |
| `model` | string | Yes | The AI model to use (gpt-4, gpt-3.5-turbo) |
| `max_tokens` | integer | No | Maximum tokens to generate (default: 100) |
| `temperature` | float | No | Controls randomness (0.0-2.0, default: 0.7) |
| `top_p` | float | No | Nucleus sampling parameter (0.0-1.0, default: 1.0) |
| `frequency_penalty` | float | No | Reduces repetition (-2.0-2.0, default: 0.0) |
| `presence_penalty` | float | No | Encourages new topics (-2.0-2.0, default: 0.0) |

**Response:**

```json
{
  "success": true,
  "data": {
    "id": "gen_1234567890",
    "content": "Artificial Intelligence (AI) has revolutionized...",
    "model": "gpt-4",
    "usage": {
      "prompt_tokens": 12,
      "completion_tokens": 150,
      "total_tokens": 162
    },
    "created": 1640995200
  }
}
```

#### Generate Images

Creates images using AI models.

**Endpoint:** `POST /generate/image`

**Request Body:**

```json
{
  "prompt": "A beautiful sunset over mountains",
  "model": "dall-e-3",
  "size": "1024x1024",
  "quality": "standard",
  "style": "natural"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `prompt` | string | Yes | Description of the image to generate |
| `model` | string | Yes | Image model (dall-e-3, stable-diffusion) |
| `size` | string | No | Image dimensions (default: "1024x1024") |
| `quality` | string | No | Image quality (standard, hd) |
| `style` | string | No | Artistic style (natural, vivid) |

**Response:**

```json
{
  "success": true,
  "data": {
    "id": "img_1234567890",
    "url": "https://api.example.com/images/img_1234567890.png",
    "model": "dall-e-3",
    "created": 1640995200
  }
}
```

### Analysis

#### Analyze Text

Performs text analysis and extraction.

**Endpoint:** `POST /analyze`

**Request Body:**

```json
{
  "text": "Sample text to analyze",
  "tasks": ["sentiment", "entities", "keywords"],
  "language": "en"
}
```

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `text` | string | Yes | Text to analyze |
| `tasks` | array | Yes | Analysis tasks to perform |
| `language` | string | No | Language code (default: "en") |

**Response:**

```json
{
  "success": true,
  "data": {
    "sentiment": {
      "score": 0.8,
      "label": "positive"
    },
    "entities": [
      {
        "text": "John Doe",
        "type": "PERSON",
        "confidence": 0.95
      }
    ],
    "keywords": [
      {
        "text": "artificial intelligence",
        "score": 0.92
      }
    ]
  }
}
```

### Models

#### List Available Models

Retrieves available AI models.

**Endpoint:** `GET /models`

**Response:**

```json
{
  "success": true,
  "data": [
    {
      "id": "gpt-4",
      "name": "GPT-4",
      "type": "text",
      "description": "Most capable text generation model",
      "max_tokens": 8192,
      "pricing": {
        "input": 0.03,
        "output": 0.06
      }
    },
    {
      "id": "dall-e-3",
      "name": "DALL-E 3",
      "type": "image",
      "description": "Advanced image generation model",
      "max_tokens": 4000,
      "pricing": {
        "input": 0.04,
        "output": 0.08
      }
    }
  ]
}
```

## Status Codes

| Code | Description |
|------|-------------|
| `200` | Success |
| `201` | Created |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `429` | Rate Limit Exceeded |
| `500` | Internal Server Error |

## SDKs and Libraries

We provide official SDKs for popular programming languages:

- [JavaScript/Node.js SDK](https://github.com/example/js-sdk)
- [Python SDK](https://github.com/example/python-sdk)
- [Go SDK](https://github.com/example/go-sdk)
- [Ruby SDK](https://github.com/example/ruby-sdk)

## Webhooks

Configure webhooks to receive real-time notifications:

- [Webhook Setup Guide](../guides/webhooks.md)
- [Webhook Events Reference](../api-reference/webhooks.md)

## Support

- [Error Codes](errors.md) - Complete error reference
- [Rate Limits](../getting-started/rate-limits.md) - Usage limits and quotas
- [Best Practices](../guides/best-practices.md) - Recommended patterns
- [Contact Support](../support/contact.md) - Get help