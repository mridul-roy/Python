print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#Write your code below this line 👇

first_round = input('You are on a cross road.Choose "left" or "right"\n').lower()

if first_round == "right":
  second_round = input(
    'You reached on a bank of river."swim"for cross the river and "wait" wait for boat.Choose "wait" or "swim"\n'
  ).lower()
  #continue game
  if second_round == "wait":
    third_round = input(
      'You reached in a house which has many collered door. Choose one "red" or "blue" or "yellow" or "other"\n'
    ).lower()
    if third_round == "red":
      print("Game Over. You are in fire")

    elif third_round == "blue":
      print("Game Over. Blast attack on you.")

    elif third_round == "yellow":
      print("You got the trasure. You win !!!")
    else:
      print("Game Over.")

  else:
    print("Game Over. One sark attack on you.")
else:
  print("Game Over. You fall into a hole.")

