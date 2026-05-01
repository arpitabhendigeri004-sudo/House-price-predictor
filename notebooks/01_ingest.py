import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.DataFrame({
    "GrLivArea": np.random.randint(500, 3000, 1000),
    "GarageArea": np.random.randint(100, 800, 1000),
    "TotalBsmtSF": np.random.randint(200, 1500, 1000),
    "YearBuilt": np.random.randint(1980, 2020, 1000),
    "FullBath": np.random.randint(1, 3, 1000),
    "HalfBath": np.random.randint(0, 2, 1000),
    "TotRmsAbvGrd": np.random.randint(4, 10, 1000),
    "Neighborhood": np.random.choice(["NAmes", "CollgCr", "OldTown"], 1000),
    "BldgType": np.random.choice(["1Fam", "2fmCon"], 1000),
    "SalePrice": np.random.randint(2000000, 10000000, 1000)
})

df.to_parquet("data/houses.parquet")
print("Dataset created")