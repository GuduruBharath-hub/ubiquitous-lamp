# 📊 Task 4 — Advanced Analytics (Basic)

![Status](https://img.shields.io/badge/Status-Complete-success)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![SciPy](https://img.shields.io/badge/SciPy-Statistics-blue)
![Timeline](https://img.shields.io/badge/Timeline-6%20Days-purple)

> Part of the **ApexPlanet Data Analytics Internship — 30 Days**
> 🏢 [ApexPlanet Software Pvt. Ltd.](https://www.apexplanet.in)

---

## 🎯 Objective

Apply statistical analysis and basic machine learning techniques — including hypothesis testing, customer segmentation via K-Means clustering, and predictive modeling — on the cleaned E-commerce Sales dataset.

---

## 📅 Timeline Breakdown

| Days | Focus Area |
|------|------------|
| Day 21–22 | Statistical Analysis (Descriptive Stats + Hypothesis Testing + Confidence Intervals) |
| Day 23–24 | Customer Segmentation using K-Means Clustering (RFM + PCA) |
| Day 25–26 | Basic Predictive Models (Linear Regression + Logistic Regression) |

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| Pandas & NumPy | Data preparation and feature engineering |
| SciPy (`scipy.stats`) | Statistical tests — t-test, chi-square, confidence intervals |
| Scikit-Learn | Machine learning — clustering, regression, evaluation |
| Matplotlib & Seaborn | Visualizing results and model outputs |

---

## 📅 Day 21–22: Statistical Analysis

### Descriptive Statistics
Computed mean, median, standard deviation, skewness, and kurtosis for:
- `Quantity` — units ordered per transaction
- `UnitPrice` — price per unit
- `TotalPrice` — total transaction value

**Key Finding:** All three variables are right-skewed — most transactions are small, but a small number of very large orders pull the average upward.

### Hypothesis Testing

**T-Test — UK vs Non-UK Spending**

| Metric | Value |
|--------|-------|
| Null Hypothesis | UK and Non-UK customers spend the same |
| Test | Independent samples t-test |
| Significance Level | 0.05 |
| Result | Significant difference found (p < 0.05) |
| Business Insight | UK and Non-UK customers have meaningfully different spending behavior — separate marketing strategies are warranted |

**Chi-Square Test — Month vs High-Value Orders**

| Metric | Value |
|--------|-------|
| Null Hypothesis | Month has no effect on whether an order is high-value |
| Test | Chi-Square test of independence |
| Significance Level | 0.05 |
| Result | Month significantly affects order value (p < 0.05) |
| Business Insight | Seasonal timing matters — certain months consistently produce higher-value orders |

### Confidence Intervals
Computed a **95% confidence interval** for the average order value from a random sample of 1,000 transactions, giving a reliable range for the true population mean.

---

## 📅 Day 23–24: Customer Segmentation (K-Means Clustering)

### RFM Feature Engineering
Created three behavioral features per customer:

| Feature | Definition |
|---------|-----------|
| **Recency (R)** | Days since the customer's last purchase |
| **Frequency (F)** | Number of unique invoices (orders) |
| **Monetary (M)** | Total amount spent |

### Clustering Process
1. Scaled RFM features using `StandardScaler`
2. Used the **Elbow Method** to find optimal K (K=4 selected)
3. Applied **K-Means clustering** with K=4
4. Visualized clusters in 2D using **PCA**

### Customer Segments & Recommendations

| Cluster | Segment | Description | Recommendation |
|---------|---------|-------------|----------------|
| 0 | At-Risk Customers | Haven't bought recently, low frequency | Win-back campaigns, special discounts |
| 1 | Loyal Customers | Buy regularly, moderate spend | Upsell premium products |
| 2 | New / Occasional | Low frequency, recent first purchase | Nurture with onboarding emails |
| 3 | Champions | Most recent, most frequent, highest spend | Reward with loyalty programs, early access |

---

## 📅 Day 25–26: Basic Predictive Models

### Model A — Linear Regression (Predict Total Order Value)

| Metric | Result |
|--------|--------|
| Features | Quantity, UnitPrice |
| Target | TotalPrice |
| Train/Test Split | 80% / 20% |
| R² Score | *see notebook output* |
| MAE | *see notebook output* |
| RMSE | *see notebook output* |

### Model B — Logistic Regression (Predict High-Value Order)

| Metric | Result |
|--------|--------|
| Features | Quantity, UnitPrice, Month |
| Target | HighValue (1 = above median, 0 = below) |
| Train/Test Split | 80% / 20% |
| Accuracy | *see notebook output* |
| Precision | *see notebook output* |
| Recall | *see notebook output* |
| Top Feature | UnitPrice (strongest predictor) |

---

## 💡 Key Findings

1. **📊 Right-Skewed Distributions** — Most transactions are small-value; a few very large orders significantly influence the mean, making median a more reliable central measure for business decisions.
2. **🌍 Regional Spending Differences** — T-test confirmed that UK and Non-UK customers have statistically different spending patterns, supporting region-specific pricing or promotions.
3. **📅 Seasonality Affects Order Quality** — Chi-square test proved that the month of purchase is significantly linked to whether an order is high-value, validating Q4-focused marketing.
4. **👥 Four Distinct Customer Tiers** — K-Means segmentation revealed Champions, Loyal, At-Risk, and Occasional customer clusters — each requiring a different business response.
5. **🔮 UnitPrice is the Strongest Predictor** — In both regression models, UnitPrice was the most influential feature in predicting order value and high-value classification.

---

## 📁 Deliverables

- ✅ `notebooks/task4_advanced_analytics.ipynb` — Full notebook with stats + clustering + prediction models
- ✅ `reports/stat_distributions.png` — Descriptive statistics distribution plots
- ✅ `reports/stat_ttest.png` — T-test boxplot visualization
- ✅ `reports/cluster_elbow.png` — Elbow method chart for optimal K
- ✅ `reports/cluster_pca.png` — PCA 2D cluster scatter plot
- ✅ `reports/cluster_comparison.png` — RFM metrics comparison by cluster
- ✅ `reports/model_linear_regression.png` — Actual vs predicted chart
- ✅ `reports/model_confusion_matrix.png` — Logistic regression confusion matrix
- ✅ `reports/model_feature_importance.png` — Feature importance bar chart

---

## 🚀 How to Run

```bash
# Install required libraries first
pip install scipy scikit-learn statsmodels

# From the project root
jupyter notebook notebooks/task4_advanced_analytics.ipynb

# Run all cells top to bottom (Cell → Run All)
```

---

## 🔗 Links

- 📂 GitHub Repository: `[your-github-link]`
- 🎥 Screen Recording: `[your-linkedin-video-link]`

---

*ApexPlanet Data Analytics Internship — Task 4 of 5*
*© 2024 ApexPlanet Software Pvt. Ltd.*
