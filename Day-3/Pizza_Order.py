# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
bill = 0
#Write your code below this line 👇

if size == "S":
    bill = 15
if size == "M":
   bill = 20
if size == "L":
    bill = 25
if add_pepperoni == "Y" and size == "S":
    bill +=2
if add_pepperoni == "Y" and size == "M":
    bill +=3
if add_pepperoni == "Y" and size == "L":
    bill += 3 
if add_pepperoni == "N" :
    bill = bill
if extra_cheese == "Y":
    bill += 1
if extra_cheese == "N":
  bill = bill

  print(f"Toatal bil : ${bill}")
 
else:
  print ("Cancal Order")