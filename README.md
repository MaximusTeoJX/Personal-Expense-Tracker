# Expenses Tracker

This is a simple Python project that uses Pandas to analyse personal expenses from a CSV file. It calculates total spending, average spending, highest expense and spending by category.

## Description

This project reads expense data from a CSV file and provides insights such as:
- Load expenses from a CSV file
- Display first few rows of data
- Calculate total, average and highest spending
- Group spending by category
- Identify top spending categories
- Visualise spending trends through charts

It's designed as a lightweight tool for learning data analysis with Python and Pandas.

## Getting Started

### Dependencies

* Python 3.14 (or later)
* Pandas 3.0.3
* Matplotlib (for charts)
* Works on Windows 11 

### Installing

1. Clone or download this repository
```bash
git clone https://github.com/your-username/expenses-tracker.git
```

2. Navigate to the project folder
    cd expenses-tracker

3. Install required libraries
    pip install pandas
    pip install pandas matplotlib


### Executing Program

Run script: python analysis.py

## Data Visualisation

You can generate charts to better understand your spending patterns.

### 1. Expenses Over Time (Line Chart)
```python
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Amount'], marker='o', linestyle='-', color='blue')
plt.title("Expenses Over Time")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### 2. Expenses Breakdown by Category (Pie Chart)
```python
category_totals = df.groupby('Category')['Amount'].sum()

plt.figure(figsize=(6,6))
plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
plt.title("Expense Breakdown by Category")
plt.axis('equal')   # ensures the pie chart is circular
plt.tight_layout()
plt.show()
```

### 3. Monthly Expenses (Bar Chart)
```python
df['Month'] = df['Date'].dt.to_period('M')
monthly_totals = df.groupby('Month')['Amount'].sum()

plt.figure(figsize=(8,5))
monthly_totals.plot(kind='bar', color='orange')
plt.title("Monthly Expenses")
plt.xlabel("Month")
plt.ylabel("Total Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```