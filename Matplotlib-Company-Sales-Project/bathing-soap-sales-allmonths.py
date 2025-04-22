"""
Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Tanmayee Dharam/OneDrive - The University of Texas at Dallas/Desktop/company_sales_data.csv")
monthList  = df ['month_number'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()

plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Numbers')
plt.ylabel('Sales units in numbers')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Bathing Soap sales')

# Save plot with corrected file path (using raw string)
plt.savefig('C:/Users/Tanmayee Dharam/OneDrive - The University of Texas at Dallas/Desktop/Tanmayee/Excel Project/Python Matplotlib/sales_data_of_bathingsoap.png', dpi=150)
plt.show()