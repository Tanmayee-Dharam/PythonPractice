"""
Question: Calculate total sale data for last year for each product and show it using a Pie chart
Note: In Pie chart display Number of units sold per year for each product in percentage.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Tanmayee Dharam/OneDrive - The University of Texas at Dallas/Desktop/company_sales_data.csv")
monthList  = df ['month_number'].tolist()

#Defining labels and sales data
labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(),
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]

#Creating the pie chart
plt.axis("equal") #ensures that pie is drawn as a circle
plt.pie(salesData, labels=labels, autopct='%1.1f%%')

plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()