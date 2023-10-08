no_of_1 = awakenings == 1
one = df[no_of_1]
sleep_efficiency_1 = one["Sleep efficiency"]
average_sleep_efficiency_1 = sleep_efficiency_1.mean
no_of_2 = awakenings == 2
two = df[no_of_2]
sleep_efficiency_2 = two["Sleep efficiency"]
average_sleep_efficiency_2 = sleep_efficiency_2.mean
no_of_3 = awakenings == 3
three = df[no_of_3]
sleep_efficiency_3 = three["Sleep efficiency"]
average_sleep_efficiency_3 = sleep_efficiency_3.mean
no_of_4 = awakenings == 4
four = df[no_of_4]
sleep_efficiency_4 = four["Sleep efficiency"]
average_sleep_efficiency_4 = sleep_efficiency_4.mean

df2 = pd.DataFrame({"Awakenings":[0,1,2,3,4],
                      "Average Sleep Efficiency":[average_sleep_efficiency_0, average_sleep_efficiency_1, average_sleep_efficiency_2, average_sleep_efficiency_3, average_sleep_efficiency_4]})

print(df2)
