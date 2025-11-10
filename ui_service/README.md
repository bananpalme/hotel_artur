# UI Service

The UI Service provides a simple web interface for interacting with the system.  
It communicates with the API Gateway to manage employees and assign work tasks.

Built using **Streamlit**.

---

## Base URL

After starting the service:

http://localhost:8501

---

## Features

1. **View Employees**  
   Displays a list of all registered employees retrieved from the API Gateway.

2. **Register New Employee**  
   Allows adding a new employee by entering their name and department.

3. **Assign Work**  
   Lets you assign a task (e.g., "clean room 1") to an existing employee.

4. **View Assigned Work**  
   Shows all tasks assigned to employees.

---

The UI connects to the API Gateway using its internal hostname:

```python
GATEWAY_URL = "http://api_gateway:5000"
```

If running locally (without Docker), change it to:

```python
GATEWAY_URL = "http://localhost:5000"
```

and run with 


```bash
streamlit run app.py
```