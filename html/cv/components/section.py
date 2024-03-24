def function(title: str) -> str:
    title_style = " ".join([
        "text-2xl",
        "font-bold",
        "text-slate-800",
        "mt-4",
    ])

    hr_style = " ".join([
        "border",
        "border-black",
        "w-full",
        "mb-4",
    ])

    title = title[0].upper() + title[1:]

    return f"""
    <h1 class="{title_style}">{title}</h1>
    <hr class="{hr_style}">
    """
