PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = (letter_file.read())
    for name in names:
        striped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER,striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt",mode="w") as file:
            file.write(new_letter)