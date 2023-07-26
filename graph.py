# Program to input the total sales from each month and plot on a graph
# Program created on July 23, 2023
# Program created by Ashley Colbert

# Imports

import matplotlib

# Inputs

print("Please enter the total sales for each month to date.")
print("Write '0' for any month not completed yet.")
January = float(input("Enter total sales for January: "))
February = float(input("Enter total sales for February: "))
March = float(input("Enter total sales for March: "))
April = float(input("Enter total sales for April: "))
May = float(input("Enter total sales for May: "))
June = float(input("Enter total sales for June: "))
July = float(input("Enter total sales for July: "))
August = float(input("Enter total sales for August: "))
September = float(input("Enter total sales for September: "))
October = float(input("Enter total sales for October: "))
November = float(input("Enter total sales for November: "))
December = float(input("Enter total sales for December: "))

from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y = [January, February, March, April, May, June, July, August, September, October, November, December]

fig, ax = plt.subplots()

ax.bar(x, y, align='center')

ax.set_title('Total Yearly Sales by Month')
ax.set_ylabel('Total Sales($)')
ax.set_xlabel('Month')

ax.set_xticks(x)
ax.set_xticklabels(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

plt.show()