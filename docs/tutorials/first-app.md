# Building Your First App

This tutorial will guide you through building your first application using our AI-powered API.

## Prerequisites
- An API key (get one from your dashboard)
- Basic programming knowledge (JavaScript, Python, or cURL)

## Step 1: Set Up Your Project

Choose your preferred language and set up a new project directory. Install the required SDK or dependencies.

### JavaScript/Node.js
```bash
npm install @example/api-client
```

### Python
```bash
pip install example-api-client
```

## Step 2: Initialize the API Client

### JavaScript
```javascript
const { APIClient } = require('@example/api-client');
const client = new APIClient('your-api-key');
```

### Python
```python
import api_client
client = api_client.Client('your-api-key')
```

## Step 3: Make Your First API Call

Let's generate some text using the API.

### JavaScript
```javascript
const response = await client.generate({
  prompt: 'Write a welcome message for my app',
  model: 'gpt-4',
  max_tokens: 100
});
console.log(response.content);
```

### Python
```python
response = client.generate(prompt='Write a welcome message for my app', model='gpt-4', max_tokens=100)
print(response.content)
```

## Step 4: Handle Errors

Always handle errors gracefully in your code.

### JavaScript
```javascript
try {
  // ... API call ...
} catch (error) {
  console.error('API Error:', error.message);
}
```

### Python
```python
try:
    # ... API call ...
except Exception as e:
    print('API Error:', str(e))
```

## Step 5: Next Steps
- Explore more endpoints in the [API Reference](../api-reference/index.md)
- Try out [code examples](../examples/javascript.md)
- Learn about [rate limits](../getting-started/rate-limits.md)
- Check our [FAQ](../support/faq.md) for help 