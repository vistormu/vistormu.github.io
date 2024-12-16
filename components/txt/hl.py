def hl(text: str) -> str:
    style = ' '.join([
        "bg-gray",
        "text-white",
    ])

    return f"<mark class='{style}'>{text}</mark>"
