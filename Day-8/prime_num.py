#Write your code below this line

def prime_checker(number):
  if number > 1:
    for num in range(2,int(number / 2) + 1):
      if number % num == 0:
        print(" It's not a prime number")
        break
    else:
        print(" It's a prime number")
  else:
    print("It's not a prime number")


#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
