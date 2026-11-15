
import duckdb

file_path = "data/raw/real_estate_ads.csv"

con = duckdb.connect()

query = f"""
WITH filtered AS (
    SELECT
        city_slug,
        price_value,
        building_size,
        price_value / building_size AS price_per_sqm
    FROM read_csv_auto('{file_path}')
    WHERE cat2_slug = 'residential-sell'
      AND cat3_slug = 'apartment-sell'
      AND city_slug IN ('tehran', 'shiraz')
      AND price_mode = 'مقطوع'
      AND price_value > 0
      AND building_size > 0
)
SELECT
    city_slug,
    COUNT(*) AS total_records,
    COUNT(*) FILTER (WHERE price_value = 1) AS price_equals_1,
    COUNT(*) FILTER (WHERE price_value > 90000000000) AS price_above_90_billion,
    COUNT(*) FILTER (WHERE price_per_sqm > 500000000) AS sqm_above_500_million,
    COUNT(*) FILTER (WHERE price_per_sqm > 1000000000) AS sqm_above_1_billion,
    COUNT(*) FILTER (WHERE price_per_sqm > 10000000000) AS sqm_above_10_billion
FROM filtered
GROUP BY city_slug
ORDER BY city_slug
"""

print(con.execute(query).fetchdf().to_string(index=False))
