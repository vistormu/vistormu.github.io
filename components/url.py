import os


def function(href: str, alt_text: str | None = None) -> str:
    if not href.startswith("http") and not href.startswith("/"):
        raise ValueError(f"href must start with http or /: {href}")

    if href.startswith("/") and not os.path.exists("html"+href+".html"):
        raise ValueError(f"file does not exist: {href}")

    return f"<a href=\"{href}\">{alt_text if alt_text is not None else href}</a>\n"
