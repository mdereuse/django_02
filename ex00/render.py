import sys
import os
import re
import settings


class Error(Exception):
    pass


class WrongNumberOfArgumentsError(Error):
    def __init__(self):
        self.args = ("Ce programme a besoin d'un unique argument.",)


class WrongExtensionFileError(Error):
    def __init__(self):
        self.args = ("L'extension du fichier doit etre .template.",)


class TemplateFileNotFoundError(Error):
    def __init__(self):
        self.args = ("Le fichier template n'existe pas.",)


class ReadingFileError(Error):
    def __init__(self):
        self.args = ("Le fichier template n'a pas pu etre lu.",)


class WritingFileError(Error):
    def __init__(self):
        self.args = ("Le fichier html n'a pas pu etre ecrit.",)


def open_template(template_filepath):
    if not template_filepath.endswith(".template"):
        raise WrongExtensionFileError
    if not os.path.isfile(template_filepath):
        raise TemplateFileNotFoundError
    try:
        with open(template_filepath, "r") as f:
            template_content = f.read()
    except Exception:
        raise ReadingFileError
    else:
        return template_content


def format_content(template_content):
    def repl(m):
        t = m.group(1)
        new_text = "{settings." + t + "}"
        return new_text

    template_content = re.sub(r"{(.*?)}", repl, template_content)
    f_template_content = template_content.format(**globals())
    return f_template_content


def get_filename(template_filepath):
    basename = os.path.basename(template_filepath)
    return basename[:basename.find(".template")]


def write_html(content, filename):
    try:
        with open(filename + ".html", "w") as f:
            f.write(content)
    except Exception:
        raise WritingFileError


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise WrongNumberOfArgumentsError
    template_filepath = args[0]
    template_content = open_template(template_filepath)
    f_template_content = format_content(template_content)
    write_html(f_template_content, get_filename(template_filepath))


if __name__ == "__main__":
    try:
        main()
    except Error as e:
        print(e)
