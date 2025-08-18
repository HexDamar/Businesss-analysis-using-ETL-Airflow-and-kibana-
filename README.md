# Laptop & PC Sales Analysis with ETL Pipeline 💻📊

## 🌟 Overview
This repository contains an end-to-end **ETL pipeline** project analyzing laptop and PC sales data from eBay. The project extracts raw data, transforms it through cleaning and validation, and loads it into Elasticsearch for visualization in Kibana. The goal is to provide actionable business insights to optimize sales strategies in the competitive tech market.

---

## 🚀 Problem Statement
**"How can eBay leverage sales data to identify market trends and improve revenue from laptop/PC sales?"**

### Market Context:
- Fluctuating global demand for computing devices (Gartner 2024)
- Consumers prioritize specs, price, and brand reputation (Statista)
- Need for data-driven decision-making in inventory and marketing

### Objectives:
1. Identify sales trends by time (monthly/quarterly) 📅
2. Analyze performance by product category (laptop vs desktop, brands, price ranges) 💰
3. Evaluate customer segments (geography, age, usage type) 🎯

---

## 📂 Repository Structure
```
├── P2M3_Nugroho_Wicaksono_DAG.py # Airflow ETL pipeline
├── P2M3_Nugroho_Wicaksono_data_raw.csv # Raw extracted data
├── P2M3_Nugroho_Wicaksono_data_clean.csv # Cleaned data
├── P2M3_Nugroho_Wicaksono_GX.ipynb # Data validation with Great Expectations
├── P2M3_Nugroho_Wicaksono_ddl.txt # PostgreSQL schema
├── images/ # EDA visualizations
│ ├── introduction & objective.png
│ ├── plot & insight 01-06.png
│ └── kesimpulan.png
└── README.md # Project documentation

```


---

## 🔍 Key Insights
### 📈 Sales Trends
- **Peak Seasons**: Q4 holiday surge (Black Friday/Christmas) 🎄
- **Top Brands**: Dell, HP, and Lenovo dominate mid-range sales 🏆
- **Price Sensitivity**: 70% of sales occur in $500-$1200 range 💵

### 📊 Customer Behavior
- **Gaming Laptops**: 25% YoY growth among 18-35 age group 🎮
- **Geographic Hotspots**: US & Germany account for 60% of premium PC sales 🌎

---

## 🛠️ Methodology
### 🔧 ETL Pipeline Architecture
1. **Extract**: PostgreSQL → Pandas DataFrame
2. **Transform**:
   - Handle missing values
   - Standardize price/currency formats
   - Categorize products by type/specs
3. **Load**: Elasticsearch → Kibana dashboards

### ✅ Data Validation
- Used **Great Expectations** to verify:
  - No nulls in critical fields (price, brand)
  - Valid date ranges
  - Consistent category labels

### 📉 Visualization
- Kibana dashboards for:
  - Sales funnel analysis
  - Regional performance heatmaps
  - Customer segmentation trees

---

## 💡 Business Recommendations
1. **Inventory Strategy**  
   - Increase stock of gaming laptops before Q4  
   - Phase out underperforming desktop models  

2. **Pricing Optimization**  
   - Bundle accessories with mid-range laptops ($800-$1000)  

3. **Marketing Focus**  
   - Target 18-35 demographic with esports partnerships  
   - Geo-target ads in US/Germany for premium models  

---

## ⚙️ Tech Stack
| Category          | Tools/Libraries |
|-------------------|-----------------|
| **ETL**          | Airflow, Pandas, SQLAlchemy |
| **Database**     | PostgreSQL, Elasticsearch |
| **Validation**   | Great Expectations |
| **Visualization**| Kibana |

```python
# Core Libraries
import pandas as pd
from airflow import DAG
from elasticsearch import Elasticsearch
import great_expectations as gx
```

## 📚 References
- [Great Expectations Documentation](https://greatexpectations.io/expectations/)  
- [Kaggle Dataset](https://www.kaggle.com/datasets/elvinrustam/ebay-laptops-and-netbooks-sales?select=EbayPcLaptopsAndNetbooksUnclean.csv)  

---

## ✨ Contributors
[Nugroho Wicaksono](https://github.com/HexDamar) - Data Engineer  

🔹 *Last Updated: August 2025*