def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()

    styles: list[str] = [
        "text-2xl",
        "mt-16",
        "mb-4",
        "text-red",
        "font-bold",
    ]
    style: str = " ".join(styles)

    return f'<h2 class="{style}" id="{anchor}">\n\t{text}\n</h2>\n'
