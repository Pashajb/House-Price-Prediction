# Apartment Price Prediction – Tehran & Shiraz

An educational machine learning project that explores apartment price prediction using real estate listing data from Tehran and Shiraz, Iran.

> [!WARNING]
> **EDUCATIONAL PROJECT ONLY — NOT FOR REAL ESTATE VALUATION**
>
> This project is developed strictly for learning and experimentation. Its predictions should not be interpreted as current market prices or used for financial or property-related decisions.
>
> Iran's housing market is affected by inflation, currency fluctuations, economic conditions, and changes in supply and demand. These factors are not explicitly modeled in this project.
>
> Although the original dataset contains listing publication dates, the selected data is heavily concentrated between May and December 2024. Earlier and later periods have very few records. Therefore, the model cannot reliably capture long-term housing price trends or inflation.

## Project Overview

The project focuses on fixed-price apartment sale listings in:

- Tehran
- Shiraz

The objective is to practice a basic machine learning regression workflow, including data preparation, model training, and evaluation.

## Dataset

The original dataset contains approximately 1,000,000 real estate listings and 60 features.

Data source: [Divar Real Estate Ads Dataset – Hugging Face](https://huggingface.co/datasets/divarofficial/real_estate_ads)

For this project, the data is filtered to include:

- Apartment sale listings
- Tehran and Shiraz
- Fixed-price advertisements

The final processed dataset contains approximately 80,115 records.

### Features

- `city_slug`: City
- `building_size`: Building size in square meters
- `rooms_count`: Number of rooms
- `construction_year`: Year of construction

### Target

- `price_value`: Advertised apartment price in Toman

### Data Preparation

- Convert Persian and Arabic numerals into English numerals.
- Convert Persian room descriptions into numeric values.
- Remove invalid records.
- Keep apartments between 20 and 500 square meters.
- Remove extreme prices above the 99th percentile.
- Remove duplicate records.
- Handle missing values during model training.

## Models

Two regression algorithms are trained and compared:

1. Linear Regression
2. Random Forest Regressor

The dataset is split into training and testing sets using an 80/20 random split.

## Model Evaluation

| Metric | Linear Regression | Random Forest |
|---|---:|---:|
| MAE | 3.85 Billion Toman | 3.51 Billion Toman |
| RMSE | 6.48 Billion Toman | 6.12 Billion Toman |
| R² | 0.6636 | 0.6997 |

Random Forest achieved the best results among the tested models.

**Important:** These metrics measure performance on a random held-out test set from the same dataset. They do not measure accuracy on current market prices or future listings.

## Project Structure

```text
House-Price-Prediction/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── src/
│   ├── download_data.py
│   ├── inspect_data.py
│   ├── inspect_price_per_sqm.py
│   ├── prepare_data.py
│   ├── train_model.py
│   └── predict.py
├── notebooks/
├── reports/
├── requirements.txt
└── README.md
