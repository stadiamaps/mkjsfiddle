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
    <a href="#" onclick="this.closest('form').submit(); return false;">
      <svg width="48" height="40" stroke="#2E71FF" style="vertical-align: middle;">
        <g stroke-width="1.5" fill="none" fill-rule="evenodd">
        <path d="M23.4888889,20.543316 C21.4404656,18.4187374 19.0750303,15.6666667 16.4832014,15.6666667 C13.8721947,15.6666667 11.7555556,17.6366138 11.7555556,20.0666667 C11.7555556,22.4967196 13.8721947,24.4666667 16.4832014,24.4666667 C18.8347252,24.4666667 19.9845474,23.0125628 20.6429148,22.312473" stroke-linecap="round"></path>
        <path d="M22.5111111,19.5900174 C24.5595344,21.7145959 26.9249697,24.4666667 29.5167986,24.4666667 C32.1278053,24.4666667 34.2444444,22.4967196 34.2444444,20.0666667 C34.2444444,17.6366138 32.1278053,15.6666667 29.5167986,15.6666667 C27.1652748,15.6666667 26.0154526,17.1207706 25.3570852,17.8208603" stroke-linecap="round"></path>
        <path d="M45,22.7331459 C45,19.1499462 42.7950446,16.079593 39.6628004,14.7835315 C39.6774469,14.5246474 39.7003932,14.2674038 39.7003932,14.0035978 C39.7003932,6.82243304 33.8412885,1 26.611593,1 C21.3985635,1 16.9102123,4.03409627 14.8051788,8.41527616 C13.7828502,7.62878013 12.503719,7.15547161 11.1134367,7.15547161 C7.77825654,7.15547161 5.07450503,9.84159999 5.07450503,13.1544315 C5.07450503,13.7760488 5.16938207,14.3779791 5.3477444,14.9418479 C2.74863428,16.4787471 1,19.2867709 1,22.5105187 C1,27.3287502 4.89630545,31.2367856 9.72803666,31.31094 L36.3341301,31.3109406 C41.1201312,31.3406346 45,27.4870665 45,22.7331459 L45,22.7331459 Z" stroke-linejoin="round" />
      </g>
      </svg>
      Edit in JSFiddle
    </a>
    {data_fields}
</form>

```{lang}
{code}
```"""


class JSFiddlePlugin(mkdocs.plugins.BasePlugin):
    config_scheme = ()

    def on_page_markdown(self, markdown, **kwargs):
        return CODE_FENCE_REGEX.sub(jsfiddle_repl, markdown)
