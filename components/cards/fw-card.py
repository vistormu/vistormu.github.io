def function(title: str, description: str, link: str) -> str:
    if link and not link.startswith("http"):
        raise ValueError(f"Ensure that the link is a valid HTTP address: {link}")

    card_style = ' '.join([
        "relative",
        "w-full",
        "h-64",
        "border-2",
        "border-white",
        "p-4",
        "my-2",
    ])

    title_style = ' '.join([
        "pb-2",
        "text-2xl",
        "font-bold",
        "text-violet",
    ])

    button_container_style = ' '.join([
        "absolute",
        "bottom-4",
        "right-4",
        "group",
    ])

    button_style = ' '.join([
        "relative",
        "flex",
        "items-center",
        "justify-between",
        "p-2",
        "w-24",
        "h-10",
        "bg-red",
        "text-black",
        "font-bold",
    ])

    square_style = ' '.join([
        "absolute",
        "-bottom-4",
        "-right-1",
        "w-8",
        "h-8",
        "bg-black",
        "duration-300",
        "ease-linear",
        "origin-right",
        "group-hover:w-0",
    ])

    circle_style = ' '.join([
        "absolute",
        "-bottom-2",
        "right-1",
        "w-4",
        "h-4",
        "bg-red",
        "rounded-full",
    ])

    button: str = f'''
    <div class="{button_container_style}">
        <a href="{link}" class="{button_style}">
            <span>READ</span>
            <div class="relative">
                <div class="{square_style}"></div>
                <div class="{circle_style}"></div>
            </div>
        </a>
    </div>
    '''

    return f'''
    <div class="{card_style}" style="flex: 0 0 auto;">
        <div class="{title_style}">{title}</div>
        <p>{description}</p>
        {button if link else ""}
    </div>
    '''
