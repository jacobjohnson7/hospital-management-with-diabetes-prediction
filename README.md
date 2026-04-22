# MedFlow

A modern, fast, and intelligent healthcare application built with **Django** and powered by **Machine Learning**. This project features a beautiful glassmorphic UI built natively with Bootstrap 5 and integrates custom AI to predict medical conditions.

## 🌟 Key Features

- **Doctor Management:** Easily register and manage records for medical staff.
- **Patient Registration:** Seamless onboarding for patient information and credentials.
- **Patient & Appointment Handling:** View, filter, and actively manage health appointments.
- **🚀 AI Diabetes Prediction:** Utilizes a custom-trained Logistic Regression Model from `scikit-learn` to instantly analyze 8 patient parameters and predict the likelihood of diabetes.
- **Premium Interface:** High-quality, responsive glassmorphic UI spanning dynamic glowing cards and deep animated mesh gradients.

---

## 🛠️ Stack Components

- **Backend:** Python + Django framework
- **Machine Learning Layer:** Scikit-Learn + Joblib (`diabetes_model.pkl`)
- **Frontend Core:** HTML5, pure CSS3 (Glassmorphism design language)
- **UI Frameworks:** Bootstrap 5.3, Bootstrap Icons
- **Typography:** Google Fonts (Outfit)

---

## 🚀 Getting Started

Follow these instructions to run the project locally on your machine.

### Prerequisites

Ensure you have Python installed, along with the necessary Django and ML packages:
```bash
pip install django scikit-learn numpy joblib
```

### Installation

1. **Clone or Download the Repository** to your local machine.
2. **Ensure the ML Model is Present:** 
   In order for the AI Diagnostics feature to work, make sure your trained `.pkl` model (`diabetes_model.pkl`) is placed directly in the main `hostpital` project folder (the same directory that contains `manage.py`).
3. **Navigate to the core directory:**
   ```bash
   cd hostpital
   ```
4. **Start the local Django Development Server:**
   ```bash
   python manage.py runserver
   ```
5. **View the App:** Open your web browser and navigate to `http://127.0.0.1:8000/`.

---

## 🩺 Diabetes Prediction Model Architecture
The AI prediction endpoint consumes the following 8 variables to formulate the output:
- `Pregnancies`
- `Glucose`
- `BloodPressure`
- `SkinThickness`
- `Insulin`
- `BMI`
- `DiabetesPedigreeFunction`
- `Age`

*(Model accepts raw variable parameters and returns a 1 for Diabetic and 0 for Non-Diabetic probability)*

---
*© 2026 Developed for MedFlow.*
