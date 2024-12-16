def imp(text: str) -> str:
    class_style = " ".join([
        "flex",
        "items-start",
    ])

    div_style = " ".join([
        "flex",
        "items-center",
    ])

    img_style = " ".join([
        "h-6",
        "mr-1.5",
    ])

    text_style = " ".join([
        "text-yellow",
    ])

    return f"""
<div class="{class_style}">
    <div class="{div_style}">
        <img class="{img_style}" src="/assets/important.svg">
        <p class="{text_style}">Important: &nbsp;</p>
    </div>
    <p>{text}</p>
</div>
"""
