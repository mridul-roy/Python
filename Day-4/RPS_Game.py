import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rnd = random.randint(0,3)

choose = input("What you want to choose ? 0 for Rock 1 for Papar and 2 for Scissor")
print("Your Choose :\n")

