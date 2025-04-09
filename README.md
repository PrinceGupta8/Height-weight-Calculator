# ⚖️ Height-Weight Predictor Web App

This is a simple machine learning web application built with **Streamlit** that predicts a person’s weight based on their height using a trained **Linear Regression** model.

## 🚀 Features
- 📈 Predicts weight in real time based on user input
- 🎯 Trained on real-world height-weight dataset
- 🧪 Uses `StandardScaler` for normalization
- 💾 Loads model and scaler using `pickle`
- 🌐 Clean and minimal Streamlit interface

---

## 🛠 Tech Stack
- Python 3.9+
- Pandas
- Scikit-learn
- Pickle
- Streamlit

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/princegupta8/height-weight-calculator.git
cd height-weight-calculator
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run height_weight_calculator.py
```

---

## 📂 Project Structure
```
├── height_weight_calculator.py     # Streamlit application
├── data.pkl                        # Trained ML model
├── scaler.pkl                      # StandardScaler object
├── height_weight_data.csv          # Dataset used
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

---

## 🧠 Model Training
The model is trained using a basic Linear Regression algorithm on height-weight data. The features are scaled using `StandardScaler` before training to ensure consistent results.
---
