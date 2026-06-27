# 📊 ApexPlanet Data Analytics Internship — 30 Days

![Data Analytics](https://img.shields.io/badge/Domain-Data%20Analytics-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![Status](https://img.shields.io/badge/Status-In%20Progress-green)
![Internship](https://img.shields.io/badge/ApexPlanet-Internship-purple)

> A 30-day hands-on Data Analytics Internship by **ApexPlanet Software Pvt. Ltd.**
> Working on real-world E-commerce Sales data to build end-to-end analytics skills.

---

## 🗂️ Project Structure

```
apexplanet-data-analytics/
├── data/
│   ├── data.csv                        # Raw E-commerce dataset
│   ├── data_cleaned.csv                # Cleaned dataset (Task 1 output)
│   └── ecommerce.db                    # SQLite database (Task 2 output)
├── notebooks/
│   ├── task1_eda.ipynb                 # Task 1 — EDA Notebook
│   └── task2_sql.ipynb                 # Task 2 — SQL Notebook
├── scripts/
│   └── task2_queries.sql               # All SQL queries (Task 2)
├── reports/
│   ├── hist_totalprice.png             # Histogram — Total Price Distribution
│   ├── boxplot_quantity_price.png      # Boxplots — Quantity & Unit Price
│   ├── bar_top_countries.png           # Bar Chart — Top 10 Countries by Revenue
│   ├── bar_top_products.png            # Bar Chart — Top 10 Best-Selling Products
│   ├── line_monthly_sales.png          # Line Chart — Monthly Sales Trend
│   ├── heatmap_correlation.png         # Heatmap — Correlation Matrix
│   ├── interactive_monthly_sales.html  # Interactive Plotly Chart
│   ├── sql_q1_top_products.png         # SQL Q1 — Top Products Chart
│   ├── sql_q2_monthly_trend.png        # SQL Q2 — Monthly Trend Chart
│   ├── sql_q4_customer_segments.png    # SQL Q4 — Customer Segments Pie
│   ├── sql_q5_country_revenue.png      # SQL Q5 — Country Revenue Chart
│   ├── sql_q9_mom_growth.png           # SQL Q9 — MoM Growth Chart
│   └── sql_q10_price_category.png      # SQL Q10 — Price Category Donut
├── dashboards/                         # Power BI / Tableau dashboards (upcoming)
└── README.md
```

---

## ✅ Tasks Overview

| Task | Topic | Timeline | Status |
|------|-------|----------|--------|
| Task 1 | Foundation & Exploratory Data Analysis | 6 Days | ✅ Complete |
| Task 2 | SQL for Data Extraction | 7 Days | ✅ Complete |
| Task 3 | Data Visualization & Dashboarding | 7 Days | 🔄 Upcoming |
| Task 4 | Advanced Analytics (Basic) | 6 Days | 🔄 Upcoming |
| Task 5 | Final Report, Automation & Presentation | 4 Days | 🔄 Upcoming |

---

## 📌 Task 1 — Foundational Setup & Exploratory Data Analysis (EDA)
**Timeline:** Day 1–6

### 🎯 Objective
Set up the analytics environment, clean the E-commerce Sales dataset, and perform exploratory data analysis to uncover key business insights.

### 📦 Dataset
- **Source:** [E-commerce Data — Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
- **Description:** Transactional data from a UK-based online retail store (2010–2011)
- **Size:** ~541,000 rows × 8 columns

### 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Python 3.x | Core programming language |
| Pandas | Data loading, cleaning, manipulation |
| NumPy | Numerical operations, IQR calculations |
| Matplotlib | Static visualizations |
| Seaborn | Advanced statistical plots |
| Plotly | Interactive charts |
| Jupyter Notebook | Development environment |

### 🧹 Data Cleaning Steps
1. **Removed duplicate rows** — eliminated redundant entries
2. **Handled missing values** — dropped rows with missing `CustomerID`; filled missing `Description` with `'Unknown'`
3. **Fixed data types** — converted `InvoiceDate` to datetime; extracted Year, Month, Day columns
4. **Removed invalid records** — filtered out rows with negative `Quantity` or `UnitPrice`
5. **Removed outliers** — applied IQR method on `Quantity` and `UnitPrice`
6. **Created new feature** — added `TotalPrice = Quantity × UnitPrice`

### 📊 Visualizations Created
- 📉 **Histogram** — Distribution of Total Price per transaction
- 📦 **Boxplots** — Spread of Quantity and Unit Price
- 🌍 **Bar Chart** — Top 10 Countries by Revenue
- 🛒 **Bar Chart** — Top 10 Best-Selling Products by Quantity
- 📈 **Line Chart** — Monthly Sales Revenue Trend
- 🔥 **Heatmap** — Correlation Matrix (Quantity, UnitPrice, TotalPrice)
- 🖱️ **Interactive Chart** — Plotly Monthly Sales (HTML)

### 💡 5 Key Insights
1. **🌍 Top Market** — The UK dominates revenue, contributing the vast majority of total sales compared to all other countries.
2. **🛒 Best-Selling Product** — A specific gift/home product leads in units sold, suggesting high repeat purchase demand.
3. **📈 Peak Season** — Sales spike significantly towards Q4 (October–November), indicating strong seasonal/holiday demand.
4. **💷 Average Order Value** — Most transactions are small-to-mid range, suggesting a high volume, low ticket size business model.
5. **👥 Customer Diversity** — The dataset spans thousands of unique customers across hundreds of products, showing a broad customer base.

### 📁 Task 1 Deliverables
- ✅ `notebooks/task1_eda.ipynb` — Full EDA notebook with cleaning + visualizations + insights
- ✅ `data/data_cleaned.csv` — Cleaned and processed dataset
- ✅ `reports/` — All charts saved as PNG and HTML

---

## 📌 Task 2 — SQL for Data Extraction
**Timeline:** Day 7–13

### 🎯 Objective
Master SQL queries for data extraction and analysis by loading the cleaned E-commerce dataset into a SQLite database and answering 10 real business questions.

### 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| SQLite | Lightweight database engine (built into Python) |
| SQLAlchemy | Professional Python-to-database connector |
| Pandas `read_sql()` | Run SQL queries and return results as DataFrames |
| Jupyter Notebook | Development and documentation environment |

### 🗄️ Database Setup
- Created SQLite database: `data/ecommerce.db`
- Loaded cleaned dataset as table: `orders`
- Created reusable view: `customer_summary`

### 📚 SQL Concepts Covered

**Day 7–8: SQL Fundamentals**

| Concept | Description |
|---------|-------------|
| `SELECT` | Choose specific columns to display |
| `WHERE` | Filter rows based on conditions |
| `ORDER BY` | Sort results ascending or descending |
| `LIMIT` | Restrict number of rows returned |
| `GROUP BY` | Group rows and apply aggregate functions |
| `HAVING` | Filter groups after aggregation |
| `LIKE` | Pattern matching on text columns |

**Day 9–10: Advanced SQL**

| Concept | Description |
|---------|-------------|
| Subqueries | Nested SELECT inside another query |
| CTE (`WITH`) | Named temporary result set for clean, readable queries |
| `ROW_NUMBER()` | Assign unique row numbers within groups |
| `RANK()` | Rank rows within a partition |
| `LAG()` | Access previous row value (used for MoM growth) |
| `CREATE VIEW` | Save a query as a reusable virtual table |

**Day 11–13: Python + SQL Integration**
- Connected Python to SQLite using `SQLAlchemy`
- Executed SQL queries from Jupyter using `pandas.read_sql()`
- Built reusable Python utility functions for common queries
- Saved all queries to `scripts/task2_queries.sql`

### ❓ 10 Business Questions Answered

| # | Business Question | SQL Concept Used |
|---|-------------------|-----------------|
| Q1 | Top 5 products by revenue | GROUP BY, ORDER BY |
| Q2 | Monthly sales trend | GROUP BY Year & Month |
| Q3 | Top 10 customers by spend | GROUP BY, ORDER BY |
| Q4 | Customer segmentation by spend level | CTE + CASE WHEN |
| Q5 | Top 10 countries by revenue | GROUP BY, HAVING |
| Q6 | Best day of month for sales | GROUP BY Day |
| Q7 | Average order value per country | Subquery + AVG |
| Q8 | Products ordered only once | HAVING COUNT = 1 |
| Q9 | Month-over-month revenue growth % | CTE + LAG Window Function |
| Q10 | Revenue share by product price category | CTE + CASE WHEN |

### 💡 5 Key SQL Insights
1. **🏆 Revenue Concentration** — The top 5 products contribute a disproportionately large share of total revenue, highlighting the importance of protecting key SKUs.
2. **📈 Q4 Growth Surge** — Month-over-month LAG analysis confirmed strong revenue acceleration in October–November, validating the seasonal trend from Task 1.
3. **👥 Customer Tiers** — A small group of high-value customers (≥£5,000 spend) generates the majority of revenue — classic Pareto principle at work.
4. **🌍 UK Dominance** — The United Kingdom accounts for the vast majority of both orders and unique customers, with international markets still relatively small.
5. **💰 Mid-Range Products Win** — Revenue share analysis showed mid-range priced products (£3–£9.99) drive the highest total revenue despite premium products having higher per-unit value.

### 📁 Task 2 Deliverables
- ✅ `notebooks/task2_sql.ipynb` — Full SQL notebook with all queries + visualizations
- ✅ `scripts/task2_queries.sql` — All SQL queries saved in a `.sql` file
- ✅ `data/ecommerce.db` — SQLite database with `orders` table and `customer_summary` view
- ✅ `reports/` — Charts for all SQL business questions

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/apexplanet-data-analytics.git
cd apexplanet-data-analytics

# 2. Install required libraries
pip install pandas numpy matplotlib seaborn plotly sqlalchemy openpyxl notebook

# 3. Launch Jupyter Notebook
jupyter notebook

# 4. Run notebooks in order:
#    → notebooks/task1_eda.ipynb   (generates data_cleaned.csv)
#    → notebooks/task2_sql.ipynb   (generates ecommerce.db)
```

---

## 🏢 About the Internship

This internship is offered by **[ApexPlanet Software Pvt. Ltd.](https://www.apexplanet.in)** — a company dedicated to driving innovation through digital solutions. The program provides hands-on experience in real-world data analytics, covering the full pipeline from data cleaning to advanced analytics and presentation.

**Contact:**
- 📞 +91 99058 79870
- 📧 apexplanetgaya@gmail.com
- 🌐 [www.apexplanet.in](https://www.apexplanet.in)

---

## 👤 Intern Details

| Field | Details |
|-------|---------|
| Name | *Your Name* |
| Program | Data Analytics — 30 Days |
| Organization | ApexPlanet Software Pvt. Ltd. |
| Website | [www.apexplanet.in](https://www.apexplanet.in) |

---

*© 2024 ApexPlanet Software Pvt. Ltd. | Internship Project*
