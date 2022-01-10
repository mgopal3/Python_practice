"""
#Code for Coffee Machine
  1. Makes 3 flavors: Espresso/Latte/Capuccino
    Espresso
 2. Coin Operated. Accepts Penny/Nickel/Dime/Quarter
    Penny = 1 Cent ($0.01)
    Nickel = 5 Cent ($0.05)
    Dime = 10 Cents ($0.10)
    Quarter = 25 Cents ($0.25)
Program Requirements:
    report: will print all the remaining resources
    Check for sufficient Resources and
    Process Coins
    Gives you change
    then gives you a coffee and tell you to Enjoy
    Check if the transaction is successful and deduct resources
"""
from os import system
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

value = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

money_left = 0


def increment_global_money_left(value):
    """A simple way to increment and decrement the Global Money Variable"""
    global money_left
    money_left += value


def decrement_global_money_left(value):
    """A simple way to increment and decrement the Global Money Variable"""
    global money_left
    money_left -= value


def resource_check():
    """Prints the resources that are remaining in the machine"""
    print(
        f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: {money_left}\n')


def check_sufficient_resource(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    total = 0
    total += value["quarters"] * int(input("How many quarters?: "))
    total += int(input("How many dimes?: ")) * value["dimes"]
    total += int(input("How many nickles?: ")) * value["nickles"]
    total += int(input("How many pennies?: ")) * value["pennies"]
    return total


def check_transaction(drink, inserted_amount):
    cost = MENU[drink]["cost"]
    if inserted_amount < cost:
        print("Sorry that is not enough money. Money Refunded.")
        return False
    else:
        increment_global_money_left(cost)
        change = inserted_amount - cost
        if change > 0:
            print(f"Here is ${round(change, 2)} dollars in change.")
        return True


def decrement_resource(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    return


def make_coffee(drink):
    """When we come here, we have run the previous checks and are ready to make the drink"""
    decrement_resource(drink)
    print(f"Here is your {drink}. Enjoy!")
    print("Resources after purchase: ")
    resource_check()


is_on = True
while is_on:
    system("clear")
    drink_of_choice = input("What would you like? (espresso/latte/cappuccino) ")

    if drink_of_choice == "off":
        is_on = False

    elif drink_of_choice == "report":
        resource_check()
    elif drink_of_choice == "espresso" or drink_of_choice == "latte" or drink_of_choice == "cappuccino":
        if check_sufficient_resource(drink_of_choice):
            inserted_value = process_coins()
            if check_transaction(drink_of_choice, inserted_value):
                make_coffee(drink_of_choice)
