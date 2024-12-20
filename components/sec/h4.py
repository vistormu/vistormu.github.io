def h4(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()

    styles: list[str] = [
        "font-bold",
        "text-yellow"
    ]
    style: str = " ".join(styles)

    return f'<h4 class="{style}" id="{anchor}">\n\t{text}\n</h4>\n'
