# Authentication

Learn how to authenticate with our AI-powered API using API keys and other authentication methods.

## API Keys

API keys are the primary method of authentication for our API. Each API key is unique and should be kept secure.

### Getting Your API Key

1. **Sign up** at [our platform](https://example.com/signup)
2. **Navigate** to the [API Keys section](https://dashboard.example.com/api-keys)
3. **Create** a new API key
4. **Copy** and securely store your key

<div class="admonition warning" markdown="1">
  <p class="admonition-title">Security Warning</p>
  <p>Never expose your API key in client-side code, public repositories, or logs. Always use environment variables or secure configuration management.</p>
</div>

### Using API Keys

Include your API key in the `Authorization` header of all requests:

```bash
Authorization: Bearer YOUR_API_KEY
```

#### Example Requests

=== "cURL"
    ```bash
    curl -X POST https://api.example.com/v1/generate \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{
        "prompt": "Hello, world!",
        "model": "gpt-4"
      }'
    ```

=== "JavaScript"
    ```javascript
    const response = await fetch('https://api.example.com/v1/generate', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer YOUR_API_KEY',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        prompt: 'Hello, world!',
        model: 'gpt-4'
      })
    });
    ```

=== "Python"
    ```python
    import requests
    
    response = requests.post(
        'https://api.example.com/v1/generate',
        headers={
            'Authorization': 'Bearer YOUR_API_KEY',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': 'Hello, world!',
            'model': 'gpt-4'
        }
    )
    ```

## Environment Variables

Store your API key securely using environment variables:

### Unix/Linux/macOS

```bash
export API_KEY="your-api-key-here"
```

### Windows (Command Prompt)

```cmd
set API_KEY=your-api-key-here
```

### Windows (PowerShell)

```powershell
$env:API_KEY="your-api-key-here"
```

### Using Environment Variables in Code

=== "JavaScript"
    ```javascript
    const apiKey = process.env.API_KEY;
    
    const response = await fetch('https://api.example.com/v1/generate', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        prompt: 'Hello, world!',
        model: 'gpt-4'
      })
    });
    ```

=== "Python"
    ```python
    import os
    import requests
    
    api_key = os.environ.get('API_KEY')
    
    response = requests.post(
        'https://api.example.com/v1/generate',
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        json={
            'prompt': 'Hello, world!',
            'model': 'gpt-4'
        }
    )
    ```

## API Key Management

### Creating Multiple Keys

You can create multiple API keys for different purposes:

- **Development**: For testing and development
- **Production**: For live applications
- **Read-only**: For monitoring and analytics
- **Admin**: For administrative tasks

### Key Permissions

Each API key can have different permissions:

| Permission | Description |
|------------|-------------|
| `read` | Can read data and generate content |
| `write` | Can create and update resources |
| `admin` | Full administrative access |
| `webhook` | Can manage webhooks |

### Rotating Keys

Regularly rotate your API keys for security:

1. **Create** a new API key
2. **Update** your applications to use the new key
3. **Test** that everything works correctly
4. **Delete** the old key

## Error Responses

### Invalid API Key

```json
{
  "success": false,
  "error": {
    "code": "INVALID_API_KEY",
    "message": "The provided API key is invalid",
    "details": {
      "key_id": "key_1234567890"
    }
  }
}
```

### Expired API Key

```json
{
  "success": false,
  "error": {
    "code": "EXPIRED_API_KEY",
    "message": "The API key has expired",
    "details": {
      "expired_at": "2024-01-01T00:00:00Z"
    }
  }
}
```

### Missing API Key

```json
{
  "success": false,
  "error": {
    "code": "MISSING_API_KEY",
    "message": "API key is required",
    "details": {
      "header": "Authorization"
    }
  }
}
```

## Best Practices

### Security

- **Never commit API keys** to version control
- **Use environment variables** for configuration
- **Rotate keys regularly** (every 90 days)
- **Monitor key usage** for suspicious activity
- **Use different keys** for different environments

### Rate Limiting

- **Respect rate limits** to avoid 429 errors
- **Implement exponential backoff** for retries
- **Monitor usage** to stay within limits
- **Use appropriate timeouts** for requests

### Error Handling

```javascript
async function makeAPIRequest(endpoint, data) {
  try {
    const response = await fetch(`https://api.example.com/v1/${endpoint}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.API_KEY}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) {
      const error = await response.json();
      
      switch (response.status) {
        case 401:
          throw new Error('Invalid API key. Please check your credentials.');
        case 403:
          throw new Error('Access denied. Check your API key permissions.');
        case 429:
          throw new Error('Rate limit exceeded. Please try again later.');
        default:
          throw new Error(`API Error: ${error.error.message}`);
      }
    }

    return await response.json();
  } catch (error) {
    console.error('API request failed:', error.message);
    throw error;
  }
}
```

## Next Steps

- [Rate Limits](rate-limits.md) - Understand usage limits
- [Error Codes](../api-reference/errors.md) - Complete error reference
- [Best Practices](../guides/best-practices.md) - Security recommendations
- [SDKs](../guides/sdks.md) - Official client libraries 