#using pandas for data acquisition
import pandas as pd

#Load dataset using Pandas
df = pd.read_csv("Trips_by_Distance.csv")

#Inspect dataset
print(df.head())
print(df.info())
