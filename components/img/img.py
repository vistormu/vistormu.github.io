def img(src: str, width: str, align: str) -> str:
    return f"""
<div class="flex justify-{align}">
    <img class="h-auto w-{width}" src="{src}">
</div>
"""
