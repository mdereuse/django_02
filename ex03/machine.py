#!/usr/bin/python3


import random
from beverages import HotBeverage, Coffee, Cappuccino, Chocolate, Tea


class CoffeeMachine:
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        desc = "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self):
            self.args = ("This coffee machine has to be repaired.",)

    def __init__(self):
        self.broken = False
        self.beverage_served = 0

    def repair(self):
        self.broken = False
        self.beverage_served = 0
        print("Machine has been repaired!")

    def serve(self, beverage: HotBeverage) -> HotBeverage():
        if self.broken:
            raise self.BrokenMachineException
        r = random.random()
        self.beverage_served += 1
        if self.beverage_served == 10:
            self.broken = True
        if r > 0.5:
            return beverage()
        else:
            return self.EmptyCup()


def main():
    coffee_machine = CoffeeMachine()
    beverage_lst = [Tea, Coffee, Cappuccino, Chocolate]
    n = 0
    while n < 2:
        try:
            beverage = random.choice(beverage_lst)
            print(coffee_machine.serve(beverage))
            print()
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffee_machine.repair()
            print()
            n += 1


if __name__ == "__main__":
    main()
