# SDKs Guide

Our API offers official SDKs for popular programming languages to make integration easy and efficient.

## Available SDKs

- **JavaScript/Node.js**: [GitHub](https://github.com/example/js-sdk)
- **Python**: [GitHub](https://github.com/example/python-sdk)
- **Go**: [GitHub](https://github.com/example/go-sdk)
- **Ruby**: [GitHub](https://github.com/example/ruby-sdk)

## Installation

### JavaScript/Node.js
```bash
npm install @example/api-client
```

### Python
```bash
pip install example-api-client
```

### Go
```bash
go get github.com/example/go-sdk
```

### Ruby
```bash
gem install example-api-client
```

## Basic Usage

### JavaScript Example
```javascript
const { APIClient } = require('@example/api-client');
const client = new APIClient('your-api-key');
const response = await client.generate({ prompt: 'Hello, world!', model: 'gpt-4' });
console.log(response.content);
```

### Python Example
```python
import api_client
client = api_client.Client('your-api-key')
response = client.generate(prompt='Hello, world!', model='gpt-4')
print(response.content)
```

## Best Practices
- Always use the latest SDK version.
- Store your API key securely (use environment variables).
- Handle errors and rate limits as described in our [Best Practices](best-practices.md).

## More Information
- [API Reference](../api-reference/index.md)
- [Contact Support](../support/contact.md) 