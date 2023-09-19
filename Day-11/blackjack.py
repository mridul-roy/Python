import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    
user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    
    return sum(cards)

is_game_over = False

while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    if user_score > 21  or user_score == 0 or computer_score == 0 :
        is_game_over = True
    else:
        user_choose_card = input("Do you want to take another card 'y' for yes or 'n' for pass :")
        if user_choose_card == "y":
            user_cards.append(deal_card())
        else:
            is_game_over = True

    print(f" user score {user_cards} for the cards pair{user_score}")
    print(f" computer first cards {computer_cards[0]}")
    # print(user_cards)
    # print(computer_cards)


