first = df_trips[df_trips['Number of Trips 10-25'] > 10000000]['Date']
second = df_trips[df_trips['Number of Trips 50-100'] > 10000000]['Date']

print(f"The number of dates where the number of trips between 10 and 25 miles is above 10 million is {len(first)}")
print(f"The number of dates where the number of trips between 50 and 100 miles is above 10 million is {len(second)}")
