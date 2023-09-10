import csv

with open("Sleep_Efficiency.csv", "r") as file:
  csv_reader = csv.reader(file)
  data_list = []
  for row in csv_reader:
    if "" in row:
      pass
    else:
      data_list.append(row)
# data_list only has rows of data with no missing data

# Now writing the data_list data into a new csv file, while removing the columns bedtime and wakeup time

  with open("Sleep_Efficiency_clean.csv", "w") as new_file:
    csv_writer = csv.writer(new_file)
    for row in data_list:
      csv_writer.writerow(row[0], row[1], row[2], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14])      
