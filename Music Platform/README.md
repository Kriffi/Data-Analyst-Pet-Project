# Data-Analyst-Pet-Project
Data Analyst Portfolio Project

## Music Data Analysis Platform (API + SQL + Analytics)
# Overview

AThis project demonstrates a full-cycle data analysis workflow:
from data collection via API to SQL analysis and business insights.

Using the iTunes API, I collected music data for Louis Armstrong and built a structured dataset for further analytical tasks.

The project simulates a real-world scenario where a Data Analyst works with external data sources, prepares data, and extracts insights for business decisions.
# Business Goal
Build a data pipeline and analyze music content to:

- Structure raw API data into analytical datasets
- Identify patterns in album releases
- Simulate product and sales analysis using SQL
- Generate insights applicable to media/content platforms
# Data Collection (API)
- Performed GET request to retrieve artist data
- Extracted amgArtistId
- Sent POST request to fetch album-level data
- Collected 100+ records
# Data Processing
- Parsed JSON responses
- Converted data into Pandas DataFrames
- Cleaned and structured dataset
- Removed non-relevant records (artist vs albums)
- Exported data:
   - .xlsx (reporting)
   - .csv (analysis-ready format)
# SQL Analysis
After data collection, the dataset was used for SQL-based analysis:

- Aggregated album data
- Analyzed distribution of releases
- Simulated revenue-style metrics:
  - number of releases
  - album frequency
  - activity over time

 Example tasks:

- Identify most active periods
- Count albums per category
- Rank records using window functions
# Product / Behavioral Analysis

Simulated product analytics approach:

- Analyzed “content production funnel” (artist → albums)
- Evaluated distribution and density of releases
- Identified irregularities in dataset structure

Key idea:
Treat albums as “products” and analyze them like a content platform
# Key Insights
API data may include mixed entity types → requires filtering
- Content (albums) is unevenly distributed
- Structured APIs still require preprocessing
- Dataset can be reused for multiple analytical задач
  
# Business Impact

This project demonstrates how to:
- [x] Build datasets from external APIs
- [x] Combine Python + SQL in one workflow
- [x] Apply analytical thinking to real-world data
- [x] Translate raw data into business insights

# Tech Stack

- Python
- Requests
- Pandas
- SQL (PostgreSQL)
- Jupyter Notebook
- Git

# Skills Demonstrated
- API integration (REST)
- Data extraction & transformation
- SQL analysis (aggregations, joins, window functions)
- Data cleaning
- Product analytics thinking
- End-to-end data workflow
  
# Why This Project Matters
This project reflects real Data Analyst tasks:

- Working with external data sources
- Preparing messy data
- Combining tools (Python + SQL)
- Generating insights for business use
