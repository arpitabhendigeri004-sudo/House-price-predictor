import pandas as pd
import numpy as np

df = pd.read_parquet("data/houses.parquet")

# Log transform
df["log_price"] = np.log1p(df["SalePrice"])

# Remove outliers
df = df[df["GrLivArea"] < df["GrLivArea"].quantile(0.99)]

df.to_parquet("data/houses_clean.parquet")