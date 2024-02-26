import pandas as pd

# Read the data from the spreadsheet
df = pd.read_csv('C:/Users/sarpo/Downloads/sales.csv')
print(df)

# Collect all of the sales from each month into a single list
sales_data = df['sales'].tolist()
print(sales_data)

# Output the total sales across all months
total_sales = sum(sales_data)


# Calculate monthly changes as a percentage
df['monthly_change_pct'] = df['sales'].pct_change() * 100

# Calculate the average
average_sales = df['sales'].mean()

# Months with the highest and lowest sales
highest_sales_month = df.loc[df['sales'].idxmax()]['month']
lowest_sales_month = df.loc[df['sales'].idxmin()]['month']

# Output a summary of the results to a spreadsheet
summary_df = pd.DataFrame({
    'Total Sales': [total_sales],
    'Average Sales': [average_sales],
    'Highest Sales Month': [highest_sales_month],
    'Lowest Sales Month': [lowest_sales_month]
})

# Write the summary to a new CSV file
summary_df.to_csv('C:/Users/sarpo/Downloads/summary.csv', index=False)

print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sales Month:", highest_sales_month)
print("Lowest Sales Month:", lowest_sales_month)
print("Summary saved to summary.csv")