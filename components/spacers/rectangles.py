import random


def function(alignment: str) -> str:
    colors: list[str] = [
        "white",
        "red",
        "green",
        "blue",
        "light-blue",
        "yellow",
        "violet",
        "orange",
        "pink",
    ]

    color_1: str = random.choice(colors)
    color_2: str = random.choice(colors)
    while color_2 == color_1:
        color_2 = random.choice(colors)

    width_1: int = random.randint(48, 275)
    gutter_1: int = random.randint(48, 100)

    width_2: int = random.randint(48, 275)
    gutter_2: int = random.randint(48, 100)

    gap: int = random.randint(5, 15)

    return f'''
    <div style="position: relative; height: 10px; width: 100%;">
        <div style="height: 10px;"></div>
        <div class="rectangle" style="background-color: var(--{color_1}); width: {width_1}px; {alignment}: {gutter_1}px;"></div>
        <div style="height: {gap}px;"></div>
        <div class="rectangle" style="background-color: var(--{color_2}); width: {width_2}px; {alignment}: {gutter_2}px;"></div>
    </div>
    '''
