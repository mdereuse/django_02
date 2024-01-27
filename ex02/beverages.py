class HotBeverage:
    price = 0.30
    name = "hot beverage"
    desc = "Just some hot water in a cup."

    @classmethod
    def description(cls):
        return cls.description

    @classmethod
    def __str__(cls):
        txt = f"name : {cls.name}\n"
        txt += f"price : {cls.price:.2f}\n"
        txt += f"description : {cls.desc}"
        return txt


class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"
    desc = "A coffee, to stay awake."


class Tea(HotBeverage):
    name = "tea"


class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"
    desc = "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"
    desc = "Un po’ di Italia nella sua tazza!"


def main():
    print(HotBeverage())
    print()
    print(Coffee())
    print()
    print(Tea())
    print()
    print(Chocolate())
    print()
    print(Cappuccino())


if __name__ == "__main__":
    main()
