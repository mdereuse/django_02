#!/usr/bin/python3


class Intern:
    class Coffee:
        @staticmethod
        def __str__():
            return "This is the worst coffee you ever tasted."

    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def work():
        raise Exception("I’m just an intern, I can’t do that...")

    @classmethod
    def make_coffee(cls):
        return cls.Coffee()


def main():
    intern0 = Intern()
    intern1 = Intern("Mark")
    print(intern0)
    print(intern1)
    print(intern1.make_coffee())
    intern0.work()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
