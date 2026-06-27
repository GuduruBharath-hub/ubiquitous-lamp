
-- ============================================================
-- ApexPlanet Data Analytics Internship — Task 2
-- SQL Queries for E-commerce Data Extraction
-- ============================================================

-- Q1: Top 5 Products by Revenue
SELECT Description, ROUND(SUM(TotalPrice),2) AS Revenue
FROM orders GROUP BY Description
ORDER BY Revenue DESC LIMIT 5;

-- Q2: Monthly Sales Trend
SELECT Year, Month, ROUND(SUM(TotalPrice),2) AS MonthlyRevenue
FROM orders GROUP BY Year, Month ORDER BY Year, Month;

-- Q3: Top 10 Customers by Spend
SELECT CustomerID, Country, ROUND(SUM(TotalPrice),2) AS TotalSpend,
       COUNT(DISTINCT InvoiceNo) AS TotalOrders
FROM orders GROUP BY CustomerID ORDER BY TotalSpend DESC LIMIT 10;

-- Q4: Customer Segmentation by Spend
WITH CustomerSpend AS (
    SELECT CustomerID, SUM(TotalPrice) AS TotalSpend
    FROM orders GROUP BY CustomerID
)
SELECT
    CASE
        WHEN TotalSpend >= 5000 THEN 'High Value'
        WHEN TotalSpend >= 1000 THEN 'Mid Value'
        WHEN TotalSpend >= 200  THEN 'Low Value'
        ELSE 'Occasional'
    END AS Segment,
    COUNT(*) AS CustomerCount,
    ROUND(SUM(TotalSpend),2) AS SegmentRevenue
FROM CustomerSpend GROUP BY Segment ORDER BY SegmentRevenue DESC;

-- Q5: Top 10 Countries by Revenue
SELECT Country, ROUND(SUM(TotalPrice),2) AS Revenue,
       COUNT(DISTINCT CustomerID) AS Customers
FROM orders GROUP BY Country ORDER BY Revenue DESC LIMIT 10;

-- Q9: Month-over-Month Growth (Window Function)
WITH MonthlyRev AS (
    SELECT Year, Month, ROUND(SUM(TotalPrice),2) AS Revenue
    FROM orders GROUP BY Year, Month
)
SELECT Year, Month, Revenue,
    LAG(Revenue) OVER (ORDER BY Year, Month) AS PrevRevenue,
    ROUND((Revenue - LAG(Revenue) OVER (ORDER BY Year, Month))
        / LAG(Revenue) OVER (ORDER BY Year, Month) * 100, 2) AS GrowthPct
FROM MonthlyRev ORDER BY Year, Month;
