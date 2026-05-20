import pandas as pd

df = pd.read_csv(r"c:\Users\nc\Downloads\website wata.csv")

print(df.head())
print(df.info())

# Total page views
print("Total Page Views:", df['Page Views'].sum())

# Average bounce rate
print("Average Bounce Rate:", df['Bounce Rate'].mean())

# Average session duration
print("Average Session Duration:", df['Session Duration'].mean())

# Average conversion rate
print("Average Conversion Rate:", df['Conversion Rate'].mean())

traffic = df.groupby('Traffic Source')['Page Views'].sum()

print(traffic)

import matplotlib.pyplot as plt

traffic.plot(kind='bar')

plt.title("Traffic Sources")
plt.xlabel("Source")
plt.ylabel("Page Views")

plt.show()

df['Bounce Rate'].hist()

plt.title("Bounce Rate Distribution")

plt.show()

df['Session Duration'].hist()

plt.title("Session Duration Distribution")

plt.show()

df['Bounce Rate'].hist()

plt.title("Bounce Rate Distribution")

plt.show()


best_source = traffic.idxmax()

print("Best Traffic Source:", best_source)


print(df['Conversion Rate'].mean())