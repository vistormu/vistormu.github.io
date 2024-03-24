import os


def function(title: str, description: str, date: str, link: str) -> str:
    if link and not link.startswith("/"):
        raise ValueError(f"Ensure that the link starts with a forward slash: {link}")

    if link and not os.path.exists(link[1:]):
        raise ValueError(f"File not found: {link}")

    card_style = ' '.join([
        "relative",
        "w-full",
        "h-64",
        "border-2",
        "border-white",
        "p-4",
        "my-2",
        "max-md:h-72",
    ])

    title_style = ' '.join([
        "pb-2",
        "text-2xl",
        "font-bold",
        "text-blue",
    ])

    date_style = ' '.join([
        "absolute",
        "bottom-4",
        "left-4",
        "p-2",
        "text-sm",
        "text-orange",
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
    <article class="{card_style}">
        <div class="{title_style}">{title}</div>
        <p>{description}</p>
        <div class="{date_style}">{date if link else "coming soon"}</div>
        {button if link else ""}
    </article>
    '''
