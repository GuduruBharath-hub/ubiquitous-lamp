# 📊 Task 5 — Final Report, Automation & Presentation

![Status](https://img.shields.io/badge/Status-Complete-success)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![PDF](https://img.shields.io/badge/Report-PDF-red)
![Excel](https://img.shields.io/badge/Export-Excel-green)
![Timeline](https://img.shields.io/badge/Timeline-4%20Days-orange)

> Part of the **ApexPlanet Data Analytics Internship — 30 Days**
> 🏢 [ApexPlanet Software Pvt. Ltd.](https://www.apexplanet.in)

---

## 🎯 Objective

Create a professional executive PDF report, automate the full data pipeline from raw data to Excel export, and submit all deliverables for the final internship evaluation.

---

## 📅 Timeline Breakdown

| Days | Focus Area |
|------|------------|
| Day 27 | Executive Summary PDF Report (2 pages, KPIs, insights, recommendations) |
| Day 28–29 | Automated Pipeline Script (Load → Clean → Analyse → Excel → Charts) |
| Day 30 | GitHub Cleanup, requirements.txt, Final Submission |

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| fpdf2 | Generate professional 2-page PDF executive report |
| openpyxl | Export KPIs and analytics to formatted Excel workbook |
| Pandas & NumPy | Data loading, cleaning and KPI computation |
| Matplotlib | Generate charts embedded in report and pipeline output |
| schedule | Pipeline scheduling capability |

---

## 📅 Day 27: Executive Summary PDF Report

### What the Report Contains

**Page 1:**
- Executive Summary paragraph
- 8 Key Performance Indicators (KPI table)
- Monthly Revenue Trend chart (embedded image)

**Page 2:**
- Top 5 Key Insights (with business context)
- 3 Actionable Business Recommendations
- All 5 Internship Tasks completion status
- Professional footer with branding

### Key KPIs in the Report

| KPI | Description |
|-----|-------------|
| Total Revenue | Sum of all transaction values |
| Total Orders | Unique invoice count |
| Unique Customers | Number of distinct buyers |
| Unique Products | Number of distinct items sold |
| Avg Order Value | Revenue ÷ Orders |
| Top Country | Highest revenue market |
| Peak Sales Month | Highest revenue month |
| Total Rows Analysed | Dataset size after cleaning |

### Top 5 Insights Documented

1. **Seasonal Revenue Peak** — Q4 (Oct–Nov) consistently produces peak revenue; confirmed by both EDA and statistical testing.
2. **Geographic Concentration** — One country dominates revenue contribution; international markets remain an untapped growth opportunity.
3. **Customer Segmentation** — K-Means revealed 4 distinct customer tiers: Champions, Loyal, At-Risk, and Occasional.
4. **Statistical Spending Differences** — T-Test confirmed UK vs Non-UK customers have significantly different spending behaviors (p < 0.05).
5. **Predictive Modeling** — Logistic Regression achieved strong accuracy; UnitPrice is the strongest predictor of order value.

### 3 Business Recommendations

1. **Invest in Q4 Marketing** — Allocate 40%+ of marketing budget to Oct–Dec for flash sales, bundles, and email campaigns.
2. **Launch Customer Loyalty Program** — Reward Champions and Loyal customers with tiered benefits, early access, and exclusive discounts.
3. **Win-Back At-Risk Customers** — Deploy targeted campaigns with time-limited vouchers and personalised product recommendations.

---

## 📅 Day 28–29: Automated Pipeline

### What the Pipeline Does

The automated script (`scripts/pipeline.py`) runs the entire analytics workflow in 5 steps:

```
[1/5] Load raw data       → data/data.csv
[2/5] Clean data          → data/data_cleaned_auto.csv
[3/5] Compute KPIs        → printed to console
[4/5] Export to Excel     → reports/analytics_report.xlsx
[5/5] Generate charts     → reports/pipeline_summary_charts.png
```

### Excel Report Structure (analytics_report.xlsx)

| Sheet | Contents |
|-------|----------|
| KPI Summary | All 6 key metrics in a formatted table |
| Monthly Revenue | Month-by-month revenue, orders, customers |
| Top Countries | Top 10 countries by revenue and customer count |
| Top Products | Top 10 products by revenue and quantity sold |

### How to Run the Pipeline

```bash
# From the project root
python scripts/pipeline.py
```

The entire pipeline completes in seconds and outputs all files automatically.

---

## 📅 Day 30: Final GitHub Cleanup

### Files Added

- ✅ `requirements.txt` — all Python package dependencies with version pins
- ✅ `scripts/pipeline.py` — standalone automation script
- ✅ `reports/final_executive_report.pdf` — 2-page professional PDF
- ✅ `reports/analytics_report.xlsx` — 4-sheet formatted Excel workbook

### Final Git Commands

```bash
git add .
git commit -m "Task 5 complete: Final report, pipeline automation & submission"
git tag v1.0.0
git push origin main
git push origin v1.0.0
```

---

## 📁 Complete Project Deliverables

| File | Task | Description |
|------|------|-------------|
| `notebooks/task1_eda.ipynb` | Task 1 | EDA + Data Cleaning |
| `notebooks/task2_sql.ipynb` | Task 2 | SQL Extraction |
| `notebooks/task3_visualization.ipynb` | Task 3 | Charts + Dashboard |
| `notebooks/task4_advanced_analytics.ipynb` | Task 4 | Stats + ML Models |
| `notebooks/task5_final.ipynb` | Task 5 | Report + Pipeline |
| `scripts/task2_queries.sql` | Task 2 | All SQL queries |
| `scripts/pipeline.py` | Task 5 | Automation script |
| `data/data_cleaned.csv` | Task 1 | Cleaned dataset |
| `data/ecommerce.db` | Task 2 | SQLite database |
| `dashboards/executive_dashboard.html` | Task 3 | Interactive dashboard |
| `reports/final_executive_report.pdf` | Task 5 | PDF report |
| `reports/analytics_report.xlsx` | Task 5 | Excel KPI export |
| `requirements.txt` | Task 5 | Python dependencies |
| `README.md` | All | Project documentation |

---

## 🏆 Skills Demonstrated Across All 5 Tasks

- ✅ Python for Data Analytics (Pandas, NumPy, Matplotlib, Seaborn, Plotly)
- ✅ SQL (SQLite, SQLAlchemy, Window Functions, CTEs, Views)
- ✅ Statistical Analysis (T-Test, Chi-Square, Confidence Intervals)
- ✅ Machine Learning (K-Means Clustering, PCA, Linear & Logistic Regression)
- ✅ Dashboard Creation (Interactive Plotly Executive Dashboard)
- ✅ Report Generation (PDF with fpdf2, Excel with openpyxl)
- ✅ Pipeline Automation (end-to-end Python script)
- ✅ GitHub Version Control (commits, tags, public repo)

---

## 🚀 How to Run Everything

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/apexplanet-data-analytics.git
cd apexplanet-data-analytics

# 2. Install all dependencies
pip install -r requirements.txt

# 3. Run notebooks in order
jupyter notebook
# → task1_eda.ipynb → task2_sql.ipynb → task3_visualization.ipynb
# → task4_advanced_analytics.ipynb → task5_final.ipynb

# 4. Or run the automated pipeline directly
python scripts/pipeline.py
```

---

## 🔗 Links

- 📂 GitHub Repository: `[your-github-link]`
- 🎥 Screen Recording: `[your-linkedin-video-link]`

---

## 🏢 About the Internship

**[ApexPlanet Software Pvt. Ltd.](https://www.apexplanet.in)**
- 📞 +91 99058 79870
- 📧 apexplanetgaya@gmail.com
- 🌐 www.apexplanet.in

---

*ApexPlanet Data Analytics Internship — Task 5 of 5 — COMPLETE! 🏁*
*© 2024 ApexPlanet Software Pvt. Ltd.*
