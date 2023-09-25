import random
from art import vs
from game_data import data

opt_A = random.choice(data)
opt_B = random.choice(data)
if opt_A == opt_B:
    opt_B = random.choice(data)

opt_A_name = opt_A["name"]
opt_A_decri = opt_A["description"]
opt_A_country = opt_A["country"]

print(f"Option A : {opt_A_name}, is {opt_A_decri}, from {opt_A_country}")
print(vs)

opt_B_name = opt_B["name"]
opt_B_decri = opt_B["description"]
opt_B_country = opt_B["country"]

print(f"Option B : {opt_B_name}, is {opt_B_decri}, from {opt_B_country}")

score = input("Who has more followers? A or B :")

if score == 