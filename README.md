# 🏠 House Price Prediction Dashboard

An end-to-end Machine Learning project that predicts house prices using real-world features and displays results through an interactive web dashboard.

---

## 🚀 Project Overview

This project combines **Machine Learning + Backend API + Frontend Dashboard** to deliver real-time house price predictions.

* 📊 Predict house prices based on input features
* ⚡ Fast API response using FastAPI
* 💻 Interactive UI built with Next.js
* 📈 Visual insights using charts

---

## 🛠️ Tech Stack

### 🔹 Machine Learning

* Python
* Scikit-learn
* XGBoost

### 🔹 Backend

* FastAPI
* Uvicorn

### 🔹 Frontend

* Next.js
* React
* Recharts

---

## ✨ Features

✔ Real-time price prediction
✔ Clean and responsive UI
✔ Interactive charts
✔ Full-stack integration
✔ Scalable API architecture

---

## 📂 Project Structure

```
house-price-advanced/
│
├── frontend/           # Next.js frontend
├── serving/            # FastAPI backend
├── models/             # Trained ML model
├── src/                # ML pipeline & features
├── notebooks/          # Data analysis
├── data/               # Dataset
├── requirements.txt    # Python dependencies
└── README.md
```

---
## Screenshot
<img width="960" height="540" alt="DASH SS1" src="https://github.com/user-attachments/assets/ffaedd8d-f318-4429-b228-2ff91d73bbec" />
<img width="960" height="540" alt="ss4" src="https://github.com/user-attachments/assets/f7229db3-526d-426e-b565-19da72ce2681" />
<img width="960" height="540" alt="ss5" src="https://github.com/user-attachments/assets/fdd77dd9-0ced-42db-8d41-8f6bfe74b5b4" />



## ⚙️ Setup Instructions

### 🔹 1. Clone Repository

```
git clone https://github.com/arpitabhendigeri004-sudo/house-price-predictor-dashboard.git
cd house-price-advanced
```

---

### 🔹 2. Backend Setup

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn serving.app:app --reload
```

Backend will run on:
👉 http://127.0.0.1:8000

---

### 🔹 3. Frontend Setup

```
cd frontend
npm install
npm run dev
```

Frontend will run on:
👉 http://localhost:3000

---

## 📊 API Endpoint

### POST `/predict`

#### Sample Input:

```json
{
  "GrLivArea": 1500,
  "GarageArea": 400,
  "TotalBsmtSF": 800,
  "YearBuilt": 2005,
  "FullBath": 2,
  "HalfBath": 1,
  "TotRmsAbvGrd": 6,
  "Neighborhood": "NAmes",
  "BldgType": "1Fam"
}
```

#### Output:

```json
{
  "price": 250000
}
```

---

## 📌 Future Improvements

* Add model explainability (SHAP)
* Deploy on cloud (Render / Vercel)
* Add authentication
* Improve UI/UX design

---

## 🙏 Acknowledgment

Special thanks to **Umesh Sir** for guidance and support.

---

## 💬 Feedback

Feel free to open issues or suggest improvements!

---

## 📢 Author

**Arpita Bhendigeri**

---

⭐ If you like this project, consider giving it a star!
