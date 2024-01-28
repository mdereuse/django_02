from elements import *
from elem import Text


class Page:
    def __init__(self, elem: Elem):
        self.elem = elem

    @staticmethod
    def _is_valid_type(elem):
        type_lst = [
            Html,
            Head,
            Body,
            Title,
            Meta,
            Img,
            Table,
            Th,
            Tr,
            Td,
            Ul,
            Ol,
            Li,
            H1,
            H2,
            P,
            Div,
            Span,
            Hr,
            Br,
            Text
        ]
        return type(elem) in type_lst

    @staticmethod
    def _is_elem_valid(elem):
        if isinstance(elem, Html):
            if not (len(elem.content) == 2
                    and isinstance(elem.content[0], Head)
                    and isinstance(elem.content[1], Body)):
                return False
        elif isinstance(elem, Head):
            if not (len(elem.content) == 1
                    and isinstance(elem.content[0], Title)):
                return False
        elif isinstance(elem, Body) or isinstance(elem, Div):
            for child in elem.content:
                if type(child) not in [H1, H2, Div, Table, Ul, Ol, Span, Text]:
                    return False
        elif type(elem) in [Title, H1, H2, Li, Th, Td]:
            if not (len(elem.content) == 1
                    and isinstance(elem.content[0], Text)):
                return False
        elif isinstance(elem, P):
            for child in elem.content:
                if not isinstance(child, Text):
                    return False
        elif isinstance(elem, Span):
            for child in elem.content:
                if type(child) not in [Text, P]:
                    return False
        elif type(elem) in [Ul, Ol]:
            if len(elem.content) == 0:
                return False
            for child in elem.content:
                if not isinstance(child, Li):
                    return False
        elif isinstance(elem, Tr):
            if len(elem.content) == 0:
                return False
            if not (all(isinstance(child, Th) for child in elem.content)
                    or all(isinstance(child, Td) for child in elem.content)):
                return False
        elif isinstance(elem, Table):
            if not all(isinstance(child, Tr) for child in elem.content):
                return False
        elif not Page._is_valid_type(elem):
            return False
        else:
            return True


    def is_valid(self):
        for child in self.content:
            
            


def main():
    print(type(Div()) in [Div, Html])


if __name__ == "__main__":
    main()
