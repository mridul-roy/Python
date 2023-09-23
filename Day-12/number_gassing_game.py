import random
from art import logo

EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def game_level():
    set_level = input("Choose game level 'easy' or 'hard' :")
    if set_level == "easy":
        return EASY_LEVEL_TURN
    elif set_level == "hard":
        return HARD_LEVEL_TURN

def num_check(computer_select,guess_number,turns):
    if computer_select > guess_number:
        print("It's too low")
        return turns - 1
    elif computer_select < guess_number:
        print("It's too high")
        return turns - 1
    else:
        print("It's matched.You win.")
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    computer_select = random.randint(2,100)
    #print(f"Computer Guessd answer is :{computer_select}")

    turns = game_level()
    
    guess_number = 0

    while guess_number != computer_select :
        print(f"You have {turns} attempt to go with.")
        guess_number = int(input("Gassed a number: "))
        turns = num_check(computer_select,guess_number,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess_number != computer_select:
            print("Guess again")
game()