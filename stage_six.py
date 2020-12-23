class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.money = 550
        self.cups = 9
        self.count = 0
        print("Write action (buy, fill, take, remaining, exit):")
        self.state = "choosing an action"
        self.user_input()

    def user_input(self):
        a = input()
        self.process(a)

    def process(self, action):
        if self.state == "choosing an action":
            if action == "buy":
                print()
                self.state = "choosing a type of coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.user_input()
            elif action == "fill":
                print()
                print("Write how many ml of water do you want to add:")
                self.state = "filling"
                self.user_input()
            elif action == "take":
                print()
                print("I gave you ${}".format(self.money))
                print()
                self.money = 0
                print("Write action (buy, fill, take, remaining, exit):")
                self.user_input()
            elif action == "remaining":
                print()
                print("The coffee machine has:")
                print("{} of water".format(self.water))
                print("{} of milk".format(self.milk))
                print("{} of coffee beans".format(self.beans))
                print("{} of disposable cups".format(self.cups))
                print("${} of money".format(self.money))
                print()
                print("Write action (buy, fill, take, remaining, exit):")
                self.user_input()
            else:
                exit()
        elif self.state == "choosing a type of coffee":
            if action == "1":
                if self.water >= 250:
                    if self.beans >= 16:
                        if self.cups >= 1:
                            self.water -= 250
                            self.beans -= 16
                            self.money += 4
                            self.cups -= 1
                            print("I have enough resources, making you a coffee!")
                            print()
                            print("Write action (buy, fill, take, remaining, exit):")
                            self.state = "choosing an action"
                            self.user_input()
                        else:
                            print("Sorry, not enough cups!")
                            print()
                            print("Write action (buy, fill, take, remaining, exit):")
                            self.state = "choosing an action"
                            self.user_input()
                    else:
                        print("Sorry, not enough beans!")
                        print()
                        print("Write action (buy, fill, take, remaining, exit):")
                        self.state = "choosing an action"
                        self.user_input()
                else:
                    print("Sorry, not enough water!")
                    print()
                    print("Write action (buy, fill, take, remaining, exit):")
                    self.state = "choosing an action"
                    self.user_input()
            elif action == "2":
                if self.water >= 350:
                    if self.beans >= 20:
                        if self.milk >= 75:
                            if self.cups >= 1:
                                self.water -= 350
                                self.milk -= 75
                                self.beans -= 20
                                self.money += 7
                                self.cups -= 1
                                print("I have enough resources, making you a coffee!")
                                print()
                                print("Write action (buy, fill, take, remaining, exit):")
                                self.state = "choosing an action"
                                self.user_input()
                            else:
                                print("Sorry, not enough cups!")
                                print()
                                print("Write action (buy, fill, take, remaining, exit):")
                                self.state = "choosing an action"
                                self.user_input()
                        else:
                            print("Sorry, not enough milk!")
                            print()
                            print("Write action (buy, fill, take, remaining, exit):")
                            self.state = "choosing an action"
                            self.user_input()
                    else:
                        print("Sorry, not enough beans!")
                        print()
                        print("Write action (buy, fill, take, remaining, exit):")
                        self.state = "choosing an action"
                        self.user_input()
                else:
                    print("Sorry, not enough water!")
                    print()
                    print("Write action (buy, fill, take, remaining, exit):")
                    self.state = "choosing an action"
                    self.user_input()
            elif action == "3":
                if self.water >= 200:
                    if self.beans >= 12:
                        if self.milk >= 100:
                            if self.cups >= 1:
                                self.water -= 200
                                self.milk -= 100
                                self.beans -= 12
                                self.money += 6
                                self.cups -= 1
                                print("I have enough resources, making you a coffee!")
                                print()
                                print("Write action (buy, fill, take, remaining, exit):")
                                self.state = "choosing an action"
                                self.user_input()
                            else:
                                print("Sorry, not enough cups!")
                                print()
                                print("Write action (buy, fill, take, remaining, exit):")
                                self.state = "choosing an action"
                                self.user_input()
                        else:
                            print("Sorry, not enough milk!")
                            print()
                            print("Write action (buy, fill, take, remaining, exit):")
                            self.state = "choosing an action"
                            self.user_input()
                    else:
                        print("Sorry, not enough beans!")
                        print()
                        print("Write action (buy, fill, take, remaining, exit):")
                        self.state = "choosing an action"
                        self.user_input()
                else:
                    print("Sorry, not enough water!")
                    print()
                    print("Write action (buy, fill, take, remaining, exit):")
                    self.state = "choosing an action"
                    self.user_input()
            else:
                self.state = "choosing an action"
                print()
                print("Write action (buy, fill, take, remaining, exit):")
                self.user_input()
        elif self.state == "filling":
            if self.count == 0:
                self.water += int(action)
                self.count += 1
                print("Write how many ml of milk do you want to add:")
                self.user_input()
            elif self.count == 1:
                self.milk += int(action)
                self.count += 1
                print("Write how many grams of coffee beans do you want to add:")
                self.user_input()
            elif self.count == 2:
                self.beans += int(action)
                self.count += 1
                print("Write how many disposable cups of coffee do you want to add:")
                self.user_input()
            else:
                self.cups += int(action)
                self.count = 0
                print()
                self.state = "choosing an action"
                print("Write action (buy, fill, take, remaining, exit):")
                self.user_input()

coffee = CoffeeMachine()
