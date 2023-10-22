import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

data = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def take_input():
    word = input("Write your name :").upper()
    try:
        output = [data[letter] for letter in word]
    except KeyError:
        print("Sorry, Entered only text")
        take_input()
    else:
        print(output)


take_input()
