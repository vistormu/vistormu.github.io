head = '''
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/css/output.css">
<link id="highlight-style" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/highlight.min.js"></script>
'''


def function() -> str:
    nav_style = ' '.join([
        "flex",
        "justify-evenly",
        "max-w-4xl",
        "mx-auto",
        "p-4",
    ])

    nav_items_style = ' '.join([
        "text-lg",
        "font-semibold",
        "text-white",
        "no-underline",
    ])

    content_wrapper_style = ' '.join([
        "max-w-4xl",
        "mx-auto",
        "px-8",
    ])

    return f'''
    {head}
    <header>
        <nav class="{nav_style}">
            <a class="{nav_items_style}" href="/">about</a>
            <a class="{nav_items_style}" href="/projects">projects</a>
            <a class="{nav_items_style}" href="/tutorials">tutorials</a>
            <a class="{nav_items_style}" href="/blog">blog</a>
        </nav>
    </header>

    <div class="{content_wrapper_style}">
    '''
