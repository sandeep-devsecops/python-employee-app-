from flask import Flask, jsonify, render_template

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Sandeep", "role": "DevOps Engineer"},
    {"id": 2, "name": "Rahul", "role": "Python Developer"},
    {"id": 3, "name": "Priya", "role": "Data Analyst"}
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/employees")
def get_employees():
    return jsonify(employees)


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "application": "Employee Management API"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
