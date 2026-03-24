import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Unemployment.csv")

df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])

print(df.head())

plt.figure(figsize=(8,4))
sns.lineplot(data=df, x='Date', y='Estimated Unemployment Rate (%)', hue='Region')
plt.title("Unemployment Rate Over Time")
plt.show()
