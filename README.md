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
`configs/` folder.  Currently only `pygments.style` is used:

```ini
[pygments]
style = tango
```

You can use this to select any of the built-in Pygments styles.  Support for
custom styles will come in the future.

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
