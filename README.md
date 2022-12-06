# lektor-markdown-highlighter

This plugin adds support for syntax highlighting through Pygments to
Lektor's markdown support.

## Enabling the Plugin

To enable the plugin run this command:

```shell
lektor plugins add markdown-highlighter
```

## Configuring the Plugin

The plugin has a config file that is used to configure a few things
for Pygments.  Just create a file named `markdown-highlighter.ini` into your
`configs/` folder.

You can use `pygments.style` to select any of the built-in Pygments styles:

```ini
[pygments]
style = tango
```

Support for custom styles will come in the future.

You can also use `pygments.cssclass` to apply a custom CSS class
to the generated html and CSS:

```ini
[pygments]
cssclass = mycode
```

By default the plugin will use `highlight` for the CSS class.

The config file is considered the "source" for the Pygments stylesheet, so you must create the configuration file (it can be empty) or Lektor's build will prune `pygments.css`.

## In Markdown

To use the syntax highlighter you need to use fenced blocks and pass the name
of the pygments lexer after the opening fence:

    ```python
    print("Hello World!")
    ```

## In Templates

In templates the plugin provides the `get_pygments_stylesheet` function which
can be used to generate and retrieve a link to the pygments stylesheet:

```jinja
<link rel="stylesheet" href="{{ get_pygments_stylesheet()|url }}">
```

In addition the `|pygmentize` filter can be used to highlight code from
templates.  It takes one argument which is the lexer name:

```jinja
{{ 'print "Hello World!"'|pygmentize('python') }}
```
