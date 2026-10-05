from flask import Flask, request, jsonify
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.environ.get("API_KEY")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "applications.json")


# Load applications
with open(DATA_FILE, "r") as file:
    applications = json.load(file)


# Check API key
def check_api_key():
    key = request.headers.get("X-API-Key")

    if key != API_KEY:
        return False

    return True


# POST - Create application
@app.route("/application", methods=["POST"])
def application():

    if not check_api_key():
        return jsonify({
            "message": "Invalid API key"
        }), 401

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "No application data provided"
        }), 400

    applications.append(data)

    with open(DATA_FILE, "w") as file:
        json.dump(applications, file, indent=4)

    print("Received application:")
    print(data)

    return jsonify({
        "message": "Application received successfully",
        "data": data
    })


# GET - Get all applications
@app.route("/applications", methods=["GET"])
def get_applications():

    if not check_api_key():
        return jsonify({
            "message": "Invalid API key"
        }), 401

    return jsonify(applications)


# GET - Get one application
@app.route("/application/<application_id>", methods=["GET"])
def get_application(application_id):

    if not check_api_key():
        return jsonify({
            "message": "Invalid API key"
        }), 401

    for application in applications:

        if application.get("application_id") == application_id:
            return jsonify(application)

    return jsonify({
        "message": "Application not found"
    }), 404


# DELETE - Delete application
@app.route("/application/<application_id>", methods=["DELETE"])
def delete_application(application_id):

    if not check_api_key():
        return jsonify({
            "message": "Invalid API key"
        }), 401

    for application in applications:

        if application.get("application_id") == application_id:

            applications.remove(application)

            with open(DATA_FILE, "w") as file:
                json.dump(applications, file, indent=4)

            return jsonify({
                "message": "Application deleted successfully"
            })

    return jsonify({
        "message": "Application not found"
    }), 404


# PUT - Update application
@app.route("/application/<application_id>", methods=["PUT"])
def update_application(application_id):

    if not check_api_key():
        return jsonify({
            "message": "Invalid API key"
        }), 401

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "No update data provided"
        }), 400

    for application in applications:

        if application.get("application_id") == application_id:

            # Prevent changing the application ID
            data.pop("application_id", None)

            application.update(data)

            with open(DATA_FILE, "w") as file:
                json.dump(applications, file, indent=4)

            return jsonify({
                "message": "Application updated successfully",
                "data": application
            })

    return jsonify({
        "message": "Application not found"
    }), 404


# Start Flask server
if __name__ == "__main__":
    app.run()