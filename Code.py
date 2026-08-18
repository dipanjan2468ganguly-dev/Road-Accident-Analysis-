import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib as plt

df = pd.read_csv(r"C:\Users\Debanga Mondal\OneDrive\Desktop\Python\BCT\Project\synthetic_road_accidents_2k.csv")
print(df)
print(df.head())

Data Cleaning 
df.dropna(inplace=True)

Visualization 1: Accident Risk Distribution
sb.histplot(df['accident_risk'], kde=True, color='crimson')
plt.title("Distribution of Accident Risk")
plt.show()

Visualization 2: Road Type vs Accident Risk
sb.boxplot(x='road_type', y='accident_risk', data=df, palette='cool')
plt.title("Accident Risk by Road Type")
plt.show()

Visualization 3: Weather vs Avg Risk
avg_risk_weather = df.groupby('weather')['accident_risk'].mean().sort_values()
avg_risk_weather.plot(kind='barh', color='teal')
plt.title("Average Accident Risk by Weather Condition")
plt.xlabel("Accident Risk")
plt.ylabel("Weather")
plt.show()

Visualization 4: Speed Limit vs Accident Risk
sb.scatterplot(x='speed_limit', y='accident_risk', data=df, hue='road_type')
plt.title("Speed Limit vs Accident Risk by Road Type")
plt.show()

Visualization 5: Heatmap - Numeric Correlations
plt.figure(figsize=(10, 6))
sb.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Numerical Variables")
plt.show()

Visualization 6: Time of Day Impact
sb.violinplot(x='time_of_day', y='accident_risk', data=df)
plt.title("Impact of Time of Day on Accident Risk")
plt.xticks(rotation=30)
plt.show()


Visualization 7 : Average Risk by Road Type (Bar Chart)
avg_risk = df.groupby('road_type')['accident_risk'].mean().sort_values()

avg_risk.plot(kind='bar', color='orange')
plt.title("Average Accident Risk by Road Type")
plt.xlabel("Road Type")
plt.ylabel("Accident Risk")
plt.xticks(rotation=30)
plt.show()
