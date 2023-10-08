import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

data = {row.letter: row.code for (index, row) in nato_data.iterrows()}

word = input("Write your name : ").upper()

output = [data[letter] for letter in word]

print(output)
