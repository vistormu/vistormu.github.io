def function(text: str, alignment: str = "center") -> str:
    style = " ".join([
        "text-3xl",
        "font-bold",
        "mt-8",
        "mb-4",
        f"text-{alignment}",
        "text-violet",
    ])

    anchor: str = text.replace(" ", "-").lower()

    return f'<h1 class="{style}" id="{anchor}">{text}</h1>'
