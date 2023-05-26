# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
c_height = float(height)
c_weight = float(weight)

bmi = c_weight / c_height ** 2

print(int(bmi))