import dask
# Disable Arrow-based string support
dask.config.set({"dataframe.convert-string": False})

import time
import pandas as pd
import dask.dataframe as dd

#simulated processor counts (note: doesn't change actual execution)
processor_list = [10, 20]
execution_times = {}

#Load the dataset using Pandas
df = pd.read_csv("Trips_by_Distance.csv")

#2. Ensure numeric columns are properly formatted
df["Number of Trips 10-25"] = pd.to_numeric(df["Number of Trips 10-25"], errors="coerce")
df["Number of Trips 50-100"] = pd.to_numeric(df["Number of Trips 50-100"], errors="coerce")
# Optional: Convert text columns
# df["Date"] = df["Date"].astype(str)

#Create a Dask DataFrame with defined partitions
ddf = dd.from_pandas(df, npartitions=4)

#Apply filters and measure computation time
for core_count in processor_list:
    print(f"\nSimulating with {core_count} processors: ")
    timer_start = time.time()

    trips_10_25 = ddf[ddf["Number of Trips 10-25"] > 1e7][["Date", "Number of Trips 10-25"]].compute()
    trips_50_100 = ddf[ddf["Number of Trips 50-100"] > 1e7][["Date", "Number of Trips 50-100"]].compute()

    elapsed = time.time() - timer_start
    execution_times[core_count] = elapsed

    print(f"  Rows >10M (10-25): {len(trips_10_25)}")
    print(f"  Rows >10M (50-100): {len(trips_50_100 )}")
    print(f"  Time: {elapsed:.2f}s")

#Display summary of timing
print("\nExecution Time Summary: ")
for proc, duration in execution_times.items():
    print(f"  {proc} processors: {duration:.2f}s")
