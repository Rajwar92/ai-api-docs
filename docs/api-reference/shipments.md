# Shipments API

This page provides documentation for the Shipments API endpoints.

## API Documentation

For interactive API documentation, please visit our [Swagger UI](/tools/swagger.md) page.

## Endpoints

### Get Shipments

Retrieve a list of shipments.

**Endpoint:** `GET /api/v1/shipments`

**Parameters:**
- `page` (optional): Page number for pagination
- `limit` (optional): Number of items per page (max 100)

**Response:**
```json
{
  "data": [
    {
      "id": "ship_123",
      "tracking_number": "1Z999AA1234567890",
      "status": "in_transit",
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 20,
    "total": 150
  }
}
```

### Create Shipment

Create a new shipment.

**Endpoint:** `POST /api/v1/shipments`

**Request Body:**
```json
{
  "recipient": {
    "name": "John Doe",
    "address": "123 Main St",
    "city": "New York",
    "state": "NY",
    "zip": "10001"
  },
  "package": {
    "weight": 2.5,
    "dimensions": {
      "length": 10,
      "width": 8,
      "height": 6
    }
  }
}
```

**Response:**
```json
{
  "id": "ship_123",
  "tracking_number": "1Z999AA1234567890",
  "status": "created",
  "created_at": "2024-01-15T10:30:00Z"
}
```