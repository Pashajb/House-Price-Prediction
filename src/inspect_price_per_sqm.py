
import duckdb

file_path = "data/raw/real_estate_ads.csv"
con = duckdb.connect()

base_filter = """
    cat2_slug = 'residential-sell'
    AND cat3_slug = 'apartment-sell'
    AND city_slug IN ('tehran', 'shiraz')
    AND price_mode = 'مقطوع'
    AND price_value > 0
    AND building_size >= 30
    AND building_size <= 1000
"""

# 1. Price per square meter distribution
print("\nPRICE PER SQUARE METER DISTRIBUTION")
print("=" * 90)

query = f"""
    SELECT
        city_slug,
        COUNT(*) AS n,
        ROUND(quantile_cont(price_value / building_size, 0.50), 0) AS median,
        ROUND(quantile_cont(price_value / building_size, 0.95), 0) AS p95,
        ROUND(quantile_cont(price_value / building_size, 0.99), 0) AS p99,
        ROUND(quantile_cont(price_value / building_size, 0.999), 0) AS p999,
        MAX(price_value / building_size) AS maximum
    FROM read_csv_auto('{file_path}')
    WHERE {base_filter}
    GROUP BY city_slug
"""

for row in con.execute(query).fetchall():
    print(row)


# 2. 20 highest price-per-square-meter listings
print("\nTOP 20 PRICE PER SQUARE METER")
print("=" * 90)

query = f"""
    SELECT
        city_slug,
        created_at_month,
        price_value,
        building_size,
        ROUND(price_value / building_size, 0) AS price_per_sqm,
        title
    FROM read_csv_auto('{file_path}')
    WHERE {base_filter}
    ORDER BY price_per_sqm DESC
    LIMIT 20
"""

for row in con.execute(query).fetchall():
    print(row)
