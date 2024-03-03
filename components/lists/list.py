def function(*items: tuple[str]) -> str:
    list_style = ' '.join([
        "list-disc",
        "list-inside",
        "mb-8",
    ])

    value: str = f'<ul class="{list_style}">\n'
    for item in items:
        value += f"\t<li>{item}</li>\n"
    value += "</ul>\n"

    return value
