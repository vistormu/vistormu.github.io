def function(*items: str) -> str:
    hmtl: str = '<ul>\n'
    for item in items:
        id: str = item.replace(" ", "-").lower()
        hmtl += f'<li><a href="#{id}">{item}</a></li>\n'
    hmtl += '</ul>'

    return hmtl
