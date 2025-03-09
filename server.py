from flask import Flask, request, jsonify
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend requests

db = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    database="world",
    ssl={"ssl": {}},  # Enable SSL to support caching_sha2_password
)

cursor = db.cursor()

@app.route("/")
def home():
    return "API is running!"

# API to submit form data
@app.route("/submit", methods=["POST"])
def submit_form():
    data = request.json
    sname, place, salary = data.get("sname"), data.get("place"), data.get("salary")

    sql = "INSERT INTO form (sname, place, salary) VALUES (%s, %s, %s)"
    values = (sname, place, salary)

    try:
        cursor.execute(sql, values)
        db.commit()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


if __name__ == "__main__":
    print("Flask API is running on http://127.0.0.1:5000/")
    app.run(debug=True)
