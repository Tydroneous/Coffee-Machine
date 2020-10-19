import math

# class CoffeeMachine:
cash_in_machine = 550
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9


def is_possible(self, drink_choice):
    global cash_in_machine
    global water
    global milk
    global coffee_beans
    global disposable_cups
    # 250 ml water, 16 g coffee beans, cost 4 dollars
    espresso = [250, 16, 4]
    # 350 ml water, 75 ml of milk, 20 g of coffee beans, cost 7 dollars
    latte = [350, 75, 20, 7]
    # 200 ml water, 100 ml of milk, 12 g of coffee beans, cost 7 dollars
    cappuccino = [200, 100, 12, 6]

    temp_cups = disposable_cups - 1
    # milk is the only one not used in one of the drinks
    temp_milk = 0

    if drink_choice == 1:
        temp_water = water - espresso[0]
        temp_beans = coffee_beans - espresso[1]

    elif drink_choice == 2:
        temp_water = water - latte[0]
        temp_milk = milk - latte[1]
        temp_beans = coffee_beans - latte[2]

    else:
        temp_water = water - cappuccino[0]
        temp_milk = milk - cappuccino[1]
        temp_beans = coffee_beans - cappuccino[2]

    if temp_cups >= 0 and temp_water >= 0 and temp_milk >= 0 and temp_beans >= 0:
        disposable_cups -= 1
        if drink_choice == 1:
            water -= espresso[0]
            coffee_beans -= espresso[1]
            cash_in_machine += espresso[2]
        elif drink_choice == 2:
            water = temp_water
            milk = temp_milk
            coffee_beans = temp_beans
            cash_in_machine += latte[3]
        else:
            water -= cappuccino[0]
            milk -= cappuccino[1]
            coffee_beans -= cappuccino[2]
            cash_in_machine += cappuccino[3]
        return "True"
    else:
        if temp_cups <= -1:
            negative_value = "cups"
        if temp_water <= -1:
            negative_value = "water"
        if temp_beans <= -1:
            negative_value = "beans"
        return negative_value


def buying_coffee():
    print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    drink_selection = input()
    if drink_selection != "back":
        drink_selection = int(drink_selection)
        if 1 <= drink_selection <= 3:
            possibility = is_possible(drink_selection)
            if possibility == "True":
                print("I have enough resources, making you a coffee!\n")
                return
            else:
                print("Sorry, not enough {0}!\n".format(possibility))
                return
        else:
            print("Incorrect selection.\n")

    else:
        print()
        return


def filling_coffee_machine():
    global cash_in_machine
    global water
    global milk
    global coffee_beans
    global disposable_cups

    print("\nWrite how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups += int(input())
    print()
    return


def take_money_from_machine():
    global cash_in_machine
    print("\nI gave you ${0}".format(cash_in_machine))
    print()
    cash_in_machine = 0
    return


def remaining_info():
    return


#  This will sort the actions and call the correct function based upon selection
def initial_action(option_selected):
    if option_selected == "buy":
        buying_coffee()
    elif option_selected == "fill":
        filling_coffee_machine()
    elif option_selected == "take":
        take_money_from_machine()
    else:
        machine_state()


# print(calculations(cups_qty, water_total, milk_total, coffee_beans_total))
def machine_state():
    print("\nThe coffee machine has:")
    print("{0} of water".format(water))
    print("{0} of milk".format(milk))
    print("{0} of coffee beans".format(coffee_beans))
    print("{0} of disposable cups".format(disposable_cups))
    print("${0} of money".format(cash_in_machine))
    print()


selection = ""
while selection != "exit":
    print("Write action (buy, fill, take, remaining, exit):")
    selection = str(input())
    if selection == "buy" or selection == "fill" or selection == "take" or selection == "remaining":
        initial_action(selection)

# my_coffee_machine = CoffeeMachine()
#
# my_coffee_machine.initial_action()
