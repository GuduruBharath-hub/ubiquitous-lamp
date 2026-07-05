import sqlite3
import pandas as pd

conn = sqlite3.connect('data/ecommerce.db')
q = """
SELECT 
    strftime('%w', InvoiceDate) as DayNum,
    CASE CAST(strftime('%w', InvoiceDate) AS INTEGER)
        WHEN 0 THEN 'Sunday'
        WHEN 1 THEN 'Monday'
        WHEN 2 THEN 'Tuesday'
        WHEN 3 THEN 'Wednesday'
        WHEN 4 THEN 'Thursday'
        WHEN 5 THEN 'Friday'
        WHEN 6 THEN 'Saturday'
    END AS DayOfWeek,
    COUNT(DISTINCT InvoiceNo)      AS TotalOrders,
    ROUND(SUM(TotalPrice), 2)      AS TotalRevenue,
    ROUND(AVG(TotalPrice), 2)      AS AvgOrderValue
FROM orders
GROUP BY DayNum
ORDER BY TotalRevenue DESC
"""
print(pd.read_sql_query(q, conn))
conn.close()
