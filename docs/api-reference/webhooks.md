# Webhook Events Reference

This page documents all webhook events available in our API.

## Available Events

| Event                | Description                       |
|----------------------|-----------------------------------|
| shipment.created     | A new shipment was created        |
| shipment.updated     | A shipment was updated            |
| user.created         | A new user was created            |
| user.updated         | A user was updated                |

## Event Payload Example

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

_See the [Webhooks Guide](../guides/webhooks.md) for setup instructions._ 