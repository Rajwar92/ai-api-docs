# Postman Collection

## API Testing with Postman

We provide a comprehensive Postman collection to help you test our API endpoints easily.

### Download Collection

You can download our Postman collection from the following location:
- [Postman Collection](../postman/ai-api-docs.postman_collection.json)

### Import Instructions

1. Download the collection file
2. Open Postman
3. Click "Import" in the top left
4. Drag and drop the collection file or click "Upload Files"
5. The collection will be imported with all endpoints and examples

### Environment Variables

To use the collection effectively, set up these environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `base_url` | Your API base URL | `https://api.example.com` |
| `api_key` | Your API key | `sk_test_1234567890` |
| `access_token` | OAuth access token | `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...` |

### Setting Up Environment

1. In Postman, click the "Environments" tab
2. Click "New" to create a new environment
3. Add the variables listed above
4. Save the environment
5. Select your environment from the dropdown in the top right

### Collection Structure

Our Postman collection is organized into the following folders:

#### Authentication
- Login
- Refresh Token
- Logout

#### Shipments
- List Shipments
- Create Shipment
- Get Shipment
- Update Shipment
- Delete Shipment

#### Users
- List Users
- Create User
- Get User
- Update User
- Delete User

### Pre-request Scripts

Some requests include pre-request scripts that automatically:
- Set authentication headers
- Generate timestamps
- Format request bodies

### Tests

Each request includes tests that:
- Verify response status codes
- Validate response schemas
- Extract values for use in subsequent requests

### Running the Collection

1. Import the collection and environment
2. Set up your environment variables
3. Run the collection using the "Run" button
4. Review the test results in the collection runner

### Troubleshooting

If you encounter issues:

1. **Authentication Errors**: Verify your API key and access token
2. **Rate Limiting**: Check our [rate limits](../getting-started/rate-limits.md)
3. **Network Issues**: Ensure your base URL is correct
4. **Schema Validation**: Update the collection if our API has changed

### Support

For help with the Postman collection:
- Check our [FAQ](../support/faq.md)
- Review our [API documentation](../api-reference/index.md)
- [Contact support](../support/contact.md) 