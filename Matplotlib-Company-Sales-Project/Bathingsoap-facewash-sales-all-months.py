"""
Question: Read Bathing soap facewash of all months and display it using the Subplot
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/Tanmayee Dharam/OneDrive - The University of Texas at Dallas/Desktop/company_sales_data.csv")
monthList  = df['month_number'].tolist()
bathingsoap = df['bathingsoap'].tolist()
faceWashSalesData = df['facewash'].tolist()

f, axarr = plt.subplots(2, sharex=True)

# Plot 1: Bathing soap sales
axarr[0].plot(monthList, bathingsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[0].grid(True)

# Plot 2: Facewash sales
axarr[1].plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')
axarr[1].grid(True)

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()



