import pandas as pd

#Load the dataset
df_trips = pd.read_csv("Trips_by_Distance.csv")

# rows where trips exceed 10 million in each range
trips_over_10m_10_25 = df_trips[df_trips['Number of Trips 10-25'] > 10_000_000]
trips_over_10m_50_100 = df_trips[df_trips['Number of Trips 50-100'] > 10_000_000]

# Extract the dates from the filtered data
dates_with_10_25 = set(trips_over_10m_10_25['Date'])
dates_with_50_100 = set(trips_over_10m_50_100['Date'])

# Identify overlapping and unique dates between the two sets
common_dates = dates_with_10_25 & dates_with_50_100
unique_to_10_25 = dates_with_10_25 - dates_with_50_100
unique_to_50_100 = dates_with_50_100 - dates_with_10_25

# Display the findings
print("Dates where both trip ranges (10–25 and 50–100) exceeded 10 million:")
print(sorted(common_dates))

print("\nDates where only the 10–25 trip range exceeded 10 million:")
print(sorted(unique_to_10_25))

print("\nDates where only the 50–100 trip range exceeded 10 million:")
print(sorted(unique_to_50_100))
