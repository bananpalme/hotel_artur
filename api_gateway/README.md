# API Gateway

The API Gateway acts as a single entry point for clients to interact with multiple microservices — including the Employee Service and Work Service.  
It forwards requests to the appropriate service and aggregates responses when necessary.

---

## Base URL

http://localhost:5000

---

## Endpoints

### 1. GET `/employees`

### Response example

```JSON
[
    {
        "id": 1,
        "name": "John",
        "department": "cleaning"
    }
]
```

### 2. POST `/employees`

### Request body example

```JSON
{
  "name": "Alice",
  "department": "reception"
}
```

### 3. GET `/work`

### Response example

```JSON
[
  {
    "id": 1,
    "employee_id": 1,
    "task": "clean room 1"
  }
]
```

### 4. POST `/work`

### Request body example

```JSON
{
  "employee_id": 1,
  "task": "clean room 2"
}
```