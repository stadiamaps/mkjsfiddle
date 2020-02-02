import html
import mkdocs.plugins

from mkjsfiddle import CODE_FENCE_REGEX
from mkjsfiddle.parser import ScriptAndStyleParser


def jsfiddle_repl(match):
    lang = match.group(1)[1:]
    options = match.group(2)
    code = match.group(3)

    if options == "-htmlonly":
        quoted_html = html.escape(code, True)
        data_fields = f'<input type="hidden" name="html" value="{quoted_html}" />'
    else:
        parser = ScriptAndStyleParser()
        parser.feed(code)

        quoted_html = html.escape(parser.html_body, True)
        quoted_js = html.escape(parser.js_body, True)
        quoted_css = html.escape(parser.css_body, True)

        data_fields = f"""
    <input type="hidden" name="wrap" value="b" />
    <input type="hidden" name="html" value="{quoted_html}" />
    <input type="hidden" name="js" value="{quoted_js}" />
    <input type="hidden" name="css" value="{quoted_css}" />
"""

    return f"""
<form action="https://jsfiddle.net/api/post/library/pure" method="post" target="_blank">
    <input type="submit" value="Edit in JSFiddle" />
    {data_fields}
</form>

```{lang}
{code}
```"""


class JSFiddlePlugin(mkdocs.plugins.BasePlugin):
    config_scheme = ()

    def on_page_markdown(self, markdown, **kwargs):
        return CODE_FENCE_REGEX.sub(jsfiddle_repl, markdown)
