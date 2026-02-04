# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 15:16:00 2026

@author: Prof. Arshad Ahmed
"""

import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset (update path if needed)
df = pd.read_csv("online_retail.csv", encoding="latin1")
# Look at the first few rows
df.head()


df.shape
df.columns
df.dtypes




df.describe()



df.isnull().sum()


df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
df[['Quantity', 'UnitPrice', 'TotalPrice']].head()


df.sort_values(by='TotalPrice', ascending=False).head()
large_orders = df[df['Quantity'] > 50]
large_orders.head()


uk_data = df[df['Country'] == 'United Kingdom']
uk_data.head()



sales_by_country = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
sales_by_country.head()


top_countries = sales_by_country.head(5)
plt.bar(top_countries.index, top_countries.values)
plt.title('Top 5 Countries by Total Sales')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.show()




df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
daily_sales = df.groupby(df['InvoiceDate'].dt.date)['TotalPrice'].sum()


plt.plot(daily_sales.index, daily_sales.values)
plt.title('Daily Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.show()





large=df[df['Quantity'] > 50]
large.shape
