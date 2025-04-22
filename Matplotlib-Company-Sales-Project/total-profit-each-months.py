"""
Question: Read the total profit of each month and show it using the histogram to see the most common profit ranges
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Tanmayee Dharam/OneDrive - The University of Texas at Dallas/Desktop/company_sales_data.csv")
profitList = df ['total_profit'].tolist()

## Defining labels and profit ranges
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]

plt.hist(profitList, profit_range, label = 'Profit', color='Green', edgecolor='black')

plt.xlabel('Profit Range In Dollar')
plt.ylabel('Actual Profit In Dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Total Profit For Each Months')

plt.show()