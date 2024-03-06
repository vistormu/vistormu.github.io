def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()

    styles: list[str] = [
        "text-3xl",
        "font-bold",
        "mt-8",
        "mb-4",
        "text-center",
        "text-violet",
    ]
    style: str = " ".join(styles)

    return f'<h1 class="{style}" id="{anchor}">\n\t{text}\n</h1>\n'
