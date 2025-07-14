# New API Endpoint

> _This is a template for documenting a new API endpoint. Replace the placeholders with actual endpoint details._

## Endpoint

`POST /api/v1/new-endpoint`

## Description

Describe what this endpoint does, its purpose, and any important notes.

## Request

### Headers
- `Authorization: Bearer YOUR_API_KEY`
- `Content-Type: application/json`

### Body Example
```json
{
  "parameter1": "value1",
  "parameter2": 123
}
```

### Parameters
| Name         | Type   | Required | Description                |
|--------------|--------|----------|----------------------------|
| parameter1   | string | Yes      | Description of parameter1   |
| parameter2   | int    | No       | Description of parameter2   |

## Response

### Success
```json
{
  "success": true,
  "data": {
    "id": "new_123",
    "result": "Some result"
  }
}
```

### Error
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Error message"
  }
}
```

## Example Usage

=== "cURL"
    ```bash
    curl -X POST https://api.example.com/v1/new-endpoint \
      -H "Authorization: Bearer YOUR_API_KEY" \
      -H "Content-Type: application/json" \
      -d '{ "parameter1": "value1", "parameter2": 123 }'
    ```

=== "Python"
    ```python
    import requests
    response = requests.post(
        'https://api.example.com/v1/new-endpoint',
        headers={
            'Authorization': 'Bearer YOUR_API_KEY',
            'Content-Type': 'application/json'
        },
        json={
            'parameter1': 'value1',
            'parameter2': 123
        }
    )
    print(response.json())
    ```

## See Also
- [API Reference](index.md)
- [Error Codes](errors.md)
