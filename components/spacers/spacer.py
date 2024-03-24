def function(height: str = "5") -> str:
    positive: bool = False if height.startswith("-") else True
    if not positive:
        height = height.lstrip("-")

    style = ' '.join([
        f"h-{height}" if positive else "",
        f"-mt-{height}" if not positive else "",
    ])

    return f'<div class="{style}"></div>\n'
