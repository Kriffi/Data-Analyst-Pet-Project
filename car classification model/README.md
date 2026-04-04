# Car Price Category Classification: Data Analysis & Preparation

## Project Overview

This project focuses on preparing and analyzing a dataset of used cars listed for sale in the United States. The ultimate goal is to build a classification model that predicts the price category (low, medium, high) of a used vehicle based on its characteristics. This report covers the initial data exploration, variable identification, handling of missing values, and distribution analysis that serve as the foundation for the modeling stage.

The dataset is a subset of Craigslist vehicle listings and includes various features such as price, year, manufacturer, condition, odometer reading, fuel type, transmission, and geographic information.

---

## Data Sources

| File | Description |
|------|-------------|
| `vehicles_dataset.csv` | Main dataset containing 10,050 records and 27 columns. Includes car features, listing metadata, and the target variable `price_category`. |

Source: Provided as part of a data analytics coursework.

## Dataset Description

The dataset contains **10,050 records** and **27 columns**. Below is the description of each field:

| Column Name     | Description                                          |
|----------------|------------------------------------------------------|
| `id`            | Unique record identifier                             |
| `url`           | Craigslist listing URL                               |
| `region`        | Geographic region of the listing                     |
| `region_url`    | URL of the region page                               |
| `price`         | Listed price (USD)                                   |
| `year`          | Vehicle manufacturing year                           |
| `manufacturer`  | Car brand (e.g., Ford, Toyota)                       |
| `model`         | Vehicle model name                                   |
| `condition`     | Condition category (new, good, fair, etc.)           |
| `cylinders`     | Number of cylinders                                  |
| `fuel`          | Fuel type (gas, diesel, hybrid, electric)            |
| `odometer`      | Miles driven                                         |
| `title_status`  | Title status (clean, salvage, etc.)                  |
| `transmission`  | Transmission type (automatic, manual)                |
| `VIN`           | Vehicle Identification Number                        |
| `drive`         | Drivetrain (fwd, rwd, 4wd)                           |
| `size`          | Vehicle size category (compact, midsize, full-size)  |
| `type`          | Body type (sedan, SUV, pickup, etc.)                 |
| `paint_color`   | Exterior color                                       |
| `image_url`     | URL of the vehicle image                             |
| `description`   | Text description of the listing                      |
| `county`        | County name (mostly missing)                         |
| `state`         | US state code                                        |
| `lat`           | Latitude coordinate                                  |
| `long`          | Longitude coordinate                                 |
| `posting_date`  | Date and time of the listing                         |
| `price_category`| **Target variable** – low / medium / high price class |
---

## Tools & Technologies

- **Python** – data manipulation and analysis (pandas, numpy)
- **Jupyter Notebook** – interactive environment for exploration
- **Git / GitLab** – version control and project submission

---

## Data Preparation Steps

1. **Load the dataset**  
   - Read `vehicles_dataset.csv` using `pandas.read_csv()`.
   - Displayed first few rows and checked shape: `(10050, 27)`.

2. **Inspect column types and basic statistics**  
   - Used `df.info()` and `df.describe()` to understand numeric columns.
   - Identified columns with missing values (e.g., `year`, `cylinders`, `paint_color`, `county`).

3. **Explore unique values per column**  
   - For each column, printed number of unique values and frequency counts.
   - Example: `id` column has 10,000 unique values (some duplicates due to data collection quirks).

4. **Classify variable types**  
   - Determined discrete, continuous, and categorical variables (see table below).

5. **Identify target variable**  
   - According to the task, `price_category` is the target: it contains three classes – `low`, `medium`, `high`.

6. **Check target distribution**  
   - Computed value counts and proportions:
     - high: 34.97%
     - medium: 32.78%
     - low: 32.26%
   - The distribution is nearly balanced (suitable for classification without heavy resampling).

---

## Variable Classification

| Variable        | Discrete | Continuous | Categorical |
|----------------|----------|------------|--------------|
| id              | X        |            |              |
| region          |          |            | X            |
| year            | X        |            |              |
| manufacturer    |          |            | X            |
| condition       | X        |            |              |
| fuel            |          |            | X            |
| odometer        |          | X          |              |
| title_status    |          |            | X            |
| transmission    |          |            | X            |
| VIN             |          |            | X            |
| drive           |          |            | X            |
| paint_color     |          |            | X            |
| state           |          |            | X            |
| price_category  | X        |            |              |

---

## Exploratory Data Analysis (EDA)

### Descriptive Statistics (Numeric Columns)

| Column    | Count   | Mean        | Std         | Min      | 25%      | 50%      | 75%      | Max         |
|-----------|---------|-------------|-------------|----------|----------|----------|----------|-------------|
| price     | 10050   | 20,684.29   | 124,321.6   | 500      | 7,900    | 15,749.5 | 27,990   | 12,345,680  |
| year      | 10014   | 2010.92     | 9.70        | 1915     | 2008     | 2013     | 2017     | 2022        |
| odometer  | 10007   | 95,657.19   | 86,579.48   | 0        | 38,994.5 | 88,377   | 137,000  | 3,245,000   |

- **Price** has a very high max (over $12M) – potential outlier.
- **Year** ranges from 1915 to 2022; modern cars dominate (median 2013).
- **Odometer** shows extreme values (3 million miles) – likely data entry errors.

### Target Variable Distribution
price_category
- high 0.349652
- medium 0.327761
- low 0.322587

The target is well‑balanced across three classes.

---

## Feature Engineering (Planned for Next Phase)

- Drop irrelevant columns: `url`, `region_url`, `image_url`, `description`, `VIN`, `id`, `posting_date` (not useful for prediction).
- Handle missing values in `year`, `odometer`, `condition`, `cylinders`, `fuel`, `transmission`, `drive`, `size`, `type`, `paint_color`.
- Encode categorical variables (one‑hot or ordinal encoding).
- Scale numeric features (`price`, `odometer`, `year`).
- Remove outliers in `price` and `odometer` using IQR or domain knowledge.
- Create new features: `car_age` = 2025 - year, `mileage_per_year` = odometer / car_age.

---

## Key Insights

1. **Balanced target** – No immediate need for oversampling/undersampling.
2. **Data quality issues** – Missing values are abundant in many categorical columns (e.g., `cylinders`, `paint_color`, `size`). Missingness must be addressed.
3. **Extreme outliers** – Some cars have unrealistic prices (> $1M) or odometer readings (> 1M miles). These will be filtered.
4. **Potential useful features** – `region`, `state`, `lat/long` may capture geographic price differences.
5. **Time component** – `posting_date` and `year` allow analysis of depreciation and market trends.

---

## How to Reproduce This Analysis

1. Clone the repository (or download the notebook).
2. Place `vehicles_dataset.csv` inside a `data/` folder.
3. Open `dataset.ipynb` in Jupyter Notebook or VS Code.
4. Run all cells sequentially to replicate:
   - Data loading and inspection
   - Variable classification
   - Target distribution analysis
5. For further EDA and modeling, extend the notebook with the steps outlined above.

---

## Author

**Student / Data Analyst** – Practical work for Data Preparation module  
Course: Skillbox Data Analyst Program

---

## Tech Stack Summary

`Python` • `pandas` • `Jupyter Notebook` • `Git` • `GitLab`

---

## Screenshots


- pandas boxplot 
  boxplot <img width="1527" height="847" alt="image" src="https://github.com/user-attachments/assets/0627a1be-1e9a-4931-9377-b11224c852e8" />

