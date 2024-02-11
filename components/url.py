def function(href: str, alt_text: str | None = None) -> str:
    if alt_text is None:
        alt_text = href
    return f"<a href=\"{href}\">{alt_text}</a>\n"
