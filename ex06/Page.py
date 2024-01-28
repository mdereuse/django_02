from elements import *
from elem import Text


class Page:
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

    def __init__(self, elem: Elem):
        self.elem = elem

    @staticmethod
    def _is_elem_valid(elem):
        if type(elem) not in Page.type_lst:
            return False
        elif isinstance(elem, Html):
            if not (len(elem.content) == 2
                    and isinstance(elem.content[0], Head)
                    and isinstance(elem.content[1], Body)):
                return False
        elif isinstance(elem, Head):
            if not (len(elem.content) == 1
                    and isinstance(elem.content[0], Title)):
                return False
        elif type(elem) in [Body, Div]:
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
        elif isinstance(elem, Text):
            return True
        return all(Page._is_elem_valid(child) for child in node.content)

    def is_valid(self):
        return Page._is_elem_valid(self.elem)

    def __str__(self):
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>" + str(self.elem)
        else:
            return str(self.elem)

    def write_to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(str(self))
            

def main():
    print(all([]))


if __name__ == "__main__":
    main()
