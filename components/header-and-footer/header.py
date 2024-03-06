def function() -> str:
    highlight_js: str = '''
    <link id="highlight-style" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/highlight.min.js"></script>
    '''

    blog_src = "/index.html"
    about_src = "/about.html"

    header_style = ' '.join([
        "sticky",
        "top-0",
        "bg-black",
        "z-50",
    ])

    content_style = ' '.join([
        "header",
        "flex",
        "justify-between",
        "items-center",
        "max-w-4xl",
        "mx-auto",
        "p-4",
        "ease-linear",
        "duration-200",
    ])

    title_style = ' '.join([
        "text-white",
        "text-2xl",
        "font-bold",
    ])

    nav_style = ' '.join([
        "nav-link",
        "flex",
        "space-x-4",
        "text-white",
    ])

    content_wrapper_style = ' '.join([
        "max-w-4xl",
        "mx-auto",
        "px-4",
    ])

    return f'''
    {highlight_js}
    <header class="{header_style}">
        <div class="{content_style}">
            <a class="{title_style}" href="{blog_src}">Vistor's Blog</a>
            <a class="{nav_style}" href="{about_src}">about</a>
        </div>
    </header>

    <div class="{content_wrapper_style}">
    '''
