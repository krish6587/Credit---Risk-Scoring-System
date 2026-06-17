# 🚀 Credit Risk Scoring System

![Credit Risk UI Preview](https://img.shields.io/badge/MLOps-FastAPI-blue?style=for-the-badge&logo=fastapi) ![Scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)

An AI-powered Credit Risk Scoring System that predicts loan approvals based on applicant details. This project demonstrates a complete MLOps pipeline, from training a Machine Learning model to deploying it behind a FastAPI backend, complete with a beautiful, modern user interface.

## ✨ Features
- **Machine Learning**: Uses a Random Forest Classifier to assess credit risk.
- **FastAPI Backend**: Serves predictions with blazing-fast speed and handles static file serving.
- **Modern UI**: A premium dark-mode web interface with micro-animations built with Vanilla HTML/CSS/JS.
- **Dockerized**: Ready to be deployed anywhere using Docker.

---

## 🛠️ How to Run This Project Locally

Anyone can run this project on their computer by following these simple steps:

### Prerequisites
Make sure you have [Python 3.10+](https://www.python.org/downloads/) installed.

### Option 1: Running with Python (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/krish6587/Credit---Risk-Scoring-System.git
   cd Credit---Risk-Scoring-System
   ```

2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

3. **Train the ML model:**
   *(This generates the `model.pkl` artifact required for predictions)*
   ```bash
   python src/train.py
   ```

4. **Start the FastAPI Server:**
   ```bash
   uvicorn app:app --host 127.0.0.1 --port 8000 --reload
   ```
5. **Open your browser** and visit 👉 `http://127.0.0.1:8000`

---

### Option 2: Running with Docker

If you have Docker installed, you can spin up the app in seconds without installing Python dependencies:

```bash
# Build the image
docker build -t credit-risk-app .

# Run the container
docker run -p 8000:8000 credit-risk-app
```
Then visit `http://127.0.0.1:8000` in your browser.

## 📁 Project Structure

```
Credit---Risk-Scoring-System/
├── app.py                 # FastAPI backend server
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container configuration
├── src/
│   ├── train.py           # ML Model training script
│   ├── predict.py         # Prediction logic
│   └── model.pkl          # Serialized ML model (generated after training)
└── static/
    ├── index.html         # Frontend UI
    ├── style.css          # Styling & Animations
    └── app.js             # API communication logic
```
