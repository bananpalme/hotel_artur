from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

employees_db = [{"id": 1, "name": "John", "department": "cleaning"}]

@app.route("/employees", methods=["GET"])
def view_employees():
    return jsonify(employees_db)

@app.route("/employees", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    department = data.get("department")

    if not name or not department:
        return jsonify({"message": "Name and department are required"}), 400
    
    new_employee = {
        "id": len(employees_db) + 1,
        "name": name,
        "department": department,
    }

    employees_db.append(new_employee)
    return jsonify({"message": f"Employee registered successfully"}), 201

app.run(host="0.0.0.0", port=5001)