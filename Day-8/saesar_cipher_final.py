alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

from art import logo

def seasar(txt,shift_amount, direction):
    final_word = ""
    for letter in txt :
        

# def encrypt(txt, shift_amount):
#     encrypt_word = ""
#     for letter in txt:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         encrypt_word += new_letter
#     print(f"Encrypted text is : {encrypt_word}")


# def decrypt(txt, shift_amount):
#     encrypt_word = ""
#     for letter in txt:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         encrypt_word += new_letter
#     print(f"Decoded text is : {encrypt_word}")


# if direction == 'encode':
#     encrypt(txt=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(txt=text, shift_amount=shift)
# else:
#     print("Invalid. Something wrong !!!")

#shift = shift % 26
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.