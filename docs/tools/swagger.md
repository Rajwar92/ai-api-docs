# Swagger UI

## Interactive API Documentation

Our API documentation is available in multiple formats for your convenience.

### OpenAPI Specification

You can download our OpenAPI specification file:
- [OpenAPI 3.0 Specification](../swagger/openapi.yaml)

### Interactive Documentation

For the best experience, we recommend using one of these tools:

1. **Swagger Editor**: Copy the OpenAPI specification and paste it into [Swagger Editor](https://editor.swagger.io/)
2. **Swagger UI**: Use the specification with any Swagger UI instance
3. **Postman**: Import the OpenAPI specification into [Postman](https://www.postman.com/)

### API Endpoints Overview

Our API provides the following main endpoints:

#### Authentication
- `POST /auth/login` - Authenticate user
- `POST /auth/refresh` - Refresh access token
- `POST /auth/logout` - Logout user

#### Shipments
- `GET /api/v1/shipments` - List shipments
- `POST /api/v1/shipments` - Create shipment
- `GET /api/v1/shipments/{id}` - Get shipment details
- `PUT /api/v1/shipments/{id}` - Update shipment
- `DELETE /api/v1/shipments/{id}` - Delete shipment

#### Users
- `GET /api/v1/users` - List users
- `POST /api/v1/users` - Create user
- `GET /api/v1/users/{id}` - Get user details
- `PUT /api/v1/users/{id}` - Update user
- `DELETE /api/v1/users/{id}` - Delete user

### Testing the API

You can test our API endpoints using:

1. **cURL examples** - See our [cURL examples](../examples/curl.md)
2. **JavaScript SDK** - See our [JavaScript examples](../examples/javascript.md)
3. **Python SDK** - See our [Python examples](../examples/python.md)
4. **Postman Collection** - See our [Postman collection](../tools/postman.md)

### Rate Limits

Please be aware of our [rate limits](../getting-started/rate-limits.md) when testing the API.

### Support

If you encounter any issues with the API, please check our [FAQ](../support/faq.md) or [contact support](../support/contact.md). 