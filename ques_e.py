import pandas as pd
# Plotting the average number of trips by distance category
import matplotlib.pyplot as plt


# List of distance trip columns
trip_cols = [
    'Number of Trips <1',
    'Number of Trips 1-3',
    'Number of Trips 3-5',
    'Number of Trips 5-10',
    'Number of Trips 10-25',
    'Number of Trips 25-50',
    'Number of Trips 50-100',
    'Number of Trips 100-250',
    'Number of Trips 250-500',
    'Number of Trips >=500'
]

# Calculate average for each trip category
avg_trips = df_trips[trip_cols].mean()

# Plotting bar chart
plt.figure(figsize=(12,6))
avg_trips.plot(kind='bar', color='pink', edgecolor='black')
plt.title('Average Number of Trips by Distance Category')
plt.xlabel('Distance Range')
plt.ylabel('Average Number of Trips')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
