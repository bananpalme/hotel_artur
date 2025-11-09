from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

EMPLOYEE_SERVICE_URL = "http://localhost:5001"
WORK_SERVICE_URL = "http://localhost:5002"

@app.route("/employees", methods=["GET", "POST"])
def employees():
    if request.method == "GET":
        res = requests.get(f"{EMPLOYEE_SERVICE_URL}/employees")
        return jsonify(res.json()), res.status_code
    elif request.method == "POST":
        data = request.get_json()
        res = requests.post(f"{EMPLOYEE_SERVICE_URL}/employees", json=data)
        return jsonify(res.json()), res.status_code

@app.route("/work", methods=["GET", "POST"])
def work():
    if request.method == "GET":
        res = requests.get(f"{WORK_SERVICE_URL}/work")
        return jsonify(res.json()), res.status_code
    elif request.method == "POST":
        data = request.get_json()
        res = requests.post(f"{WORK_SERVICE_URL}/work", json=data)
        return jsonify(res.json()), res.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
