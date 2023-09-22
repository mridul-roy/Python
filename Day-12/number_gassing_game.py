import random

computer_select = random.randint(2,100)
print(f"Computer Gussed answer is :{computer_select}")
flag = True

number = int(input("Gassed a number: "))
easy_attempt_count = 0
for number in range (5):
    def level_easy(number):
        if number == computer_select:
            return f"You win.Picked number matched with computer choose"
        elif number > computer_select:
            return "Number is too high"
        elif number < computer_select:
            return "Number is too less"
           

level_easy(number)
result = level_easy(number)
print(result)