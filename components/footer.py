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


def function(where: str = "post") -> str:
    scroll_script: str = "./scripts/scroll.js"
    if where == "post":
        scroll_script = "./." + scroll_script

    copy_script: str = "./scripts/copyCode.js"
    if where == "post":
        copy_script = "./." + copy_script

    highlight_script: str = "<script> hljs.highlightAll(); </script>" if where == "post" else ""

    bar_color: str = random.choice(colors)

    return f"""
    <div style="height: 120px;"></div>
    <div class="divider" style="height: 20px; background-color: var(--{bar_color});"></div>
    <script src="{scroll_script}"></script>
    <script src="{copy_script}"></script>
    {highlight_script}
    """
