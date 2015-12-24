from setuptools import setup

setup(
    name='lektor-markdown-highlighter',
    description='Adds syntax highlighting support with Pygments to markdown.',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    url='http://github.com/lektor/lektor-markdown-highlighter',
    version='0.1',
    license='BSD',
    py_modules=['lektor_markdown_highlighter'],
    entry_points={
        'lektor.plugins': [
            'markdown-highlighter = lektor_markdown_highlighter:MarkdownHighlighterPlugin',
        ]
    },
    install_requires=[
        'Pygments',
    ]
)
