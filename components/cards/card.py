import os


def function(title: str,
             subtitle: str,
             description: str,
             date: str = "",
             link: str = "",
             button_text: str = "READ",
             ) -> str:
    if link:
        if not link.startswith("http") and not link.startswith("/"):
            raise ValueError(f"Ensure that the link is a valid HTTP address or an absolute path to a file: {link}")
        elif link.startswith("/") and not os.path.exists("html"+link+".html"):
            raise ValueError(f"File not found: {link}")

    card_style = ' '.join([
        "relative",
        "w-full",
        "h-72",
        "border-2",
        "border-white",
        "p-4",
        "my-2",
        "max-md:h-96",
    ])

    title_style = ' '.join([
        "text-xl",
        "font-bold",
        "text-blue",
    ])

    subtitle_style = ' '.join([
        "text-sm",
        "text-green",
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
        <a href="{link}" target="_blank" class="{button_style}">
            <span>{button_text}</span>
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
        <div class="{subtitle_style}">{subtitle}</div>
        <p>{description}</p>
        <div class="{date_style}">{date}</div>
        {button if link else ""}
    </article>
    '''
