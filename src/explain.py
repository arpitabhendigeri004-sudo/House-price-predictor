import shap
import joblib
import pandas as pd

model = joblib.load("models/model.joblib")

df = pd.read_parquet("data/houses_clean.parquet")
X = df.drop("SalePrice", axis=1)

explainer = shap.Explainer(model.named_steps["xgb"])
shap_values = explainer(model.named_steps["pre"].transform(X))

shap.summary_plot(shap_values)