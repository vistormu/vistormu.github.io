def function(title: str) -> str:
    style = " ".join([
        "text-2xl",
        "text-slate-800",
        "mt-4",
        "font-medium",
    ])

    return f'<h2 class="{style}">{title}</h2>'
