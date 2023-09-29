from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_game_on = True
while is_game_on:
    option = menu.get_items()
    user_choose = input(f"What would you like? ({option}):")
    if user_choose == "off":
        is_game_on = False
    elif user_choose == "report":

        coffee_maker.report()

    else:
        drink = menu.find_drink(user_choose)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

