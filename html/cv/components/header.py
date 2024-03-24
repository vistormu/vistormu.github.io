def function(name: str, position: str, bg_color: str) -> str:
    container_style = " ".join([
        f"bg-{bg_color}",
        "px-8",
        "py-2",
    ])

    name_style = " ".join([
        "text-4xl",
        "text-white",
        "text-black",
    ])

    position_style = " ".join([
        "text-xl",
        "text-white",
        "font-light",
    ])

    links_style = " ".join([
        "flex",
        "flex-col",
        "text-white",
        "h-full",
    ])

    links = {
        "GitHub": "https://github.com/vistormu",
        "LinkedIn": "https://www.linkedin.com/in/vistormu/",
        "Email": "emailto:vistormu@gmail.com",
        "Webpage": "https://vistormu.github.io",
    }
    alias = {
        "GitHub": "vistormu",
        "LinkedIn": "Víctor Muñoz",
        "Email": "vistormu@gmail.com",
        "Webpage": "vistormu.github.io",
    }

    first_column = ""
    second_column = ""
    for link, url in links.items():
        first_column += f"<h3>{link}:</h3>\n"
        second_column += f"<a href=\"{url}\">{alias[link]}</a>"

    return f"""
    <div class="{container_style}">
        <div class="flex justify-between items-center">
            <div>
                <h1 class="{name_style}">{name}</h1>
                <h2 class="{position_style}">{position}</h2>
            </div>
            <div class="flex justify-between items-center gap-2">
                <div class="{links_style}">
                    {first_column}
                </div>
                <div class="{links_style}">
                    {second_column}
                </div>
            </div>
        </div>
    </div>
    """
