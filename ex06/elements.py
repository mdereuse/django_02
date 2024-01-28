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


if __name__ == "__main__":
    main()
