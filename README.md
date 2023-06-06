# MkDocs JSFiddle Plugin

A plugin for [MkDocs](https://www.mkdocs.org/) that lets you
augment your code fences with an "Try it in JSFiddle" button.

## Installation

This package can be installed via pip.

```
pip install mkjsfiddle
```

Then, add `jsfiddle` to the `plugins` section of your `mkdocs.yml`
file.

```yaml
plugins:
  - jsfiddle
```

## Usage

Code fences will be left alone by default, as many code blocks may not
form a coherent block for a user to edit. To opt in for a given code fence,
add `jsfiddle-` to your fence language declaration, like so.

~~~markdown
```jsfiddle-html
<!DOCTYPE html>
<!-- Some content here -->
```
~~~

The `html` above will be preserved for syntax highlighting, and the
`jsfiddle-` will be dropped. Other languages are theoretically
supported, but will have no impact besides code highlighting.

The default behavior is for a simple HTML parser to extract the inline JS
and CSS elements and put their contents in the appropriate JSFiddle panels.
More specifically, if you have a `script` tag with the attribute `type=text/javascript`
AND not having the `src` attribute, or if you have a `style` tag with the attribute
`type=text/css`, it will be extracted to the appropriate panel. If you have multiple
of these, they will all be extracted and concatenated with some newlines thrown in as
breaks.

If you prefer to opt out of this behavior and just dump everything as-is into
the HTML box, you can add `-htmlonly` to the language string (for a full string that
looks something like `jsfiddle-html-htmlonly`).

## Known limitations

We attempt to keep formatting as-is, but make no guarantees in the default mode. The
`-htmlonly` option however should preserve formatting (if it does not, please submit
a bug report). This has been developed and tested with [Material for MkDocs](https://github.com/squidfunk/mkdocs-material),
and has not been tested extensively with additional styles. Pull requests to improve styling
are welcome.
