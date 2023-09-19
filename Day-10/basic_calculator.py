from art import logo
#sum
def add(n1, n2):
    """"This function will add two number"""
    return n1 + n2

#subtraction
def sub(n1, n2):
    return n1 - n2

#multipulacation
def multi(n1, n2):
    return n1 * n2

#devide
def div(n1, n2):
    return n1 / n2

operation = {
    "+": add, "-": sub, "*": multi, "/": div
    }
def calculator():
    print(logo)
    num1 = float(input("What is the first number? :"))

    flag = True
    while flag:
        for opt in operation:
            print(opt)

        opt_symble = input("Pick an operation :")

        num2 = float(input("What is the next number? :"))

        opt_function = operation[opt_symble]
        ans = opt_function(num1,num2)

        print(f"{num1} {opt_symble} {num2} = {ans}")
        want_continue = input("Do you want to continue calculating ? (Type 'y'to continue or 'n' to new start) :")
        if want_continue == 'y':
            num1 = ans
        else:
            flag = False
            calculator()

calculator()







