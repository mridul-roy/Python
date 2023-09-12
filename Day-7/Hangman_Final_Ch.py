import random
from hangman_words import word_list
from hangman_art import logo,stages


print(logo)
chosen_word = random.choice(word_list)


display = ["_" for _ in chosen_word]
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f'{guess} You have already choose that.')

    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter '{guess}' is not in Word. You lose a live.")
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!!!")

    print(stages[lives])
print(f'The solution is {chosen_word}.')
