# 📊 ApexPlanet Data Analytics Internship — 30 Days

![Data Analytics](https://img.shields.io/badge/Domain-Data%20Analytics-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Status](https://img.shields.io/badge/Status-In%20Progress-green)
![Internship](https://img.shields.io/badge/ApexPlanet-Internship-purple)

---

## 🗂️ Project Structure

```
apex-task-1/
├── data/
│   ├── data.csv                   # Raw E-commerce dataset
│   └── data_cleaned.csv           # Cleaned dataset (output of Task 1)
├── notebooks/
│   └── task1_eda.ipynb            # Task 1 — EDA Notebook
├── scripts/                       # Python utility scripts (upcoming tasks)
├── reports/
│   ├── hist_totalprice.png        # Histogram — Total Price Distribution
│   ├── boxplot_quantity_price.png # Boxplots — Quantity & Unit Price
│   ├── bar_top_countries.png      # Bar Chart — Top 10 Countries by Revenue
│   ├── bar_top_products.png       # Bar Chart — Top 10 Best-Selling Products
│   ├── line_monthly_sales.png     # Line Chart — Monthly Sales Trend
│   ├── heatmap_correlation.png    # Heatmap — Correlation Matrix
│   └── interactive_monthly_sales.html  # Interactive Plotly Chart
├── dashboards/                    # Power BI / Tableau dashboards (upcoming)
└── README.md
```

---

## 📌 Task 1 — Foundational Setup & Exploratory Data Analysis (EDA)

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
4. **Removed invalid records** — filtered out rows with negative `Quantity` or `UnitPrice` (cancellations/errors)
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

1. **🌍 Top Market** — The UK dominates revenue, contributing the vast majority of total sales compared to other countries.
2. **🛒 Best-Selling Product** — A specific gift/home product leads in units sold, suggesting high repeat purchase demand.
3. **📈 Peak Season** — Sales spike significantly towards Q4 (October–November), indicating strong seasonal demand likely driven by holiday shopping.
4. **💷 Average Order Value** — Most transactions are small-to-mid range, suggesting a high volume, low ticket size business model.
5. **👥 Customer Diversity** — The dataset spans thousands of unique customers across hundreds of products, indicating a broad and diverse customer base.

### 📁 Deliverables

- ✅ `notebooks/task1_eda.ipynb` — Full EDA notebook with cleaning + visualizations + insights
- ✅ `data/data_cleaned.csv` — Cleaned and processed dataset
- ✅ `reports/` — All charts saved as PNG and HTML

---