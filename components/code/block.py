def block(code: str, file: str = "", lang: str = "none") -> str:
    replacements = {
        "\n.": "\n&nbsp;",
        ">": "&gt;",
        "<": "&lt;",
    }

    for key, value in replacements.items():
        code = code.replace(key, value)

    if code.startswith("."):
        code = "&nbsp;" + code[1:]

    block_style = " ".join([
        "relative",
    ])

    file_style = " ".join([
        "absolute",
        "-top-1",
        "left-0",
        "m-2",
        "text-sm",
        "text-orange",
    ])

    copy_button_style = " ".join([
        "copy-btn",
        "absolute",
        "-top-1",
        "right-0",
        "m-2",
        "text-sm",
        "text-pink",
        "bg-transparent",
        "cursor-pointer",
    ])

    pre_style = " ".join([
        "border",
        "border-white",
        "overflow-x-auto",
        "px-4",
        "py-2",
        "mb-8",
        "mt-4",
    ])

    code_style = " ".join([
        "!bg-black",
        "!text-sm",
        f"language-{lang}",
    ])

    return f"""
<div class="{block_style}">
    <pre class="{pre_style}"><code class="{code_style}">
        {code.strip()}
    </code></pre>
    <button class="{copy_button_style}">copy</button>
    <div class="{file_style}">{file.strip()}</div>
</div>
"""
