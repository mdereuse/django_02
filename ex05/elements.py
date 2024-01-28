from elem import Elem, Text


class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("html", attr=attr, content=content, tag_type="double")


class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("head", attr=attr, content=content, tag_type="double")


class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("body", attr=attr, content=content, tag_type="double")


class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("title", attr=attr, content=content, tag_type="double")


class Meta(Elem):
    def __init__(self, attr={}):
        super().__init__("meta", attr=attr, content=None, tag_type="simple")


class Img(Elem):
    def __init__(self, attr={}):
        super().__init__("img", attr=attr, content=None, tag_type="simple")


class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("table", attr=attr, content=content, tag_type="double")


class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("th", attr=attr, content=content, tag_type="double")


class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("tr", attr=attr, content=content, tag_type="double")


class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("td", attr=attr, content=content, tag_type="double")


class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("ul", attr=attr, content=content, tag_type="double")


class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("ol", attr=attr, content=content, tag_type="double")


class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("li", attr=attr, content=content, tag_type="double")


class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("h1", attr=attr, content=content, tag_type="double")


class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("h2", attr=attr, content=content, tag_type="double")


class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("p", attr=attr, content=content, tag_type="double")


class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("div", attr=attr, content=content, tag_type="double")


class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__("span", attr=attr, content=content, tag_type="double")


class Hr(Elem):
    def __init__(self, attr={}):
        super().__init__("hr", attr=attr, content=None, tag_type="simple")


class Br(Elem):
    def __init__(self, attr={}):
        super().__init__("br", attr=attr, content=None, tag_type="simple")


def main():
    txt = str(
        Html([
                Head(
                    Title(Text("\"Hello ground!\""))
                ),
                Body([
                    H1(Text("\"Oh no, not again!\"")),
                    Img({"src": "http://i.imgur.com/pfp3T.jpg"})
                ])
        ])
    ).replace("&quot;", "\"")
    print(txt)
    print()
    big_txt = str(Html([
        Head([
            Title(Text("\"Hello ground!\"")),
            Meta(attr={"charset": "utf-8"}),
        ]),
        Body([
            H1(Text("\"Oh no, not again!\"")),
            Hr(),
            Div([
                H2(Text("\"Yes, again.\"")),
                Span([
                    P([
                        Text("This is one text in a P."),
                        Br(),
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
                Br(),
                Ul([
                    Li(Text("truc")), Li(Text("bidule")), Li(Text("chouette"))
                ]),
                Ol([
                    Li(Text("chose")), Li(Text("machin")), Li(Text("blop"))
                ]),
            ])
        ])
    ]))
    print(big_txt)


if __name__ == "__main__":
    main()
