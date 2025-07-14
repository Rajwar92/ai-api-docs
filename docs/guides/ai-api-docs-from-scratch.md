# Step-by-Step AI Prompts to Create API Documentation from Zero

This guide provides a sequence of AI prompts to generate comprehensive API documentation, even if you're starting with minimal information. Replace placeholders (like `<API_NAME>`) with your specifics.

---

## **Phase 1: Gather Basic API Information**
**Goal:** Extract foundational details about the API.

### **Prompt 1: Identify Core API Purpose**
```
"Act as an API technical writer. List the key questions I need to answer to document `<API_NAME>`. Focus on: 
- Primary use cases
- Target audience (developers, internal teams, etc.)
- Authentication methods
- Rate limits/quotas
- Error handling approach
- Data formats (JSON/XML)."
```

**Example Output:**  
> *1. What problem does this API solve?  
> 2. Is authentication via API keys, OAuth, or tokens?  
> 3. Are there HTTP status codes for errors like 429 (rate limits)?*

---

## **Phase 2: Generate Endpoint Structure**
**Goal:** Map out API endpoints and methods.

### **Prompt 2: Define Resources and Actions**
```
"Generate a REST API endpoint table for `<API_NAME>` with:  
- HTTP methods (GET/POST/PUT/DELETE)  
- Resource paths (e.g., `/users/{id}`)  
- Short descriptions.  

Example format:  
| Method | Path         | Description                  |  
|--------|-------------|------------------------------|  
| GET    | /users      | Fetch all registered users   |"
```

**Placeholder Output:**  
| Method | Path          | Description                     |  
|--------|--------------|---------------------------------|  
| POST   | `/auth/login` | Authenticate user with email/pw |  

---

## **Phase 3: Document Request/Response Examples**
**Goal:** Create realistic payload and response samples.

### **Prompt 3: Request/Response Templates**
```
"Generate a JSON request/response example for `<ENDPOINT_PATH>` in `<API_NAME>`. Include:  
- Required headers (e.g., `Authorization: Bearer <token>`)  
- Sample request body  
- Success response (200 OK) with mock data  
- Error response (e.g., 400 Bad Request)."
```

**Example Output:**  
```json
// REQUEST (POST /orders)
{
  "product_id": "prod_123",
  "quantity": 2
}

// RESPONSE (201 Created)
{
  "order_id": "ord_abc",
  "status": "pending"
}
```

---

## **Phase 4: Add Usage Scenarios**
**Goal:** Clarify real-world API use cases.

### **Prompt 4: Use Case Narratives**
```
"Write 3 practical scenarios for `<API_NAME>` showing how to:  
1. Perform `<COMMON_TASK_1>` (e.g., ‘Create a user profile’).  
2. Handle `<EDGE_CASE>` (e.g., ‘Retry failed payments’).  
3. Chain endpoints (e.g., ‘Fetch user → Update permissions’)."
```

**Example Scenario:**  
> **Scenario 1: Check Inventory**  
> 1. Call `GET /inventory?product_id=123`  
> 2. If `stock_level > 0`, proceed to `/checkout`.  

---

## **Phase 5: Finalize Documentation**
**Goal:** Compile a polished doc with all sections.

### **Prompt 5: Full Documentation Template**
```
"Generate a markdown template for `<API_NAME>` covering:  
1. **Overview** (2-3 sentences)  
2. **Quickstart** (curl example)  
3. **Endpoints** (table from Phase 2)  
4. **Examples** (from Phase 3)  
5. **Troubleshooting** (common errors)."
```

**Template Snippet:**  
```markdown
## **Quickstart**  
```bash
curl -X GET https://api.example.com/v1/users \
  -H "Authorization: Bearer YOUR_TOKEN"
```
```

---

## **GraphQL and WebSocket API Documentation**

If your API uses GraphQL or WebSockets, you can adapt the prompt-driven approach as follows:

### **GraphQL Prompts**

**Prompt:**
```
"Act as an API technical writer. List the key questions to document `<GRAPHQL_API_NAME>`, focusing on:
- Main queries and mutations
- Schema structure (types, fields, relationships)
- Authentication and authorization
- Error handling and response format
- Example queries and responses."
```

**Example Output:**
> 1. What are the main queries and mutations available?
> 2. What does the schema look like for each resource?
> 3. How do you authenticate GraphQL requests?

**Prompt for Example Query:**
```
"Generate a sample GraphQL query for `<RESOURCE>` and its expected response."
```

**Example:**
```graphql
# QUERY
query GetUser {
  user(id: "123") {
    id
    name
    email
  }
}

# RESPONSE
{
  "data": {
    "user": {
      "id": "123",
      "name": "Alice",
      "email": "alice@example.com"
    }
  }
}
```

---

### **WebSocket Prompts**

**Prompt:**
```
"Document the WebSocket API for `<API_NAME>`, covering:
- Connection URL and protocol
- Authentication (if any)
- Message formats (subscribe, publish, event types)
- Example send/receive messages
- Error and disconnect handling."
```

**Example Output:**
> 1. Connect to `wss://api.example.com/ws`
> 2. Authenticate by sending `{ "type": "auth", "token": "<TOKEN>" }`
> 3. Subscribe to events: `{ "type": "subscribe", "channel": "orders" }`

**Prompt for Example Message:**
```
"Provide a sample WebSocket message to subscribe to order updates, and a sample event message received."
```

**Example:**
```json
// SUBSCRIBE
{
  "type": "subscribe",
  "channel": "orders"
}

// EVENT
{
  "type": "order_update",
  "order_id": "ord_abc",
  "status": "shipped"
}
```

---

## **Bonus: AI Tips for Better Prompts**
- Use **"Act as a [role]"** to guide tone (e.g., *"Act as a senior backend developer"*).  
- Specify **output format** (e.g., *"Generate a table comparing endpoints"*).  
- Iterate: Refine prompts with *"Expand the section about error codes"*.

---

**Next Steps:**  
1. Replace all placeholders (`<LIKE_THIS>`) with your API details.  
2. Use tools like [Swagger](https://swagger.io/) or [Postman](https://www.postman.com/) to test examples.  
3. Share drafts with developers for feedback.

---

This template balances structure with flexibility. Customize prompts further based on your API’s complexity (e.g., add GraphQL or WebSocket specifics). 