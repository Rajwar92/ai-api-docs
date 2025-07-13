# JavaScript Examples

Learn how to integrate our AI-powered API into your JavaScript applications with these comprehensive examples.

## Setup

### Browser (ES6 Modules)

```html
<!DOCTYPE html>
<html>
<head>
    <title>AI API Example</title>
</head>
<body>
    <div id="output"></div>
    
    <script type="module">
        import { APIClient } from 'https://cdn.example.com/api-client.js';
        
        const client = new APIClient('your-api-key');
        // Your code here
    </script>
</body>
</html>
```

### Node.js

```bash
npm install @example/api-client
```

```javascript
const { APIClient } = require('@example/api-client');
// or
import { APIClient } from '@example/api-client';
```

## Basic Usage

### Initialize the Client

```javascript
const client = new APIClient('your-api-key', {
    baseURL: 'https://api.example.com/v1',
    timeout: 30000,
    retries: 3
});
```

### Generate Text

```javascript
async function generateText() {
    try {
        const response = await client.generate({
            prompt: "Write a short story about a robot learning to paint",
            model: "gpt-4",
            max_tokens: 300,
            temperature: 0.7
        });
        
        console.log('Generated text:', response.content);
        return response;
    } catch (error) {
        console.error('Error generating text:', error.message);
        throw error;
    }
}

// Usage
generateText();
```

### Generate Images

```javascript
async function generateImage() {
    try {
        const response = await client.generateImage({
            prompt: "A serene lake at sunset with mountains in the background",
            model: "dall-e-3",
            size: "1024x1024",
            quality: "standard"
        });
        
        console.log('Image URL:', response.url);
        return response;
    } catch (error) {
        console.error('Error generating image:', error.message);
        throw error;
    }
}
```

### Analyze Text

```javascript
async function analyzeText() {
    try {
        const response = await client.analyze({
            text: "I absolutely love this new AI technology! It's amazing.",
            tasks: ["sentiment", "entities", "keywords"],
            language: "en"
        });
        
        console.log('Sentiment:', response.sentiment);
        console.log('Entities:', response.entities);
        console.log('Keywords:', response.keywords);
        return response;
    } catch (error) {
        console.error('Error analyzing text:', error.message);
        throw error;
    }
}
```

## Advanced Examples

### Chat Application

```javascript
class ChatBot {
    constructor(apiKey) {
        this.client = new APIClient(apiKey);
        this.conversation = [];
    }
    
    async sendMessage(message) {
        // Add user message to conversation
        this.conversation.push({
            role: 'user',
            content: message
        });
        
        try {
            const response = await this.client.chat({
                messages: this.conversation,
                model: "gpt-4",
                max_tokens: 150
            });
            
            // Add AI response to conversation
            this.conversation.push({
                role: 'assistant',
                content: response.content
            });
            
            return response.content;
        } catch (error) {
            console.error('Chat error:', error.message);
            throw error;
        }
    }
    
    clearConversation() {
        this.conversation = [];
    }
}

// Usage
const bot = new ChatBot('your-api-key');

bot.sendMessage("Hello! How are you?")
    .then(response => console.log('Bot:', response))
    .catch(error => console.error('Error:', error));
```

### Content Generator

```javascript
class ContentGenerator {
    constructor(apiKey) {
        this.client = new APIClient(apiKey);
    }
    
    async generateBlogPost(topic, style = 'informative') {
        const prompt = `Write a comprehensive blog post about ${topic} in a ${style} style. 
                       Include an introduction, main points, and conclusion.`;
        
        try {
            const response = await this.client.generate({
                prompt,
                model: "gpt-4",
                max_tokens: 800,
                temperature: 0.7
            });
            
            return response.content;
        } catch (error) {
            console.error('Error generating blog post:', error.message);
            throw error;
        }
    }
    
    async generateSocialMediaPost(topic, platform = 'twitter') {
        const maxLength = platform === 'twitter' ? 280 : 2200;
        const prompt = `Create a ${platform} post about ${topic}. Keep it under ${maxLength} characters.`;
        
        try {
            const response = await this.client.generate({
                prompt,
                model: "gpt-4",
                max_tokens: 100,
                temperature: 0.8
            });
            
            return response.content;
        } catch (error) {
            console.error('Error generating social media post:', error.message);
            throw error;
        }
    }
}

// Usage
const generator = new ContentGenerator('your-api-key');

generator.generateBlogPost('artificial intelligence', 'educational')
    .then(post => console.log('Blog post:', post));

generator.generateSocialMediaPost('AI trends', 'linkedin')
    .then(post => console.log('LinkedIn post:', post));
```

