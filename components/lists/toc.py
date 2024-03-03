def function(*items: str) -> str:
    list_style: str = ' '.join([
        "list-none",
        "list-inside",
        "mb-8",
    ])

    hmtl: str = f'<ul class="{list_style}">\n'
    for item in items:
        id: str = item.replace(" ", "-").lower()
        hmtl += f'<li>-&gt;&nbsp;<a href="#{id}">{item}</a></li>\n'
    hmtl += '</ul>'

    return hmtl
