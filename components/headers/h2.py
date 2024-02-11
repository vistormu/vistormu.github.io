def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()
    return f"<h2 id=\"{anchor}\">\n\t{text}\n</h2>\n"
