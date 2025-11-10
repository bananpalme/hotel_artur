import streamlit as st
import requests
import pandas as pd

GATEWAY_URL = "http://api_gateway:5000"

st.title("Hotel Artur - Employee & Work Management")

st.header("View Employees")
if st.button("Load Employees"):
    res = requests.get(f"{GATEWAY_URL}/employees")
    if res.status_code == 200:
        employees = res.json()
        if employees:
            df_employees = pd.DataFrame(employees)
            st.dataframe(df_employees)
        else:
            st.info("No employees found.")
    else:
        st.error("Failed to fetch employees from API Gateway.")

st.header("Register New Employee")
with st.form("employee_form"):
    name = st.text_input("Name")
    department = st.text_input("Department")
    submitted = st.form_submit_button("Register Employee")

    if submitted:
        if not name or not department:
            st.warning("Please fill out all fields.")
        else:
            data = {"name": name, "department": department}
            res = requests.post(f"{GATEWAY_URL}/employees", json=data)
            if res.status_code == 201:
                st.success("Employee registered successfully!")
            else:
                st.error(f"Error: {res.json().get('message', 'Unknown error')}")

st.header("View Work Assignments")
if st.button("Load Work Assignments"):
    res = requests.get(f"{GATEWAY_URL}/work")
    if res.status_code == 200:
        work = res.json()
        if work:
            df_work = pd.DataFrame(work)
            st.dataframe(df_work)
        else:
            st.info("No work assignments found.")
    else:
        st.error("Failed to fetch work assignments.")

st.header("Assign Task to Employee")
with st.form("task_form"):
    emp_res = requests.get(f"{GATEWAY_URL}/employees")
    employees = emp_res.json() if emp_res.status_code == 200 else []

    employee_options = {f"{e['name']} (ID: {e['id']})": e['id'] for e in employees}

    selected_emp = st.selectbox("Select Employee", options=list(employee_options.keys()))
    task = st.text_input("Task Description")
    submitted_task = st.form_submit_button("Assign Task")

    if submitted_task:
        if not task or not selected_emp:
            st.warning("Please select an employee and enter a task.")
        else:
            data = {
                "employee_id": employee_options[selected_emp],
                "task": task
            }
            res = requests.post(f"{GATEWAY_URL}/work", json=data)
            try:
                res_json = res.json()
            except ValueError:
                res_json = {"message": f"Invalid response: {res.text}"}

            if res.status_code == 201:
                st.success("Task assigned successfully!")
            else:
                st.error(f"Error: {res_json.get('message', 'Unknown error')}")
