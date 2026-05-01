from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

# -------------------------------
# 🚀 LOAD MODEL
# -------------------------------
model = joblib.load("models/model.joblib")

# -------------------------------
# 🚀 INIT APP
# -------------------------------
app = FastAPI(title="House Price Prediction API")

# -------------------------------
# 🚀 ENABLE CORS (IMPORTANT)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# 🚀 INPUT SCHEMA
# -------------------------------
from pydantic import BaseModel, Field

class House(BaseModel):
    GrLivArea: float = Field(gt=0)
    GarageArea: float = Field(ge=0)
    TotalBsmtSF: float = Field(ge=0)
    YearBuilt: int = Field(gt=1800, lt=2025)
    FullBath: int = Field(ge=0)
    HalfBath: int = Field(ge=0)
    TotRmsAbvGrd: int = Field(gt=0)
    Neighborhood: str
    BldgType: str


# -------------------------------
# 🚀 ROOT
# -------------------------------
@app.get("/")
def home():
    return {"message": "✅ House Price API Running"}


# -------------------------------
# 🚀 HEALTH CHECK
# -------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# -------------------------------
# 🚀 PREDICT API
# -------------------------------
@app.post("/predict")
def predict(data: House):
    try:
        df = pd.DataFrame([data.dict()])

        # FIX: add missing feature
        df["Age"] = 2024 - df["YearBuilt"]

        prediction = model.predict(df)[0]

        return {"price": float(prediction), "status": "success"}

    except Exception as e:
        return {"error": str(e), "status": "failed"}