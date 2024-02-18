import random

colors: list[str] = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "pink",
    "light-blue",
]


def function(level=0) -> str:
    level = int(level)

    scroll_script: str = "./."*level + "./scripts/scroll.js"
    copy_script: str = "./."*level + "./scripts/copyCode.js"

    highlight_script: str = "<script> hljs.highlightAll(); </script>" if level > 0 else ""

    bar_color: str = random.choice(colors)

    return f"""
    <div style="height: 120px;"></div>
    <div class="divider" style="height: 20px; background-color: var(--{bar_color});"></div>
    <script src="{scroll_script}"></script>
    <script src="{copy_script}"></script>
    {highlight_script}
    """
