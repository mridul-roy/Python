import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


color = data["Primary Fur Color"]
#total = data["Primary Fur Color"].count()

Gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
Red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

print(Gray_squirrel_count)
print(Red_squirrel_count)
print(Black_squirrel_count)


color_dic = {
    "Fur Color": ["Gray","Red","Black"],
    "Count": [Gray_squirrel_count,Red_squirrel_count,Black_squirrel_count]
}


n_data = pandas.DataFrame(color_dic)

print(n_data)

n_data.to_csv("squirrel.csv")


#print(total)
#print(color)