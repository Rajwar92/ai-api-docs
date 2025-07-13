# Error Codes

Complete reference of all API error codes and their meanings.

## Error Response Format

All API errors follow a consistent format:

```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {
      "field": "specific_field_name",
      "issue": "detailed_issue_description"
    }
  },
  "meta": {
    "request_id": "req_1234567890",
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## HTTP Status Codes

| Status | Description |
|--------|-------------|
| `200` | Success |
| `201` | Created |
| `400` | Bad Request |
| `401` | Unauthorized |
| `403` | Forbidden |
| `404` | Not Found |
| `429` | Rate Limit Exceeded |
| `500` | Internal Server Error |
| `502` | Bad Gateway |
| `503` | Service Unavailable |

## Authentication Errors

### 401 - Unauthorized

| Code | Message | Description |
|------|---------|-------------|
| `MISSING_API_KEY` | API key is required | No API key provided in request |
| `INVALID_API_KEY` | The provided API key is invalid | API key format is incorrect or doesn't exist |
| `EXPIRED_API_KEY` | The API key has expired | API key has passed its expiration date |
| `REVOKED_API_KEY` | The API key has been revoked | API key was manually revoked |

### 403 - Forbidden

| Code | Message | Description |
|------|---------|-------------|
| `INSUFFICIENT_PERMISSIONS` | Insufficient permissions for this operation | API key lacks required permissions |
| `ACCOUNT_SUSPENDED` | Account has been suspended | Account is temporarily or permanently suspended |
| `QUOTA_EXCEEDED` | Monthly quota exceeded | Monthly usage limit has been reached |

## Request Errors

### 400 - Bad Request

| Code | Message | Description |
|------|---------|-------------|
| `INVALID_REQUEST` | The request was invalid | General request validation error |
| `MISSING_REQUIRED_FIELD` | Required field is missing | A required parameter was not provided |
| `INVALID_FIELD_VALUE` | Field value is invalid | Parameter value doesn't meet requirements |
| `UNSUPPORTED_MODEL` | Model is not supported | Specified model doesn't exist or isn't available |
| `INVALID_FILE_FORMAT` | File format is not supported | Uploaded file format is not accepted |
| `FILE_TOO_LARGE` | File size exceeds limit | File is larger than allowed maximum |

### 404 - Not Found

| Code | Message | Description |
|------|---------|-------------|
| `RESOURCE_NOT_FOUND` | Resource not found | Requested resource doesn't exist |
| `ENDPOINT_NOT_FOUND` | Endpoint not found | API endpoint doesn't exist |
| `MODEL_NOT_FOUND` | Model not found | Specified model doesn't exist |

## Rate Limiting Errors

### 429 - Rate Limit Exceeded

| Code | Message | Description |
|------|---------|-------------|
| `RATE_LIMIT_EXCEEDED` | Rate limit exceeded | Too many requests in the time window |
| `CONCURRENT_LIMIT_EXCEEDED` | Too many concurrent requests | Too many simultaneous requests |

## Server Errors

### 500 - Internal Server Error

| Code | Message | Description |
|------|---------|-------------|
| `INTERNAL_ERROR` | Internal server error | Unexpected server error |
| `MODEL_UNAVAILABLE` | Model is temporarily unavailable | AI model is down for maintenance |
| `PROCESSING_ERROR` | Error processing request | Error occurred during request processing |

### 502/503 - Service Unavailable

| Code | Message | Description |
|------|---------|-------------|
| `SERVICE_UNAVAILABLE` | Service is temporarily unavailable | API is down for maintenance |
| `OVERLOADED` | Service is overloaded | Server is experiencing high load |

## Field-Specific Errors

### Text Generation Errors

| Code | Message | Field | Description |
|------|---------|-------|-------------|
| `PROMPT_TOO_LONG` | Prompt exceeds maximum length | `prompt` | Input text is too long |
| `INVALID_TEMPERATURE` | Temperature must be between 0 and 2 | `temperature` | Temperature value is out of range |
| `INVALID_MAX_TOKENS` | Max tokens must be positive | `max_tokens` | Token limit is invalid |

### Image Generation Errors

| Code | Message | Field | Description |
|------|---------|-------|-------------|
| `INVALID_IMAGE_SIZE` | Image size is not supported | `size` | Specified dimensions are invalid |
| `INVALID_IMAGE_QUALITY` | Image quality is not supported | `quality` | Quality setting is invalid |
| `PROMPT_VIOLATION` | Prompt violates content policy | `prompt` | Image description contains prohibited content |

## Error Handling Examples

### JavaScript

```javascript
async function handleAPIError(response) {
  if (!response.ok) {
    const error = await response.json();
    
    switch (response.status) {
      case 401:
        console.error('Authentication failed:', error.error.message);
        // Handle authentication error
        break;
      case 429:
        console.error('Rate limited:', error.error.message);
        // Implement retry logic
        break;
      case 400:
        console.error('Bad request:', error.error.message);
        // Handle validation errors
        break;
      default:
        console.error('API error:', error.error.message);
    }
    
    throw new Error(error.error.message);
  }
  
  return response.json();
}
```

### Python

```python
import requests

def handle_api_error(response):
    if not response.ok:
        error = response.json()
        
        if response.status_code == 401:
            print(f"Authentication failed: {error['error']['message']}")
        elif response.status_code == 429:
            print(f"Rate limited: {error['error']['message']}")
        elif response.status_code == 400:
            print(f"Bad request: {error['error']['message']}")
        else:
            print(f"API error: {error['error']['message']}")
        
        raise Exception(error['error']['message'])
    
    return response.json()
```

## Retry Logic

### Exponential Backoff

```javascript
async function retryWithBackoff(fn, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      if (attempt === maxRetries) throw error;
      
      // Don't retry on client errors (4xx)
      if (error.status >= 400 && error.status < 500) {
        throw error;
      }
      
      // Exponential backoff
      const delay = Math.pow(2, attempt) * 1000;
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}
```

## Request ID

Every error response includes a unique request ID that can be used for debugging:

```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The request was invalid"
  },
  "meta": {
    "request_id": "req_1234567890"
  }
}
```

Include this request ID when contacting support for faster resolution.

## Next Steps

- [Rate Limits](../getting-started/rate-limits.md) - Understand usage limits
- [Authentication](../getting-started/authentication.md) - Learn about API keys
- [Best Practices](../guides/best-practices.md) - Error handling patterns
- [Contact Support](../support/contact.md) - Get help with errors 