### Real-time Translation

```javascript
class Translator {
    constructor(apiKey) {
        this.client = new APIClient(apiKey);
    }
    
    async translate(text, targetLanguage, sourceLanguage = 'auto') {
        const prompt = `Translate the following text to ${targetLanguage}${sourceLanguage !== 'auto' ? ` from ${sourceLanguage}` : ''}: "${text}"`;
        
        try {
            const response = await this.client.generate({
                prompt,
                model: "gpt-4",
                max_tokens: 200,
                temperature: 0.3
            });
            
            return response.content;
        } catch (error) {
            console.error('Translation error:', error.message);
            throw error;
        }
    }
    
    async detectLanguage(text) {
        const prompt = `Detect the language of this text and respond with only the language name: "${text}"`;
        
        try {
            const response = await this.client.generate({
                prompt,
                model: "gpt-4",
                max_tokens: 10,
                temperature: 0.1
            });
            
            return response.content.trim();
        } catch (error) {
            console.error('Language detection error:', error.message);
            throw error;
        }
    }
}

// Usage
const translator = new Translator('your-api-key');

translator.translate("Hello, how are you?", "Spanish")
    .then(translation => console.log('Translation:', translation));

translator.detectLanguage("Bonjour, comment allez-vous?")
    .then(language => console.log('Detected language:', language));
```

## Error Handling

### Comprehensive Error Handling

```javascript
class APIError extends Error {
    constructor(message, code, details) {
        super(message);
        this.name = 'APIError';
        this.code = code;
        this.details = details;
    }
}

async function handleAPIRequest(requestFn) {
    try {
        return await requestFn();
    } catch (error) {
        if (error.response) {
            // Server responded with error status
            const { status, data } = error.response;
            
            switch (status) {
                case 401:
                    throw new APIError('Invalid API key', 'AUTH_ERROR', data);
                case 429:
                    throw new APIError('Rate limit exceeded', 'RATE_LIMIT', data);
                case 400:
                    throw new APIError('Invalid request', 'BAD_REQUEST', data);
                case 500:
                    throw new APIError('Server error', 'SERVER_ERROR', data);
                default:
                    throw new APIError(`HTTP ${status}`, 'HTTP_ERROR', data);
            }
        } else if (error.request) {
            // Network error
            throw new APIError('Network error', 'NETWORK_ERROR', error.request);
        } else {
            // Other error
            throw new APIError(error.message, 'UNKNOWN_ERROR', error);
        }
    }
}

// Usage
handleAPIRequest(() => client.generate({
    prompt: "Test prompt",
    model: "gpt-4"
}))
.then(response => console.log('Success:', response))
.catch(error => {
    console.error(`${error.name}: ${error.message}`);
    if (error.details) {
        console.error('Details:', error.details);
    }
});
```

## Rate Limiting

### Implement Rate Limiting

```javascript
class RateLimitedClient {
    constructor(apiKey, requestsPerMinute = 60) {
        this.client = new APIClient(apiKey);
        this.requestsPerMinute = requestsPerMinute;
        this.requests = [];
    }
    
    async makeRequest(requestFn) {
        // Clean old requests
        const now = Date.now();
        this.requests = this.requests.filter(time => now - time < 60000);
        
        // Check rate limit
        if (this.requests.length >= this.requestsPerMinute) {
            const oldestRequest = this.requests[0];
            const waitTime = 60000 - (now - oldestRequest);
            throw new Error(`Rate limit exceeded. Try again in ${Math.ceil(waitTime / 1000)} seconds.`);
        }
        
        // Add current request
        this.requests.push(now);
        
        // Make the actual request
        return await requestFn();
    }
    
    async generate(options) {
        return this.makeRequest(() => this.client.generate(options));
    }
    
    async generateImage(options) {
        return this.makeRequest(() => this.client.generateImage(options));
    }
}

// Usage
const rateLimitedClient = new RateLimitedClient('your-api-key', 30);

// This will respect the rate limit
for (let i = 0; i < 5; i++) {
    rateLimitedClient.generate({
        prompt: `Request ${i + 1}`,
        model: "gpt-4"
    })
    .then(response => console.log(`Request ${i + 1} completed`))
    .catch(error => console.error(`Request ${i + 1} failed:`, error.message));
}
```

## Next Steps

- [Python Examples](python.md) - Examples in Python
- [cURL Examples](curl.md) - Command line examples
- [API Reference](../api-reference/index.md) - Complete API documentation
- [Best Practices](../guides/best-practices.md) - Recommended patterns 