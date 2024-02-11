def function(where: str = "post") -> str:
    highlight_js: str = '''
    <link id="highlight-style" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/highlight.min.js"></script>
    ''' if where == "post" else ""

    blog_src: str = "./index.html"
    if where == "post":
        blog_src = "./." + blog_src

    about_src: str = "./about.html"
    if where == "post":
        about_src = "./." + about_src

    return f"""
    {highlight_js}
    <header class="header">
        <div class="header-content">
            <div class="logo">
                <a href="{blog_src}">Vistor's Blog</a>
            </div>
            <nav>
                <a href="{about_src}" class="nav-link">about</a>
            </nav>
        </div>
    </header>

    <div class="content-wrapper">
    """
