## Project Overview

This project is a complete data analytics case study focused on cleaning, integrating, and visualizing socio-economic data from various countries. The goal was to demonstrate professional data preparation and visualization skills using **Power BI** — without writing DAX — while applying left joins, fuzzy matching, data type corrections, and interactive dashboard design.

The dataset originates from the CIA World Factbook and includes demographic, health, education, military, and unemployment indicators.

---

## Data Sources

| File | Description |
|------|-------------|
| `people_and_society.tsv` | Main table (TSV format): country, region, median age, birth rate, death rate, life expectancy, fertility rate, obesity rate. |
| `education.csv` | Education expenditure (% of GDP). |
| `military.csv` | Military expenditure (% of GDP). |
| `unemployment.csv` | Unemployment rate (% of labor force). |

All files were loaded, cleaned, and joined in Power BI.

---

## Tools & Technologies

- **SQL** – conceptual data modeling and join logic (LEFT JOIN, fuzzy matching)
- **Python** – initial data inspection and validation (pandas) before importing into Power BI
- **Power BI** – data transformation (Power Query), relationship management, interactive dashboards, and visualizations (cards, bar charts, grouped bar charts, filled maps, scatter plots, slicers)

---

## Data Preparation Steps

1. **Load `people_and_society.tsv`**  
   - Tab-separated values  
   - Fixed decimal separator: replaced `#` with `.` in `median_age` → changed column type to decimal  
   - Corrected region typo: `Evropa` → `Europe`

2. **Load additional CSV files** (`education`, `military`, `unemployment`)  
   - Kept only `country` and respective metric columns  
   - Renamed columns for clarity

3. **Establish relationships**  
   - Left joins from `people_and_society` to each secondary table  
   - Enabled **fuzzy matching** to handle country name inconsistencies

4. **Data modeling**  
   - All tables connected via `country` key  
   - No calculated columns or DAX measures were used — only built-in aggregations (sum, median, max, min)

---

## Dashboard Pages & Visualizations

### Page 1 – Key Metrics & Top 10 Rankings

**Cards:**
- Total number of countries
- Median of median ages across all countries
- Maximum life expectancy
- Minimum life expectancy

**Bar Charts:**
- Top 10 countries by death rate
- Top 10 countries by birth rate

**Grouped Bar Charts:**
- Fertility rate vs education expenditure for **bottom 10** countries by education spending
- Fertility rate vs education expenditure for **top 10** countries by education spending  
  *Note: The highest bar in the second chart appeared for `(Blank)` country. This was filtered out because blank country names exist in the source but contain valid numeric data.*

**Table:**
- Region | median_age | unemployment_rate  
  Aggregation changed from *sum* to *median*, columns renamed back. Blank region row removed.

### Page 2 – Geographic Analysis

- **Circle Map** – bubble size represents military expenditure (% of GDP)
- **Filled Map** – color gradient (darker = higher obesity rate)  
  - Tooltip shows country name and obesity percentage
- **Slicer** – filter by region (excludes blank country). Maps update dynamically.

### Page 3 – Scatter Plot (Fertility vs Median Age)

- X‑axis: median age  
- Y‑axis: fertility rate  
- Aggregation set to *Don’t Summarize*  
- **Insight:** Strong negative correlation — countries with higher median age have lower fertility rates, reflecting demographic transition patterns.

---

## Key Insights

1. **Demographic transition** is clearly visible on the scatter plot: developed nations (older median age) tend to have lower fertility rates.
2. **Education spending** does not always correlate with lower fertility; some low‑spending countries still have low fertility due to other factors.
3. **Obesity rates** vary significantly by region, with the highest concentrations in North America and Europe.
4. **Military vs education spending** shows interesting trade‑offs – visualized on maps.
5. Data quality issues (blank country names, incorrect decimal separators, region typos) were successfully identified and fixed using Power Query.

---

## How to Use This Project

1. Clone the repository or download `bi_homework.pbix`.
2. Open the file in **Power BI Desktop** (free version).
3. Navigate through the three report pages using tabs at the bottom.
4. Use the region slicer on Page 2 to filter maps interactively.
5. Hover over any visual to see tooltips with detailed values.

---

## Author
Kriffi
**Data Analyst** – portfolio project  

---

## Tech Stack Summary

`SQL` • `Python (pandas)` • `Power BI` • `Power Query` • `Fuzzy Matching` • `Interactive Dashboards`
##  Screenshots 
- <img width="1932" height="1049" alt="image" src="https://github.com/user-attachments/assets/93cb0c8d-4f2e-4036-b30b-9a0dd82ce693" />
  - <img width="1914" height="1094" alt="image" src="https://github.com/user-attachments/assets/29412023-ae31-4128-8581-5391dde20e37" />
  - <img width="1902" height="1099" alt="image" src="https://github.com/user-attachments/assets/d33ad7e3-f765-491e-b7e1-c9c4472ec2e6" />
- <img width="1953" height="930" alt="image" src="https://github.com/user-attachments/assets/d7e52af6-e7c2-476f-81bd-65852e7b0970" />
---







