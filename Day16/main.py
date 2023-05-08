from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

coffee_machine_on = True

while coffee_machine_on:
    types_of_drinks = menu.get_items()
    users_choice = input(f'What would you like? {types_of_drinks}: ')
    if users_choice == 'off':
        coffee_machine_on = False
    elif users_choice == 'report':
        coffee_machine.report()
        money.report()
    else:
        drink = menu.find_drink(users_choice)
        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)
