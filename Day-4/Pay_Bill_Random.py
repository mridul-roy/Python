# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names)
person_who_pay = random.randint(0,num_items-1)
print(f"{names[person_who_pay]} is going to buy the meal today!$")
