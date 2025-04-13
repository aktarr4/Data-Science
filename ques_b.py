import pandas as pd

# Load the dataset
df_trips = pd.read_csv("Trips_by_Distance.csv")


# Filter for > 10 million trips in each category
high_10_25 = df_trips[df_trips['Number of Trips 10-25'] > 10_000_000]
high_50_100 = df_trips[df_trips['Number of Trips 50-100'] > 10_000_000]

# Get the dates
dates_10_25 = set(high_10_25['Date'])
dates_50_100 = set(high_50_100['Date'])

# Compare sets
both = dates_10_25 & dates_50_100
only_10_25 = dates_10_25 - dates_50_100
only_50_100 = dates_50_100 - dates_10_25

# Print results
print(" Dates with >10M trips in BOTH 10–25 and 50–100 categories:")
print(sorted(both))

print("\n Dates with >10M trips in 10–25 only:")
print(sorted(only_10_25))

print("\n Dates with >10M trips in 50–100 only:")
print(sorted(only_50_100))
