from types_of_coffee import MENU

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

money = 0


def is_resource_sufficient(ingredients):
    for item in resources:
        if ingredients[item] > resources[item]:
            print(f'Sorry there is not enough {item}.')
            return False
    return True


def process_coins():
    print('Please insert coins.')
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.1
    total += int(input('How many nickels?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return total


def is_transaction_successful(money_received, cost_of_drink):
    if money_received >= cost_of_drink:
        change = round(money_received - cost_of_drink, 2)
        print(f'Here is ${change} in change.')
        global money
        money += cost_of_drink
        return True
    else:
        print('Sorry that\'s not enough money. Money refunded.')
        return False


def make_coffee(drink, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'Here is your {drink}. Enjoy!')


coffee_machine_on = True

while coffee_machine_on:
    users_choice = input('What would you like? (espresso/latte/cappuccino): ')
    if users_choice == 'off':
        coffee_machine_on = False
    elif users_choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
    else:
        drink = MENU[users_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(users_choice, drink['ingredients'])

# TODO: Print report

# TODO: Check resources to see if sufficient

# TODO: Process coins

# TODO: Check transaction successful

# TODO: Make coffee







