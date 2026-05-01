import pandas as pd
from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib


from features import add_features
from pipeline import preprocessor

df = pd.read_parquet("data/houses_clean.parquet")
df = add_features(df)

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = Pipeline([
    ("pre", preprocessor),
    ("xgb", XGBRegressor(n_estimators=500))
])

model.fit(X_train, y_train)

pred = model.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, pred))
print("RMSE:", rmse)

joblib.dump(model, "models/model.joblib")