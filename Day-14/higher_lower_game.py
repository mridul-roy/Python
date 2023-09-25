import random
from art import vs,logo
from game_data import data
import os

def format_data(opt):
    """"This function formate the dictionary value and reture as output"""
    opt_name = opt["name"]
    opt_decri = opt["description"]
    opt_country = opt["country"]
    
    return (f"{opt_name}, is {opt_decri}, from {opt_country}")
def get_random():
    return random.choice(data)


def check_score (user_select,opt_A_follower,opt_B_follower):
    """"This function check who has more follower and return as True who has more"""
    if opt_A_follower > opt_B_follower:
        return user_select == "a"
    elif opt_B_follower > opt_A_follower:
        return user_select == "b"
def game():    
    print(logo)
    score = 0   
    should_continue = True
    opt_A = get_random()
    opt_B = get_random()

    while should_continue:
        opt_A = opt_B
        opt_B = get_random()
        while opt_A == opt_B:
            opt_B = get_random()
        
        print(f"Option A : {format_data(opt_A)}")
        print(vs)
        print(f"Option B : {format_data(opt_B)}")

        user_select = input("Who has more followers? A or B :").lower()
        opt_A_follower = opt_A["follower_count"]
        opt_B_follower = opt_B["follower_count"]
        is_correct = check_score(user_select,opt_A_follower,opt_B_follower)
        os.system('cls')
        if is_correct:
            print(logo)
            score += 1
            
            print(f"You got the right answer. Your score is {score}")
            
        else:
            print(f"Sorry, Your answer is wrong. Your score is {score}")
            should_continue = False

game()