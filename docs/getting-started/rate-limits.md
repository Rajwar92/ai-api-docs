# Rate Limits

Learn about our API rate limits and how to handle them effectively.

## Overview

Our API implements rate limiting to ensure fair usage and maintain service quality for all users.

## Rate Limit Tiers

| Plan | Requests per Minute | Requests per Hour | Requests per Day |
|------|-------------------|------------------|------------------|
| Free | 60 | 1,000 | 10,000 |
| Pro | 300 | 10,000 | 100,000 |
| Enterprise | Custom | Custom | Custom |

## Rate Limit Headers

Every API response includes rate limit information in the headers:

```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1640995200
```

- **X-RateLimit-Limit**: Maximum requests allowed in the current window
- **X-RateLimit-Remaining**: Number of requests remaining in the current window
- **X-RateLimit-Reset**: Unix timestamp when the rate limit resets

## Handling Rate Limits

### HTTP 429 Response

When you exceed the rate limit, you'll receive a 429 status code:

```json
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Try again in 60 seconds.",
    "details": {
      "retry_after": 60,
      "limit": 60,
      "reset_time": 1640995200
    }
  }
}
```

### Exponential Backoff

Implement exponential backoff for retries:

```javascript
async function makeRequestWithRetry(endpoint, data, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const response = await fetch(`https://api.example.com/v1/${endpoint}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${process.env.API_KEY}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      if (response.status === 429) {
        const error = await response.json();
        const retryAfter = error.error.details.retry_after || Math.pow(2, attempt);
        
        console.log(`Rate limited. Retrying in ${retryAfter} seconds...`);
        await new Promise(resolve => setTimeout(resolve, retryAfter * 1000));
        continue;
      }

      return await response.json();
    } catch (error) {
      if (attempt === maxRetries) throw error;
      console.log(`Request failed. Retrying... (${attempt}/${maxRetries})`);
    }
  }
}
```

## Best Practices

### Monitor Usage

Track your rate limit usage:

```javascript
function checkRateLimit(headers) {
  const limit = headers.get('X-RateLimit-Limit');
  const remaining = headers.get('X-RateLimit-Remaining');
  const reset = headers.get('X-RateLimit-Reset');
  
  console.log(`Rate limit: ${remaining}/${limit} requests remaining`);
  console.log(`Resets at: ${new Date(reset * 1000).toISOString()}`);
  
  // Alert when usage is high
  if (parseInt(remaining) < parseInt(limit) * 0.1) {
    console.warn('Rate limit usage is high!');
  }
}
```

### Batch Requests

When possible, batch multiple operations into a single request:

```javascript
// Instead of multiple requests
const results = [];
for (const item of items) {
  const result = await api.process(item);
  results.push(result);
}

// Use batch endpoint
const results = await api.processBatch(items);
```

### Cache Responses

Cache responses to reduce API calls:

```javascript
const cache = new Map();

async function getCachedData(key, ttl = 300000) { // 5 minutes
  const cached = cache.get(key);
  if (cached && Date.now() - cached.timestamp < ttl) {
    return cached.data;
  }
  
  const data = await api.getData(key);
  cache.set(key, { data, timestamp: Date.now() });
  return data;
}
```

## Rate Limit by Endpoint

Different endpoints may have different rate limits:

| Endpoint | Rate Limit | Window |
|----------|------------|--------|
| `/generate` | 60/min | Per minute |
| `/analyze` | 120/min | Per minute |
| `/models` | 1000/min | Per minute |
| `/webhooks` | 10/min | Per minute |

## Enterprise Plans

Enterprise customers can request custom rate limits based on their needs. Contact our sales team for more information.

## Next Steps

- [Authentication](authentication.md) - Learn about API authentication
- [Error Codes](../api-reference/errors.md) - Complete error reference
- [Best Practices](../guides/best-practices.md) - Recommended patterns
- [Contact Support](../support/contact.md) - Get help with rate limits 