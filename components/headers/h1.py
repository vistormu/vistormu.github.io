def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()
    return f"<h1 id=\"{anchor}\">\n\t{text}\n</h1>\n"
