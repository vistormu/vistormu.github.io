def nav() -> str:
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
<header>
    <nav class="{nav_style}">
        <a class="{nav_items_style}" href="/">about</a>
        <a class="{nav_items_style}" href="/projects">projects</a>
        <a class="{nav_items_style}" href="/research">research</a>
        <a class="{nav_items_style}" href="/tutorials">tutorials</a>
        <a class="{nav_items_style}" href="/blog">blog</a>
    </nav>
</header>

<div class="{content_wrapper_style}">
'''
