def landing(title: str, subtitle: str, description: str, links: str = "") -> str:
    container_style = " ".join([
        "flex",
        "justify-center",
        "items-left",
        "h-screen",
        "flex-col",
    ])

    title_style = " ".join([
        "text-4xl",
        "font-bold",
        "text-violet",
        "mb-2",
    ])

    subtitle_style = " ".join([
        "text-xl",
        "text-red",
    ])

    links_style = " ".join([
        "text-blue",
    ])

    big_dot = "•"

    links_html = ""
    links_iter = [name.strip() for name in links.split("\n") if name.strip() != ""]
    for i, name in enumerate(links_iter):
        if "[" in name:
            name, link = name.split("[")
            link = link.replace("]", "")
        else:
            link = "#" + name.lower().replace(" ", "-")

        links_html += f'<a href="{link}" class="{links_style}">{name}</a> '
        if i < len(links_iter) - 1:
            links_html += f" {big_dot} "

    return f"""
    <div class="{container_style}">
        <h1 class="{title_style}">{title}</h1>
        <div class="{subtitle_style}">{subtitle}</div>
        <p>{description}</p>
        <span>{links_html}</span>
        <div class="h-72"></div>
    </div>
    """
