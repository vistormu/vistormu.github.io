import random

colors: list[str] = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "violet",
    "pink",
    "light-blue",
]


def function() -> str:
    bar_color: str = random.choice(colors)

    bottom_line_style = ' '.join([
        "absolute",
        "left-0",
        "right-0",
        "h-2",
        f"bg-{bar_color}",
    ])

    return f'''
    <div style="height: 120px;"></div>

    <div class="{bottom_line_style}"></div>
    <script src="/js/scroll.js"></script>
    <script src="/js/copyCode.js"></script>
    <script> hljs.highlightAll(); </script>
    '''
