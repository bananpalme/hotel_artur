from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

EMPLOYEE_SERVICE_URL = "http://employee_service:5001/employees"
WORK_SERVICE_URL = "http://work_service:5002/work"

@app.route("/employees", methods=["GET", "POST"])
def employees():
    if request.method == "GET":
        res = requests.get(f"{EMPLOYEE_SERVICE_URL}")
        return jsonify(res.json()), res.status_code
    elif request.method == "POST":
        data = request.get_json()
        res = requests.post(f"{EMPLOYEE_SERVICE_URL}", json=data)
        return jsonify(res.json()), res.status_code

@app.route("/work", methods=["GET", "POST"])
def work():
    if request.method == "GET":
        res = requests.get(f"{WORK_SERVICE_URL}")
        return jsonify(res.json()), res.status_code
    elif request.method == "POST":
        data = request.get_json()
        res = requests.post(f"{WORK_SERVICE_URL}", json=data)
        return jsonify(res.json()), res.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
