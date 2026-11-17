import pandas as pd
from pathlib import Path

df = pd.read_csv("data/raw/real_estate_ads.csv", low_memory=False)

# Select Tehran and Shiraz apartment sales
df = df[
    df["city_slug"].isin(["tehran", "shiraz"])
    & (df["cat3_slug"] == "apartment-sell")
    & (df["price_mode"] == "مقطوع")
].copy()

# Convert Persian and Arabic digits to English digits
digit_map = str.maketrans(
    "۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩",
    "01234567890123456789"
)

def convert_digits(value):
    if pd.isna(value):
        return None
    return str(value).translate(digit_map).strip()

# Convert numeric columns
df["construction_year"] = df["construction_year"].apply(convert_digits)
df["construction_year"] = pd.to_numeric(
    df["construction_year"], errors="coerce"
)

# Convert Persian room names to numbers
room_map = {
    "بدون اتاق": 0,
    "یک": 1,
    "دو": 2,
    "سه": 3,
    "چهار": 4,
    "پنج": 5,
    "شش": 6,
    "هفت": 7,
}

df["rooms_count"] = df["rooms_count"].apply(convert_digits)
df["rooms_count"] = df["rooms_count"].replace(room_map)
df["rooms_count"] = pd.to_numeric(
    df["rooms_count"], errors="coerce"
)

# Convert price and size
df["price_value"] = pd.to_numeric(df["price_value"], errors="coerce")
df["building_size"] = pd.to_numeric(df["building_size"], errors="coerce")

# Basic filtering
df = df[
    (df["price_value"] >= 1_000_000)
    & (df["building_size"] >= 20)
    & (df["building_size"] <= 500)
].copy()

# Remove extreme prices above the 99th percentile
price_limit = df["price_value"].quantile(0.99)
df = df[df["price_value"] <= price_limit].copy()

# Keep useful columns
columns = [
    "city_slug",
    "building_size",
    "rooms_count",
    "construction_year",
    "price_value"
]

df = df[columns].dropna(subset=["price_value", "building_size"])
df = df.drop_duplicates()

# Save processed dataset
Path("data/processed").mkdir(parents=True, exist_ok=True)
df.to_csv("data/processed/apartments.csv", index=False)

print("Dataset prepared successfully!")
print("Final shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nCity distribution:")
print(df["city_slug"].value_counts())
print("\nPrice limit:", f"{price_limit:,.0f}")
