def function(text: str) -> str:
    anchor: str = text.replace(" ", "-").lower()
    return f"<h3 id=\"{anchor}\">\n\t{text}\n</h3>\n"
