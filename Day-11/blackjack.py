import random
from art import logo
import os


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) > 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw!!!"
  elif computer_score == 0:
    return "You lose."
  elif user_score == 0:
    return "You win!!!"
  elif user_score > 21:
    return "You lose."
  elif computer_score > 21:
    return "Computer Lose."
  elif computer_score > user_score:
    return "Computer win."
  else:
    return "You win"

def game():
  print(logo)
  user_cards = []
  computer_cards = []

  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"You have {user_cards} with total {user_score}")
    print(f"Computer first card {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      pick_another = input("Pick another card ('y' or 'n') : ")
      if pick_another == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"   Your final hand: {user_cards}, final score: {user_score}")
  print(
      f"   Computer's final hand: {computer_cards}, final score: {computer_score}"
  )
  print(compare(user_score, computer_score))

while input("Do you want to play again? 'y' for continue 'n' for exit :") == "y":
  os.system('cls')
  game()








