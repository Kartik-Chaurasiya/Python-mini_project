from menu import menu
from menu import resources
def check_for_ingredients(order):
    if order == 'espresso':
        if (menu[order]['ingredients']['water'] - resources['water'] < 0) or (menu[order]['ingredients']['coffee'] - resources['coffee'] < 0):
            return False
        else:
            resources['water'] -= menu[order]['ingredients']['water']
            resources['coffee'] -= menu[order]['ingredients']['coffee']
            return True
    elif order == 'latte':
        if (menu[order]['ingredients']['water'] - resources['water'] < 0) or (menu[order]['ingredients']['coffee'] - resources['coffee'] < 0) or (menu[order]['ingredients']['milk'] - resources['milk'] < 0):
            return False
        else:
            resources['water'] -= menu[order]['ingredients']['water']
            resources['coffee'] -= menu[order]['ingredients']['coffee']
            resources['milk'] -= menu[order]['ingredients']['milk']
            return True
    elif order == 'cappuccino':
        if (menu[order]['ingredients']['water'] - resources['water'] < 0) or (menu[order]['ingredients']['coffee'] - resources['coffee'] < 0) or (menu[order]['ingredients']['milk'] - resources['milk'] < 0):
            return False
        else:
            resources['water'] -= menu[order]['ingredients']['water']
            resources['coffee'] -= menu[order]['ingredients']['coffee']
            resources['milk'] -= menu[order]['ingredients']['milk']
            return True
def take_money(order):
    #machine only takes coins
    quarters = int(input("Enter the number of quarters: ")) * 0.25
    dimes = int(input("Enter the number of dimes: ")) * 0.1
    nickles = int(input("Enter the number of nickles: ")) * 0.05
    pennies = int(input("Enter the number of pennies: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if total - menu[order]['cost'] < 0:
        print('The amount is not sufficient....Money refunded')
    else:
        print(f"Your order is ready \n Here's your change {total - menu[order]['cost']:.2f}")


enough_ingredients = True
menu = menu
resources = resources
while enough_ingredients:
    order = input("Enter your order: \n1. espresso \n2. latte \n3. cappuccino \n")
    if order == 'espresso':
        enough_ingredients = check_for_ingredients(order)
        take_money(order)
    elif order == 'latte':
        enough_ingredients = check_for_ingredients(order)
        take_money(order)
    elif order == 'cappuccino':
        enough_ingredients = check_for_ingredients(order)
        take_money(order)
