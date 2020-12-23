def materials(cup):
    water = 200 * cup
    milk = 50 * cup
    beans = 15 * cup
    return "For {} cups of coffee you will need:\n{} ml of water\n{} ml of milk\n{} g of coffee beans".format(cup, water, milk, beans)


print("Write how many cups of coffee you will need:")
cups = int(input())
print(materials(cups))