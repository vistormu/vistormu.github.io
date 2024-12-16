def u(items: str) -> str:
    list_style = ' '.join([
        "list-disc",
        "list-outside",
        "mb-8",
        "pl-4",
    ])

    value: str = f'<ul class="{list_style}">\n'
    for item in items.split('\n'):
        if not item:
            continue
        value += f"\t<li>{item.strip()}</li>\n"
    value += "</ul>\n"

    return value
