import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Example customer data
data = {
    "CustomerID": [1, 2, 3, 4, 5, 6],
    "Annual Income (k$)": [15, 16, 17, 45, 46, 47],
    "Spending Score (1-100)": [39, 81, 6, 77, 40, 76]
}

df = pd.DataFrame(data)

# Clustering (2 groups)
kmeans = KMeans(n_clusters=2, random_state=0).fit(df[["Annual Income (k$)", "Spending Score (1-100)"]])
df["Cluster"] = kmeans.labels_

print(df)

# Plot clusters
plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"], c=df["Cluster"])
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation")
plt.show()
