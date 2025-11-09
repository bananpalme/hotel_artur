from flask import Flask, jsonify, request

app = Flask(__name__)

work_db = [
    {"employee_id": 1, "task": "cleaning room 1"},
    {"employee_id": 1, "task": "cleaning room 2"}
]

@app.route("/work", methods=["GET"])
def view_work():
    return jsonify(work_db)

@app.route("/work", methods=["POST"])
def assign_task():
    data = request.get_json()
    employee_id = data.get("employee_id")
    task = data.get("task")

    if not employee_id or not task:
        return jsonify({"message": "employee_id and task are required"}), 400

    new_assignment = {"employee_id": employee_id, "task": task}
    work_db.append(new_assignment)
    return jsonify({"message": "Task assigned successfully"}), 201

app.run(host="0.0.0.0", port=5002)
