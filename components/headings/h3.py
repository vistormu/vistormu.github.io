def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()

    styles: list[str] = [
        "text-xl",
        "mt-8",
        "text-green",
    ]
    style: str = " ".join(styles)

    return f'<h2 class="{style}" id="{anchor}">\n\t{text}\n</h2>\n'
