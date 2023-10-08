import pandas as pd
df = pd.read_csv("Sleep_Efficiency_clean")
# Create intervals of 10 from 5 to 70
age_intervals = list(range(5, 70, 5))
# Calculate the average sleep efficiency for each age range
