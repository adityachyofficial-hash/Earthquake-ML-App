# 🌍 Earthquake Magnitude Prediction (ML Project)

## 🚀 Overview
This project predicts earthquake magnitude using Machine Learning based on features like latitude, longitude, and depth.

It demonstrates a complete end-to-end ML workflow including data cleaning, model building, evaluation, and deployment.

---

## 📊 Features
- Data Cleaning & Preprocessing using Pandas  
- Exploratory Data Analysis (EDA)  
- Model Building:
  - Linear Regression
  - Decision Tree
  - Random Forest  
- Model Evaluation using MAE  
- Interactive prediction system using Streamlit  

---

## 🧠 Machine Learning Approach

- Input Features:
  - Latitude
  - Longitude
  - Depth  

- Target:
  - Magnitude  

- Best Model:
  - Linear Regression (MAE ≈ 0.34)

---

## ⚙️ Tech Stack

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 📂 Project Structure
app.py
earthquake.csv
requirements.txt
readme.md

---

## ▶️ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/Earthquake-ML-App.git
cd Earthquake-ML-App
pip install -r requirements.txt
streamlit run app.py
