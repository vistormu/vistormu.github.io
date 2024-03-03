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

    container_style = ' '.join([
        "relative",
        "h-2",
    ])

    rectangle_1_style = ' '.join([
        "absolute",
        "h-2",
        f"bg-{color_1}",
    ])

    rectangle_2_style = ' '.join([
        "absolute",
        "h-2",
        f"bg-{color_2}",
    ])

    return f'''
    <div class="{container_style}">
        <div style="height: 10px;"></div>
        <div class="{rectangle_1_style}" style="width: {width_1}px; {alignment}: {gutter_1}px;"></div>
        <div style="height: {gap}px;"></div>
        <div class="{rectangle_2_style}" style="width: {width_2}px; {alignment}: {gutter_2}px;"></div>
    </div>
    '''
