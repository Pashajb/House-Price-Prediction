import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/processed/apartments.csv")

# Features and target
features = [
    "city_slug",
    "building_size",
    "rooms_count",
    "construction_year"
]

X = df[features]
y = df["price_value"]

# Preprocessing
numeric_features = [
    "building_size",
    "rooms_count",
    "construction_year"
]

categorical_features = ["city_slug"]

numeric_transformer = SimpleImputer(strategy="median")
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer(transformers=[
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        max_depth=20,
        random_state=42,
        n_jobs=-1
    )
}

best_model = None
best_mae = float("inf")
best_name = ""

for name, algorithm in models.items():
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", algorithm)
    ])

    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print(f"\n{name}")
    print("-" * 30)
    print(f"MAE:  {mae:,.0f} Toman")
    print(f"RMSE: {rmse:,.0f} Toman")
    print(f"R²:   {r2:.4f}")

    if mae < best_mae:
        best_mae = mae
        best_model = pipeline
        best_name = name

# Save the best model
joblib.dump(best_model, "models/best_model.joblib")

print("\n" + "=" * 30)
print("Best model:", best_name)
print("Saved to: models/best_model.joblib")
