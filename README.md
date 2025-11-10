# Hotel Kong Artur 

- An **Employee Service** for managing employees.
- A **Work Service** for assigning tasks.
- An **API Gateway** that routes service requests.
- A **UI Service** interface for above mentioned services.

From the project root, run:

```bash
docker-compose up --build

```

or run each service locally.

## **VERY IMPORTANT ABOUT RUNNING LOCALLY**

change in api_gateway

```python
EMPLOYEE_SERVICE_URL = "http://employee_service:5001/employees"
WORK_SERVICE_URL = "http://work_service:5002/work"
```

to

```python
EMPLOYEE_SERVICE_URL = "http://localhost:5001/employees"
WORK_SERVICE_URL = "http://localhost:5002/work"
```

**do the same in ui_service and change api_gateway to**

```python
GATEWAY_URL = "http://localhost:5000"
```

then go to their folder and run:

```bash
python3 app.py

```

and for the ui service run:

```bash
streamlit run app.py
```

do this for all parts and see the ui on http://localhost:8501