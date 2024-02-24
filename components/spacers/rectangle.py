import random


def function(alignment: str) -> str:
    colors: list[str] = [
        "white",
        "red",
        "green",
        "blue",
        "orange",
        "yellow",
        "violet",
        "pink",
    ]

    color: str = random.choice(colors)
    width: int = random.randint(48, 275)
    gutter: int = random.randint(48, 100)

    html: str = '<div style="position: relative; height: 10px; width: 100%;">'
    html += f'<div class="rectangle" style="background-color: var(--{color}); width: {width}px; {alignment}: {gutter}px;"></div>'
    html += '</div>'

    return html
