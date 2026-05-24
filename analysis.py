import pandas as pd
import numpy as np

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