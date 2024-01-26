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


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        raise WrongNumberOfArgumentsError
    template_filepath = args[0]
    if not template_filepath.endswith(".template"):
        raise WrongExtensionFileError
    if not os.path.isfile(template_filepath):
        raise TemplateFileNotFoundError
    with open(template_filepath, "r") as f:
        template_content = f.read()
    def repl(m):
        t = m.group(1)
        new_text = "{settings." + t + "}"
        return new_text
    template_content = re.sub(r"{(.*?)}",repl , template_content)
    f_txt = template_content.format(**globals())
    print(f_txt)
    with open("truc.html", "w") as f:
        f.write(f_txt)


if __name__ == "__main__":
    try:
        main()
    except Error as e:
        print(e)
