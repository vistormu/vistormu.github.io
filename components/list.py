def function(*items: tuple[str]) -> str:
    value: str = "<ul>\n"
    for item in items:
        value += f"\t<li>{item}</li>\n"
    value += "</ul>\n"

    return value
