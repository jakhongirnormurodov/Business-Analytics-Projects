import pandas as pd
import matplotlib.pyplot as plt

# Example sales data
data = {
    "Region": ["North", "South", "East", "West", "North", "South"],
    "Sales": [2000, 3000, 1500, 4000, 2500, 3200],
    "Product": ["A", "A", "B", "B", "C", "C"]
}

df = pd.DataFrame(data)

# Total sales by region
sales_by_region = df.groupby("Region")["Sales"].sum()
print("Sales by region:")
print(sales_by_region)

# Plot
sales_by_region.plot(kind="bar", title="Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
