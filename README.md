# 🎓 Student Application Automation System

## 📌 Project Description

A Student Application Automation System built using **n8n** and **Python Flask**.

The system collects student applications, validates eligibility, generates an application ID, stores application data, and sends the data to a secure Python backend API.

## 🔄 Workflow


-Student submits the application form.
-n8n collects the application details.
-An application ID is generated automatically.
-Student eligibility is checked using the marks/CGPA value.
-Duplicate applications are checked.
-Valid applications are stored in the n8n Data Table.
-n8n sends the application data to the Python Flask API.
-The Flask API authenticates the request using an API key.
-Application data is stored in applications.json.
-n8n handles successful and failed API requests separately.

## 🛠️ Technologies Used

- **Python**
- **Flask**
- **n8n**
- **REST API**
- **JSON**
- **API Key Authentication**
- **Environment Variables**
- **Git & GitHub**

## ✨ Features

- 📝 Student application form
- ✅ Automatic eligibility validation
- 🆔 Automatic application ID generation
- 🔍 Duplicate application checking
- 💾 Application data storage
- 🔗 n8n → Python Flask API integration
- 🔐 API key authentication
- 🌐 REST API endpoints
- ⚠️ API error handling
- 📄 JSON-based data persistence
- 🔒 Environment variable-based secret management

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/application` | Submit a new application |
| GET | `/applications` | Get all applications |
| GET | `/application/<application_id>` | Get one application |
| PUT | `/application/<application_id>` | Update an application |
| DELETE | `/application/<application_id>` | Delete an application |

## 📁 Project Structure


Student Application Automation System/
│
├── student_api.py
├── applications.json
├── .gitignore
└── README.md

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd Student-Application-Automation-System

2. Install Required Python Packages
pip install flask python-dotenv

3. Create the .env File
Create a .env file in the project folder.
Add:
API_KEY=your-secret-api-key
🔐 Never add your real API key to GitHub.

4. Start the Flask API
Run:
python student_api.py
The API will run at:
http://127.0.0.1:5000

5. Start n8n
Run:
n8n

Then open:
http://localhost:5678

🔐 Authentication
The Flask API uses API Key authentication.
n8n sends the API key using the following HTTP header:
X-API-Key: your-secret-api-key
The Flask backend validates the API key before accepting an application.
If the API key is invalid, the API returns:
{
    "message": "Invalid API key"
}

with HTTP status:
401 Unauthorized

⚠️ Error Handling
The n8n workflow handles API failures using separate success and error paths.

Successful API Request
Python API: Application saved successfully ✅
Failed API Request
Python API error — application was not sent to the backend ❌

The Flask API also returns appropriate HTTP status codes when an application is not found or authentication fails.

💾 Data Persistence

Application data is stored locally in:
applications.json
Example:

[
    {
        "application_id": "APP-123456",
        "student_name": "Example Student",
        "email": "student@example.com",
        "phone": "+91XXXXXXXXXX",
        "course": "B.Sc CA & IT",
        "marks": 78,
        "status": "Eligible"
    }
]
🎯 Project Objective

The main objective of this project is to demonstrate how workflow automation and backend API development can be combined to create a practical student application management system.

The project demonstrates:

Workflow automation using n8n
Backend development using Python Flask
REST API development
API authentication
Error handling
JSON data persistence
Environment variable management
Integration between automation and backend services

👨‍💻 Author
Om Patel
B.Sc. (CA & IT)

📌 Future Improvements
Database integration using SQLite or PostgreSQL
Admin dashboard
Email notifications
Student application status tracking
JWT authentication
Docker deployment
Cloud deployment
Automated testing