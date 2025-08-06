# 🎓 Student Performance Indicator

🔗 **Live App:** [http://student-performance-app.duckdns.org/](http://student-performance-app.duckdns.org:6120/)

This is a full-stack machine learning application that predicts a student's **math score** based on inputs like gender, parental education, reading and writing scores, lunch type, and test preparation.

It includes:
- End-to-end ML pipeline (data ingestion → training → prediction)
- Clean and responsive Flask-based UI with tooltips, reset & dark mode
- CI/CD deployment on AWS (ECR + EC2) using GitHub Actions and Docker

---

## 📊 Demo

> 🚀 Visit the app: [http://student-performance-app.duckdns.org/](http://student-performance-app.duckdns.org/)

<p align="center">
  <img src="static/student_illustration.png" alt="Student UI" width="600"/>
</p>

---

## 🧠 Problem Statement

Predict a student's **math score** based on demographic and academic features. This helps parents, teachers, or students understand where performance improvements are needed, and what factors influence performance.

---

## 📁 Features

- 🧮 Predict student's math score using ML
- 🧾 Input fields with hover-based tooltips for easy understanding
- 🌗 Dark mode support
- 🧹 Reset functionality to clear inputs and predictions
- 📈 Score-based suggestions to guide users
- 🐳 Dockerized and deployed using GitHub Actions, ECR, and EC2

---

## 🧱 Tech Stack

| Layer           | Tools Used                          |
|----------------|-------------------------------------|
| ML Pipeline     | `scikit-learn`, `pandas`, `numpy`   |
| Web App         | `Flask`, `HTML`, `CSS`, `Jinja`     |
| Deployment      | `Docker`, `GitHub Actions`, `EC2`, `ECR`, `DuckDNS` |
| Cloud Storage   | `AWS S3` (for syncing artifacts)     |
| CI/CD           | `GitHub Actions`, `DockerHub/ECR`    |

---
User → Web Form (Flask UI) → PredictPipeline → Trained Model (.pkl)
↓
HTML Output with Suggestions

ML Pipeline:  

CSV → Data Ingestion → Validation → Transformation → Model Training → Prediction
↓ ↓
train/test split preprocessor.pkl & .npy


---

## ⚙️ Local Setup Instructions

> ✅ Prerequisites: Python 3.10+, Docker, Git, AWS CLI (for cloud), MongoDB (optional for ingestion)

### 1. Clone the repository
```bash
git clone https://github.com/sarveshnatkar12/Student_Performance_Indicator.git
cd Student_Performance_Indicator

2. Create & activate virtual environment
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Start the application locally
python app.py
Access the app at http://127.0.0.1:6120

🚀 Deployment Summary
Dockerized app using a lightweight Python image

GitHub Actions workflow:

Builds and pushes Docker image to Amazon ECR

SSH into EC2 → pulls image → runs container

DNS: Connected EC2 IP to a free DuckDNS subdomain

| Field                   | Example           |
| ----------------------- | ----------------- |
| Gender                  | female            |
| Race/Ethnicity          | group B           |
| Parental Education      | bachelor’s degree |
| Lunch                   | standard          |
| Test Preparation Course | completed         |
| Reading Score           | 78                |
| Writing Score           | 74                |

🧑‍💻 Author
👨‍💻 Sarvesh Natkar

📜 License
This project is licensed under the MIT License.


## 🏗️ Architecture

