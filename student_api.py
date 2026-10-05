from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

from flask import Flask, request, jsonify
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")



with open(r"C:\Users\omnad\Desktop\Python notes\Daily challenges\n8n project\student form validation\applications.json", "r") as file:
    applications = json.load(file)

@app.route("/application", methods=["POST"])
def application():
    key = request.headers.get("X-API-Key")

    if key != API_KEY:
        return jsonify({
            "message": "Invalid API key"
        }), 401

    data = request.get_json()
    if not data:
        return jsonify({
            "message": "No application data provided"
        }), 400
    applications.append(data)
    with open(r"C:\Users\omnad\Desktop\Python notes\Daily challenges\n8n project\student form validation\applications.json", "w") as file:
        json.dump(applications, file, indent=4)
    print("Received application:")
    print(data)

    return jsonify({
        "message": "Application received successfully",
        "data": data
    })

@app.route("/applications", methods=["GET"])
def get_applications():
    return jsonify(applications)

@app.route("/application/<application_id>", methods=["GET"])
def get_application(application_id):

    for application in applications:
        if application["application_id"] == application_id:
            return jsonify(application)

    return jsonify({
        "message": "Application not found"
    }), 404

@app.route("/application/<application_id>", methods=["DELETE"])
def delete_application(application_id):

    for application in applications:
        if application["application_id"] == application_id:
            applications.remove(application)

            with open(r"C:\Users\omnad\Desktop\Python notes\Daily challenges\n8n project\student form validation\applications.json", "w") as file:
                json.dump(applications, file, indent=4)

            return jsonify({
                "message": "Application deleted successfully"
            })

    return jsonify({
        "message": "Application not found"
    }), 404

@app.route("/application/<application_id>", methods=["PUT"])
def update_application(application_id):

    data = request.get_json()

    for application in applications:
        if application["application_id"] == application_id:

            application.update(data)

            with open("applications.json", "w") as file:
                json.dump(applications, file, indent=4)

            return jsonify({
                "message": "Application updated successfully",
                "data": application
            })

    return jsonify({
        "message": "Application not found"
    }), 404

if __name__ == "__main__":
    app.run(debug=True)