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
        return all(Page._is_elem_valid(child) for child in elem.content)

    def is_valid(self):
        return Page._is_elem_valid(self.elem)

    def __str__(self):
        if isinstance(self.elem, Html):
            return "<!DOCTYPE html>\n" + str(self.elem)
        else:
            return str(self.elem)

    def write_to_file(self, filepath):
        with open(filepath, "w") as f:
            f.write(str(self))
            

def main():
    print("TEST VALID")
    test_ok = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_ok.is_valid())
    print()
    print("Head is before Body")
    test_html = Page(Html([
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ]),
        Head(
            Title(Text("\"Hello ground!\""))
        )
    ]))
    print(test_html.is_valid())
    print()
    print("Two titles")
    test_head = Page(Html([
        Head([
            Title(Text("\"Hello ground!\"")),
            Title(Text("2nd Title"))
        ]),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_head.is_valid())
    print()
    print("Wrong element type in body")
    test_body = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Li(Text("test")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_body.is_valid())
    print()
    print("Title contains more than one text")
    test_title = Page(Html([
        Head(
            Title([Text("\"Hello ground!\""), Text("pouet")])
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_title.is_valid())
    print()
    print("P contains a non text")
    test_p = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P."),
                        Li(Text("pouet"))
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_p.is_valid())
    print()
    print("Span contains a forbidden element")
    test_span = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P."),
                    ]),
                    Text("This is a text outside a P."),
                    Li(Text("pouet"))
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_span.is_valid())
    print()
    print("Ul contains no element")
    test_ul = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_ul.is_valid())
    print()
    print("Ol contains other than Li")
    test_ol = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
                Ol([
                    Li(Text("truc")), Text("bidule"), Li(Text("chouette"))
                ]),
            ])
        ])
    ]))
    print(test_ol.is_valid())
    print()
    print("Tr contains Td and Th")
    test_tr = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Td(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ])
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_tr.is_valid())
    print()
    print("Table contains other than Tr")
    test_table = Page(Html([
        Head(
            Title(Text("\"Hello ground!\""))
        ),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Text("This is a second text in a P.")
                    ]),
                    Text("This is a text outside a P.")
                ])
            ]),
            Div([
                Table([
                    Tr([
                        Th(Text("Pif")), Th(Text("Paf")), Th(Text("Pouf"))
                    ]),
                    Tr([
                        Td(Text("1")), Td(Text("2")), Td(Text("3"))
                    ]),
                    Tr([
                        Td(Text("4")), Td(Text("5")), Td(Text("6"))
                    ]),
                    Text("pouet")
                ]),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(test_table.is_valid())
    print()
    print()
    print("DISPLAY")
    print()
    print(test_ok)
    print()
    print("print only a div :")
    print()
    print(Page(Div(Text("pouet"))))
    test_ok.write_to_file("test.html")


if __name__ == "__main__":
    main()
