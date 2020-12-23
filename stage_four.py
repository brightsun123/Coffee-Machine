water = 400
milk = 540
beans = 120
money = 550
cups = 9

def buy_coffee(coffee):
    global water, beans, milk, money, cups
    if coffee == "1":
        water -= 250
        beans -= 16
        money += 4
        cups -= 1
    elif coffee == "2":
        water -= 350
        milk -= 75
        beans -= 20
        money += 7
        cups -= 1
    else:
        water -= 200
        milk -= 100
        beans -= 12
        money += 6
        cups -= 1

def fill_machine(water_value, milk_value, coffee_value, cups_value):
    global water, beans, milk, money, cups
    water += water_value
    milk += milk_value
    beans += coffee_value
    cups += cups_value

def take_money():
    global money
    print("I gave you ${}".format(money))
    money = 0

def machine_state():
    global water, beans, milk, money, cups
    print("The coffee machine has:")
    print("{} of water".format(water))
    print("{} of milk".format(milk))
    print("{} of coffee beans".format(beans))
    print("{} of disposable cups".format(cups))
    print("{} of money".format(money))

def action_question():
    print()
    print("Write action (buy, fill, take):")



def main():
    machine_state()
    action_question()
    action = input()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        buy_input = input()
        buy_coffee(buy_input)
        print()
        machine_state()
    elif action == "fill":
        print("Write how many ml of water do you want to add:")
        water_adding = int(input())
        print("Write how many ml of milk do you want to add:")
        milk_adding = int(input())
        print("Write how many grams of coffee beans do you want to add:")
        beans_adding = int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        cups_adding = int(input())
        fill_machine(water_adding, milk_adding, beans_adding, cups_adding)
        print()
        machine_state()
    else:
        take_money()
        print()
        machine_state()


main()
