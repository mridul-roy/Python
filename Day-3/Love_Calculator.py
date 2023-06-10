# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

#TRUE
t1_found = name1.count("t")
t2_found = name2.count("t")
total_t_found = t1_found + t2_found

r1_found = name1.count("r")
r2_found = name2.count("r")
total_r_found = r1_found + r2_found

u1_found = name1.count("u")
u2_found = name2.count("u")
total_u_found = u1_found + u2_found

e1_found = name1.count("e")
e2_found = name2.count("e")
total_e_found = e1_found + e2_found

total_true = (total_t_found + total_r_found + total_u_found + total_e_found)

#LOVE
l1_found = name1.count("l")
l2_found = name2.count("l")
total_l_found = l1_found + l2_found

o1_found = name1.count("o")
o2_found = name2.count("o")
total_o_found = o1_found + o2_found

v1_found = name1.count("v")
v2_found = name2.count("v")
total_v_found = v1_found + v2_found

e3_found = name1.count("e")
e4_found = name2.count("e")
total_e5_found = e3_found + e4_found

total_love = (total_l_found + total_o_found + total_v_found + total_e5_found)

total_true_love = str(total_true) + str(total_love)

total_score =int(total_true_love)


if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")

elif  (total_score >= 40) and (total_score <= 50 ):
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")