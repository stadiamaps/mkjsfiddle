import html
from html.parser import HTMLParser

# From https://html.spec.whatwg.org/multipage/syntax.html#void-elements
VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


def clean_data(s: str):
    lines = s.replace("\t", "    ").splitlines()  # Tabs to spaces
    prefix = ""
    processed_lines = []

    for line in lines:
        if not prefix and line:
            prefix = " " * (len(line) - len(line.lstrip()))  # Get prefix in space terms for indentation

        processed_lines.append(f"{line.replace(prefix, '', 1)}")

    return "\n".join(processed_lines).strip()


class ScriptAndStyleParser(HTMLParser):
    """Extracts JavaScript and style from an HTML document."""

    def __init__(self):
        super().__init__()

        self.html_body = ""

        self.__parsing_js = False
        self.__parsing_css = False

        self.__js_fragments = []
        self.__css_fragments = []

    @property
    def js_body(self):
        return "\n\n".join(self.__js_fragments) + "\n"

    @property
    def css_body(self):
        return "\n\n".join(self.__css_fragments) + "\n"

    def handle_starttag(self, tag, attrs):
        if (
            tag == "script"
            and ("type", "text/javascript") in attrs
            and not [key for (key, value) in attrs if key == "src"]
        ):
            self.__parsing_js = True
        elif tag == "style" and ("type", "text/css") in attrs:
            self.__parsing_css = True
        else:
            formatted_attrs = " ".join([f'{key}="{html.escape(value, True)}"' for (key, value) in attrs])
            self.html_body += f'<{tag}{" " if formatted_attrs else ""}{formatted_attrs}>'

    def handle_endtag(self, tag):
        if self.__parsing_js:
            self.__parsing_js = False
            self.html_body = self.html_body.rstrip()  # Gets around formatting issues
        elif self.__parsing_css:
            self.__parsing_css = False
            self.html_body = self.html_body.rstrip()  # Gets around formatting issues
        elif tag not in VOID_ELEMENTS:
            self.html_body += f"</{tag}>"

    def handle_data(self, data: str):
        if self.__parsing_js:
            self.__js_fragments.append(clean_data(data))
        elif self.__parsing_css:
            self.__css_fragments.append(clean_data(data))
        else:
            self.html_body += data.replace("\t", "    ")

    def handle_comment(self, data):
        self.html_body += f"<!--{data}-->"

    def handle_decl(self, decl):
        self.html_body += f"<!{decl}>"

    def reset(self):
        super().reset()

        self.html_body = ""

        self.__parsing_js = False
        self.__parsing_css = False

        self.__js_fragments = []
        self.__css_fragments = []
