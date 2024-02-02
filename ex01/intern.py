DEFAULT_NAME = "My name? I’m nobody, an intern, I have no name."
COFFEE_TALK = "This is the worst coffee you ever tasted."
EXCEPTION_TXT = "I’m just an intern, I can’t do that..."


class Intern:
    class Coffee:
        @staticmethod
        def __str__():
            return COFFEE_TALK

    def __init__(self, name=DEFAULT_NAME):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def work():
        raise Exception(EXCEPTION_TXT)

    @classmethod
    def make_coffee(cls):
        return cls.Coffee()


def main():
    try:
        intern0 = Intern()
        intern1 = Intern("Mark")
        print(intern0)
        print(intern1)
        print(intern1.make_coffee())
        intern0.work()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
