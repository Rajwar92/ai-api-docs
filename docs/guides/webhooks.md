# Webhooks Guide

Webhooks allow your application to receive real-time notifications from our API when certain events occur.

## What are Webhooks?

Webhooks are HTTP callbacks triggered by specific events in our system. When an event occurs (e.g., a new shipment is created), we send an HTTP POST request to your configured endpoint with event data.

## Setting Up Webhooks

1. **Create an endpoint** in your application to receive POST requests.
2. **Register your webhook URL** in the dashboard under the Webhooks section.
3. **Select the events** you want to subscribe to (e.g., shipment.created, user.updated).
4. **Save** your webhook configuration.

## Example Webhook Payload

```json
{
  "event": "shipment.created",
  "data": {
    "id": "ship_123",
    "status": "created",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "timestamp": "2024-01-15T10:30:00Z",
  "signature": "abcdef1234567890"
}
```

## Securing Webhooks

- **Validate the signature** included in the payload to ensure authenticity.
- Only accept requests from our IP addresses (see dashboard for list).
- Use HTTPS for your webhook endpoint.

## Handling Webhook Events

- Respond with HTTP 200 OK to acknowledge receipt.
- Process the event asynchronously if it requires heavy computation.
- Log all received events for auditing and debugging.

## Common Events

| Event                | Description                       |
|----------------------|-----------------------------------|
| shipment.created     | A new shipment was created        |
| shipment.updated     | A shipment was updated            |
| user.created         | A new user was created            |
| user.updated         | A user was updated                |

## Troubleshooting

- If your endpoint is down or returns an error, we'll retry delivery several times with exponential backoff.
- Check your server logs for incoming webhook requests and errors.

## More Information

- [API Reference](../api-reference/index.md)
- [Contact Support](../support/contact.md) 