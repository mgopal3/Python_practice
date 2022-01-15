from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


if __name__ == '__main__':
    need_coffee = True
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()


    while(need_coffee) :
        inp = input(f"What would you like? ({menu.get_items()}) :")
        if inp == "off" :
            need_coffee = False
        elif inp == "report" :
            coffee_maker.report()
            money_machine.report()
        elif inp == "latte" or inp == "cappuccino" or inp == "espresso" :
            drink = menu.find_drink(inp)
            if coffee_maker.is_resource_sufficient(drink) :
                if money_machine.make_payment(drink.cost) :
                    coffee_maker.make_coffee(drink)
        else:
            print("Incorrect inp provided. Try again.")


