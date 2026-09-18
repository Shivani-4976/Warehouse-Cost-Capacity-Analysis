-- SQL Server analysis for Warehouse Cost & Capacity Analysis

-- 1. Overall KPIs
SELECT COUNT(*) AS Total_Orders,
       SUM(Units) AS Total_Units,
       SUM(Order_Revenue) AS Total_Revenue,
       SUM(Total_Order_Cost) AS Total_Operating_Cost,
       AVG(Total_Order_Cost) AS Avg_Cost_Per_Order,
       SUM(Total_Order_Cost)/NULLIF(SUM(Units),0) AS Avg_Cost_Per_Unit,
       SUM(Contribution) AS Contribution
FROM warehouse_orders;

-- 2. Category performance
SELECT Category,
       COUNT(*) AS Orders,
       SUM(Units) AS Units,
       SUM(Order_Revenue) AS Revenue,
       SUM(Total_Order_Cost) AS Operating_Cost,
       SUM(Contribution) AS Contribution
FROM warehouse_orders
GROUP BY Category
ORDER BY Revenue DESC;

-- 3. Zone performance
SELECT Warehouse_Zone,
       COUNT(*) AS Orders,
       SUM(Units) AS Units,
       SUM(Order_Revenue) AS Revenue,
       SUM(Total_Order_Cost) AS Operating_Cost
FROM warehouse_orders
GROUP BY Warehouse_Zone
ORDER BY Orders DESC;

-- 4. Cost per unit by category
SELECT Category,
       SUM(Total_Order_Cost)/NULLIF(SUM(Units),0) AS Cost_Per_Unit
FROM warehouse_orders
GROUP BY Category
ORDER BY Cost_Per_Unit DESC;

-- 5. Labour productivity
SELECT Warehouse_Zone,
       SUM(Units)/(SUM(Total_Handling_Time_Min)/60.0) AS Units_Per_Labour_Hour,
       COUNT(*)/(SUM(Total_Handling_Time_Min)/60.0) AS Orders_Per_Labour_Hour
FROM warehouse_orders
GROUP BY Warehouse_Zone
ORDER BY Units_Per_Labour_Hour DESC;
