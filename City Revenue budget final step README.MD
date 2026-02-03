# 📊 City Revenue Budget Analysis

## Objective
This project analyzes city-level revenue data by comparing **Budget vs Actual revenue**, evaluating **budget utilization efficiency**, and identifying **performance trends** across cities, fiscal years, and revenue types.

The goal is to use data analytics to measure financial performance and support data-driven decision making.

## Step 1: Import Libraries and Load Dataset
We import required libraries and load the dataset into pandas DataFrame.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("City_Revenue_Budget.csv")
df.head()

## Step 2: Understanding Dataset Structure
Check shape, columns, data types and statistical summary.
print(df.shape)
print(df.columns)
df.info()
df.describe()
## Step 3: Handling Missing Values
Missing values in Budget and Actual are replaced with 0.
df.isnull().sum()

df['Budget'] = df['Budget'].fillna(0)
df['Actual'] = df['Actual'].fillna(0)

## Step 4: Removing Duplicate Records
Duplicate rows are removed for accurate analysis.
df.drop_duplicates(inplace=True)
df.shape
## Step 5: Cleaning Column Names
Standardizing column names for easier access.
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df.columns

## Step 6: Converting Data Types
Fiscal year to integer, Budget and Actual to numeric.
df['fiscal_year'] = df['fiscal_year'].astype(int)
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['actual'] = pd.to_numeric(df['actual'], errors='coerce')

## Step 7: Creating Utilization Percentage
Utilization % = (Actual / Budget) × 100
df['utilization_percentage'] = (df['actual'] / df['budget']) * 100
df.head()

## Step 8: Categorizing Budget Performance
Cities are categorized as Over Utilized or Under Utilized.
df['performance'] = np.where(df['utilization_percentage'] > 100,
                             'Over Utilized', 'Under Utilized')
df[['city_name','performance']].head()

## Step 9: City-wise Revenue Summary
Total Budget and Actual revenue for each city.
city_summary = df.groupby('city_name')[['budget','actual']].sum().reset_index()
city_summary.sort_values(by='actual', ascending=False).head(10)
## Step 10: Revenue Type Analysis
Identify top revenue generating sources.
rev_summary = df.groupby('revenue_type')['actual'].sum().reset_index()
rev_summary.sort_values(by='actual', ascending=False)

## Step 11: Pivot Table (Fiscal Year × Revenue Type)
Shows revenue pattern over years.
pivot = pd.pivot_table(df,
                       values='actual',
                       index='fiscal_year',
                       columns='revenue_type',
                       aggfunc='sum')
pivot

## Step 12: Correlation Analysis
Relationship between Budget, Actual and Utilization.
df[['budget','actual','utilization_percentage']].corr()

## Step 13: Top 10 Cities by Actual Revenue
top10 = city_summary.sort_values(by='actual', ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(data=top10, x='actual', y='city_name')
plt.title('Top 10 Cities by Actual Revenue')
plt.show()
## Step 14: Fiscal Year-wise Revenue Trend
year_summary = df.groupby('fiscal_year')['actual'].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(data=year_summary, x='fiscal_year', y='actual', marker='o')
plt.title('Fiscal Year Revenue Trend')
plt.show()
## Step 15: Budget vs Actual Comparison
year_budget = df.groupby('fiscal_year')[['budget','actual']].sum().reset_index()

year_budget.plot(x='fiscal_year', kind='line', figsize=(10,6))
plt.title('Budget vs Actual Over Years')
plt.show()
## Step 16: Revenue Contribution by Type
top_rev = rev_summary.sort_values(by='actual', ascending=False).head(5)

plt.figure(figsize=(8,8))
plt.pie(top_rev['actual'], labels=top_rev['revenue_type'], autopct='%1.1f%%')
plt.title('Top Revenue Types Contribution')
plt.show()

## Step 17: Distribution of Actual Revenue (Outlier Treated)
low = df['actual'].quantile(0.01)
high = df['actual'].quantile(0.99)

filtered = df[(df['actual'] > low) & (df['actual'] < high)]

plt.figure(figsize=(10,6))
sns.histplot(filtered['actual'], bins=30, kde=True)
plt.title('Distribution of Actual Revenue')
plt.show()


## Final Conclusion

- Some cities consistently exceed their budgets showing strong revenue performance.
- Few cities underutilize budget indicating planning gaps.
- Certain revenue types dominate city income.
- Strong positive correlation exists between Budget and Actual revenue.
- Revenue shows growth trend across fiscal years.

This analysis demonstrates how data analytics can evaluate financial efficiency and guide better budget planning.
