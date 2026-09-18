# Power BI Dashboard Setup

Import `data/warehouse_operations_data.csv`.

Create these measures:

Total Orders = COUNTROWS('warehouse_operations_data')
Total Units = SUM('warehouse_operations_data'[Units])
Total Revenue = SUM('warehouse_operations_data'[Order_Revenue])
Operating Cost = SUM('warehouse_operations_data'[Total_Order_Cost])
Cost per Order = DIVIDE([Operating Cost],[Total Orders])
Cost per Unit = DIVIDE([Operating Cost],[Total Units])
Contribution = SUM('warehouse_operations_data'[Contribution])
Contribution Margin % = DIVIDE([Contribution],[Total Revenue])

Recommended visuals:
- KPI cards: Orders, Units, Revenue, Operating Cost, Cost/Order, Cost/Unit, Contribution Margin
- Clustered column: Revenue by Category
- Column: Orders by Warehouse Zone
- Bar: Cost per Unit by Category
- Bar: Units per Labour Hour by Zone
- Slicers: Category, Warehouse Zone

Use a clean one-page executive dashboard.
