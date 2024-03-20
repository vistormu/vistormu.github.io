def function(*items: tuple[str]) -> str:
    list_style = ' '.join([
        "list-disc",
        "list-outside",
        "mb-8",
        "pl-4",
    ])

    value: str = f'<ul class="{list_style}">\n'
    for item in items:
        value += f"\t<li>{item}</li>\n"
    value += "</ul>\n"

    return value
