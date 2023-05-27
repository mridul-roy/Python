#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to Tip Calculatro")
bill = input("What was the total bill $ ? ")
tip = input("How much % of tips would you like to give ? (10%, 12%, 14%) ")
num_of_people = input("How many person to split the bill ? ")

bill_for_per_person = int(bill) / int(num_of_people)

amout_of_tip_per_person = ( int(tip) * bill_for_per_person ) / 100

total_bill_per_person = bill_for_per_person + amout_of_tip_per_person

print(f"Each person sould pay $ {round(total_bill_per_person, 2)}" )
