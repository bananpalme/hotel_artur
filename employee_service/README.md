# Employee Service API

The Employee Service provides a simple REST API for managing employees.

---

## Base URL

http://localhost:5001

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