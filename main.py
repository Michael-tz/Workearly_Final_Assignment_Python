import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('finance_liquor_sales_2016-2019.csv')

df_grouped = df.groupby(['zip_code', 'sale_dollars']).sum()
print(df_grouped['item_number'].head(1))

plt.figure()
plt.scatter(df['zip_code'],df['bottles_sold'],c=df['sale_dollars'],cmap='Set3')
plt.xlabel('Zip_Code')
plt.ylabel('Bottles Sold')
plt.show()

