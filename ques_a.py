# Importing library
import pandas as pd

df_trips = pd.read_csv('Trips_by_Distance.csv')   

#average Population Staying at Home 
print(df_trips[df_trips['Level'] == 'National']['Population Staying at Home'].mean().round())

# Use average distance for each trip range
df_trips['Total Distance'] = (
    df_trips['Number of Trips <1'] * 0.5 +
    df_trips['Number of Trips 1-3'] * 2 +
    df_trips['Number of Trips 3-5'] * 4 +
    df_trips['Number of Trips 5-10'] * 7.5 +
    df_trips['Number of Trips 10-25'] * 17.5 +
    df_trips['Number of Trips 25-50'] * 37.5 +
    df_trips['Number of Trips 50-100'] * 75 +
    df_trips['Number of Trips 100-250'] * 175 +
    df_trips['Number of Trips 250-500'] * 375 +
    df_trips['Number of Trips >=500'] * 600
)

# Calculating average distance per person who weren't home
df_trips['Avg Distance Per Person'] = df_trips['Total Distance'].sum() / df_trips['Population Not Staying at Home'].sum()

print(df_trips["Avg Distance Per Person"].mean().round())
