import pandas as pd
df = pd.read_csv("Sleep_Efficiency_clean.csv")
# Create intervals of 5 from 9 to 69
age_intervals = list(range(9, 74, 5))
# Calculate the average sleep efficiency for each age range
i = 0
while i <= (len(age_intervals)-1):
    start_interval = age_intervals[i]
    end_interval = age_intervals[i+1]
    interval = df[(df["Age"] >= start_interval) and (df["Age"] < end_interval)]
    average_sleep_efficiency = df["Sleep efficiency"].mean
    table = average_sleep_efficiency.append(interval, ignore_index = True)
    i+=1

print(table)
