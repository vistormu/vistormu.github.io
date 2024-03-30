def function() -> str:
    title = "Welcome!"
    subtitle = "My name is Vistor"
    description = "I am a researcher in soft robotics and a passionate programmer."

    links = {
        "about me": "/index.html#about-me",
        "GitHub": "https://github.com/vistormu",
        "email": "emailto:vimunozs@pa.uc3m.es",
        "cv": "/html/cv/cv.html"
    }

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
    for i, (name, link) in enumerate(links.items()):
        links_html += f'<a href="{link}" class="{links_style}">{name}</a> '
        if i < len(links) - 1:
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
