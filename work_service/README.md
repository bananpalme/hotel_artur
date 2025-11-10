# Work Service API

The Work Service provides a REST API for managing work assignments for work.

---

## Base URL

http://localhost:5002

---

## Endpoints

### 1. GET `/work`

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

### 2. POST `/work`

### Request body example

```JSON
{
  "employee_id": 1,
  "task": "clean room 2"
}
```