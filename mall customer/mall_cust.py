import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#Load the dataset
df = pd.read_csv("mall customer\Mall_Customers.csv")   

print(df.shape)       
print(df.head())      

#Drop unnecessary column
df = df.drop("CustomerID", axis=1)

#Encode 'Gender' (Male=1, Female=0)
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

#Check for missing values
print("Missing values:\n", df.isnull().sum())

#Feature scaling (standardization)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

#Convert back to DataFrame for clarity
scaled_df = pd.DataFrame(scaled_data, columns=df.columns)

print(scaled_df.head())


X = scaled_df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 2: Use Elbow Method to find best k
wcss = []  # Within Cluster Sum of Squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot Elbow curve
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Step 3: Train KMeans with chosen number of clusters (e.g., k=5)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Step 4: Add cluster labels to DataFrame
scaled_df['Cluster'] = y_kmeans

print(scaled_df.head())