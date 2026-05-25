import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("expenses.csv")  # Load the expense data from the CSV file into a pandas DataFrame for analysis

# Display first 5 rows to view data structure
print("Expense Data:")
print(df.head())        # Display the first 5 rows of the DataFrame to get an overview of the data structure and contents

# Total spending
total_spending = df["Amount"].sum()     # Calculate the total spending by summing the "Amount" column in the DataFrame
print("\nTotal Spending: $", total_spending)

# Average spending
average_spending = np.mean(df["Amount"])     # Calculate the average spending by taking the mean of the "Amount" column
print("Average Spending: $", round(average_spending, 2))

# Highest expense
highest_expense = df["Amount"].max()        # Find the highest expense by taking the maximum value from the "Amount" column
print("Highest Expense: $", highest_expense)

# Spending by category
category_summary = df.groupby("Category")["Amount"].sum()       # Group the DataFrame by the "Category" column and sum the "Amount" for each category to get the total spending per category 
print("\nSpending by Category:")
print(category_summary)

# Sort highest spending categories
sorted_categories = category_summary.sort_values(ascending=False)       # Sort the category summary in descending order to identify the categories with the highest spending

print("\nTop Spending Categories:")
print(sorted_categories)


# Expense Trend Over Time
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)      # Converts the Date column from strings into proper datetime objects using day/month/year format so it can be used for time‑based operations like sorting, grouping, and plotting
df = df.sort_values('Date')     # Sorts the entire DataFrame by the Date column in ascending order. This ensures that when we plot the data, the dates will be in chronological order, which is important for accurately visualizing trends over time

plt.figure(figsize=(10,5))      # figsize=(10,5) sets the width to 10 inches and height to 5 inches, controlling how big the chart looks
plt.plot(df['Date'], df['Amount'], marker='o', linestyle='-', color='blue')     # Plots df['Date'] on x‑axis and df['Amount'] on y‑axis with blue circles connected by blue solid lines
plt.title("Expenses Over Time")     # Adds a title to the line chart
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)        # Rotate the x-axis labels by 45 degrees for better readability, especially if there are many data points or long date labels
plt.tight_layout()      # Automatically adjusts spacing so labels, titles, and ticks fit neatly within the figure without being cut off
plt.show()

# Category Breakdown Pie Chart
category_totals = df.groupby('Category')['Amount'].sum()        # Group the DataFrame by the "Category" column and sum the "Amount" for each category to get the total spending per category

plt.figure(figsize=(6,6))
plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)    # Draws a pie chart with category_totals as slice sizes, category names as labels, percentages shown to one decimal place, and rotated to start at 140° for readability
plt.title("Expense Breakdown by Category")
plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular
plt.tight_layout()
plt.show()

# Monthly Spending Bar Chart
df['Month'] = df['Date'].dt.to_period('M')      # Creates a new column 'Month' by extracting the month and year from the 'Date' column, resulting in a period format like '2026-01' for January 2026
monthly_totals = df.groupby('Month')['Amount'].sum()        # Groups the data by month and sums the spending amounts to get monthly totals

plt.figure(figsize=(8,5))   
monthly_totals.plot(kind='bar', color='orange')     # Plots the monthly totals as an orange bar chart
plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Total Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()