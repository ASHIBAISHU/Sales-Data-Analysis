import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('sales_data.csv')

# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'])

# Group by Product and Date, summing Sales and Profit
grouped_data = data.groupby(['Date', 'Product']).sum().reset_index()

# Print the grouped data
print(grouped_data)

# Plotting sales over time
plt.figure(figsize=(10, 5))
for product in grouped_data['Product'].unique():
    product_data = grouped_data[grouped_data['Product'] == product]
    plt.plot(product_data['Date'], product_data['Sales'], marker='o', label=product)

plt.title('Sales Over Time by Product')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot
plt.savefig('sales_over_time.png')
plt.show()
