"""
Question 1: Read Total profit of all months and show it using a line plot

Total profit data provided for each month. Generated line plot must include the following properties: –
X label name = Month Number
Y label name = Total profit
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Tanmayee Dharam/OneDrive - The University of Texas at Dallas/Desktop/company_sales_data.csv")
profitList = df ['total_profit'].tolist()   #.tolist()- converting data structure to python list
monthList  = df ['month_number'].tolist()   #.tolist()- converting data structure to python list
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company Profits Per Month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()