def function(level=0) -> str:
    level = int(level)

    highlight_js: str = '''
    <link id="highlight-style" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/highlight.min.js"></script>
    ''' if level > 0 else ""

    blog_src: str = "./."*level + "./index.html"
    about_src: str = "./."*level + "./about.html"

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
