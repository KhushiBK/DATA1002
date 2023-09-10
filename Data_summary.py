import pandas as pd
import numpty as np


df=pd.read_csv('Sleep_Efficiency_cleaned.csv')


#FINDING Max AND Min of age
max = df['Age'].max()
min = df['Age'].min()
average = df['Age'].mean()
r_value = df.corr()
 
print(max)
print(min)
print(average)
print(r_value)


