# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
new_two_digit_num = str(two_digit_number)
#dissect the string then add the two numbers
a = int(new_two_digit_num[1])
b = int(new_two_digit_num [0])
result = a + b
print(result)