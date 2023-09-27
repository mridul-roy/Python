print("Welcome to Coffee Maker !!!")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
game_on = True
while game_on:
    user_choose = input("“What would you like? (espresso/latte/cappuccino):")
    if user_choose == "off":
        game_on = False

    elif user_choose == "report":
        print(f"Water :{resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money: ${'profit'}")

    else:
        drink = MENU[user_choose]
        print(drink)

