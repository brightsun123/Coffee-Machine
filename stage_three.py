print("Write how many ml of water the coffee machine has:")
machine_water = int(input())
print("Write how many ml of milk the coffee machine has:")
machine_milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
machine_beans = int(input())
print("Write how many cups of coffee you will need:")
cups_wanted = int(input())
water_cups = machine_water // 200
milk_cups = machine_milk // 50
bean_cups = machine_beans // 15
water_needed = 200
milk_needed = 50
bean_needed = 15
if water_cups >= cups_wanted and milk_cups >= cups_wanted and bean_cups >= cups_wanted:
    if water_cups <= milk_cups and water_cups <= bean_cups:
        min_value = water_cups
    elif milk_cups <= water_cups and milk_cups <= bean_cups:
        min_value = milk_cups
    else:
        min_value = bean_cups
    difference = min_value - cups_wanted
    if difference == 0:
        print("Yes, I can make that amount of coffee")
    else:
        print("Yes, I can make that amount of coffee (and even {} more than that)".format(difference))
else:
    if machine_water >= water_needed or machine_milk >= milk_needed or machine_beans >= bean_needed:
        if water_cups <= milk_cups and water_cups <= bean_cups:
            min_value = water_cups
        elif milk_cups <= water_cups and milk_cups <= bean_cups:
            min_value = milk_cups
        else:
            min_value = bean_cups
        print("No, I can only make {} cups of coffee".format(min_value))
    else:
        print("No, I can make only 0 cups of coffee")
