def function(text: str) -> str:
    style = " ".join([
        "text-3xl",
        "font-bold",
        "mt-8",
        "mb-4",
        f"text-center",
        "text-violet",
    ])

    anchor: str = text.replace(" ", "-").lower()

    return f'<h1 class="{style}" id="{anchor}">{text}</h1>'
