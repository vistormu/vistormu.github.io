def h3(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()

    styles: list[str] = [
        "text-xl",
        "mt-8",
        "text-green",
    ]
    style: str = " ".join(styles)

    return f'<h3 class="{style}" id="{anchor}">\n\t{text}\n</h3>\n'
