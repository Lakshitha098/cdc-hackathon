import matplotlib.pyplot as plt
import seaborn as sns

# Plot temperature trends over time
plt.figure(figsize=(10, 6))
sns.lineplot(x='Date', y='Temperature', data=data)
plt.title('Global Temperature Trends Over Time')
plt.xlabel('Year')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Climate Data')
plt.show()
