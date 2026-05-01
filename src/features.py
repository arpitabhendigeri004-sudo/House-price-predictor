def add_features(df):
    df = df.copy()
    df["Age"] = 2025 - df["YearBuilt"]
    df["BathsTotal"] = df["FullBath"] + 0.5 * df["HalfBath"]
    df["RoomsPerArea"] = df["TotRmsAbvGrd"] / df["GrLivArea"]
    return df