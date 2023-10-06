# import csv
#
# with open("weather_data.csv") as file:
#     temperature = []
#     data = csv.reader(file)
#     for row in data:
#         if row[1] != "temp":
#
#          temperature.append(int(row[1]))
#
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# data_dic =data.to_dict()
# print(data_dic)
#
# temp_list = (data["temp"].max())
#
# print(temp_list)


#get data in callum

#retive data as dictionary
# print(data["condition"])
#retrive data as object
# print(data.day)

#get data in row

print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])


#create Dataframe

data_dic = {
    "Student": ["Any","Jams","Angela"],
    "Score": [59,43,56]
}

data = pandas.DataFrame(data_dic)
#data.to_csv("data.csv")
print(data)
