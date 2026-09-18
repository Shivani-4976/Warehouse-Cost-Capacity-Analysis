import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/warehouse_operations_data.csv')

print('Shape:', df.shape)
print('\nMissing values:\n', df.isna().sum())
print('\nOverall KPIs')
print('Orders:', len(df))
print('Units:', df['Units'].sum())
print('Revenue:', round(df['Order_Revenue'].sum(),2))
print('Operating Cost:', round(df['Total_Order_Cost'].sum(),2))
print('Cost/Order:', round(df['Total_Order_Cost'].mean(),2))
print('Cost/Unit:', round(df['Total_Order_Cost'].sum()/df['Units'].sum(),2))
print('Contribution:', round(df['Contribution'].sum(),2))
print('Contribution Margin %:', round(df['Contribution'].sum()/df['Order_Revenue'].sum()*100,2))

category = df.groupby('Category').agg(
    Orders=('Order_ID','count'),
    Units=('Units','sum'),
    Revenue=('Order_Revenue','sum'),
    Operating_Cost=('Total_Order_Cost','sum'),
    Contribution=('Contribution','sum')
)
category['Cost_per_Order'] = category['Operating_Cost']/category['Orders']
category['Cost_per_Unit'] = category['Operating_Cost']/category['Units']
print('\nCategory analysis:\n', category.sort_values('Revenue', ascending=False))

zone = df.groupby('Warehouse_Zone').agg(
    Orders=('Order_ID','count'),
    Units=('Units','sum'),
    Revenue=('Order_Revenue','sum'),
    Operating_Cost=('Total_Order_Cost','sum')
)
zone['Cost_per_Order'] = zone['Operating_Cost']/zone['Orders']
zone['Units_per_Labour_Hour'] = zone['Units']/(df.groupby('Warehouse_Zone')['Total_Handling_Time_Min'].sum()/60)
print('\nZone analysis:\n', zone)

category['Revenue'].plot(kind='bar', title='Revenue by Category')
plt.tight_layout()
plt.savefig('../screenshots/revenue_by_category.png', dpi=180)
plt.close()
