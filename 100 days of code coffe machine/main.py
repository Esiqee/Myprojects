from misc import logo, resources


def main():
    print(logo)
    choice = "on"
    current = resources
    while choice.lower() != "off":
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice.lower() == "off":
            print("*** Machine OFF ***")
        elif choice.lower() == "report":
            report(current)
        elif choice.lower() in ["espresso", "latte", "cappuccino"]:
            current = drink(choice, current)
        else:
            print("ERROR: INVALID ACTION!")


def latte(current):
    if current['water'] < 200:
        print("Sorry there is not enough water.")
        return
    elif current['milk'] < 150:
        print("Sorry there is not enough milk.")
        return
    elif current['coffee'] < 24:
        print("Sorry there is not enough coffee.")
        return
    else:
        print("This drink costs $2.5")
        money = coins()
        if money < 2.5:
            print("Sorry that's not enough money. Money refunded.")
            return
        else:
            current['water'] -= 200
            current['milk'] -= 150
            current['coffee'] -= 24
            current['money'] += 2.5
            ret = money - 2.5
            print(f"Here is ${ret:.2f} dollars in change.")
            print("Here is your ☕. Enjoy!")
            return current


def espresso(current):
    if current['water'] < 50:
        print("Sorry there is not enough water.")
        return
    elif current['coffee'] < 18:
        print("Sorry there is not enough coffee.")
        return
    else:
        print("This drink costs $1.5")
        money = coins()
        if money < 1.5:
            print("Sorry that's not enough money. Money refunded.")
            return
        else:
            current['water'] -= 50
            current['coffee'] -= 18
            current['money'] += 1.5
            ret = money - 1.5
            print(f"Here is ${ret:.2f} dollars in change.")
            print("Here is your ☕. Enjoy!")
            return current


def cappuccino(current):
    if current['water'] < 250:
        print("Sorry there is not enough water.")
        return
    elif current['milk'] < 100:
        print("Sorry there is not enough milk.")
        return
    elif current['coffee'] < 24:
        print("Sorry there is not enough coffee.")
        return
    else:
        print("This drink costs $3.0")
        money = coins()
        if money < 3.0:
            print("Sorry that's not enough money. Money refunded.")
            return
        else:
            current['water'] -= 250
            current['milk'] -= 100
            current['coffee'] -= 24
            current['money'] += 3.0
            ret = money - 3.0
            print(f"Here is ${ret:.2f} dollars in change.")
            print("Here is your ☕. Enjoy!")
            return current


def coins():
    quarters = int(input("How many quarters do you want to enter?: ")) * 25
    dimes = int(input("How many dimes do you want to enter?: ")) * 10
    nickles = int(input("How many nickles do you want to enter?: ")) * 5
    pennies = int(input("How many pennies do you want to enter?: "))
    money = quarters + dimes + nickles + pennies
    return money / 100


def report(current):
    print(f"Water : {current['water']}ml")
    print(f"Milk : {current['milk']}ml")
    print(f"Coffee : {current['coffee']}g")
    print(f"Money : ${current['money']}")


def drink(choice, current):
    if choice.lower() == "latte":
        current = latte(current)
    elif choice.lower() == "espresso":
        current = espresso(current)
    elif choice.lower() == "cappuccino":
        current = cappuccino(current)
    return current


if __name__ == "__main__":
    main()
    
    
