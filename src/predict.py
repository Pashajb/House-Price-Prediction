import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/best_model.joblib")

print("=" * 40)
print("APARTMENT PRICE PREDICTION")
print("=" * 40)

city = input("City (tehran / shiraz): ").strip().lower()
size = float(input("Building size (m²): "))
rooms = float(input("Number of rooms: "))
year = float(input("Construction year (e.g. 1395): "))

apartment = pd.DataFrame([{
    "city_slug": city,
    "building_size": size,
    "rooms_count": rooms,
    "construction_year": year
}])

prediction = model.predict(apartment)[0]

print("\nEstimated apartment price:")
print(f"{prediction:,.0f} Toman")
print(f"Approximately {prediction / 1_000_000_000:.2f} Billion Toman")
