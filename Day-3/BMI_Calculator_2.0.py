# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
c_height = float(height)
c_weight = float(weight)

bold = '\033[1m'

bmi = round(c_weight / c_height**2)

if bmi <= 18:
  print(f"Your BMI is {bmi}, you are \033[1munderweight.\033") #use \033[1mTEXT\-33 --> for bold the String]
  
elif bmi > 18.5 and bmi <= 25:
  print(f"Your BMI is {bmi}, you have a \033[1mnormal weight.\033")

elif bmi > 25 and bmi <= 30:
  print(f"Your BMI is {bmi}, you are stightly \033[1moverweight.\033")

elif bmi > 30 and bmi <= 35:
  print(f"Your BMI  is {bmi}, you are \033[1mobese.\033")

else:
  print(f"Your BMI is {bmi}, you are \033[1mclinically obese.\033")


