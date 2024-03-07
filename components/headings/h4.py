def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()

    styles: list[str] = [
        "text-lg",
        "font-bold",
    ]
    style: str = " ".join(styles)

    return f'<h4 class="{style}" id="{anchor}">\n\t{text}\n</h4>\n'
