def function(file: str, language: str, code: str) -> str:
    special_characters = {
        '<': '&lt;',
        '>': '&gt;',
    }

    for key, value in special_characters.items():
        code = code.replace(key, value)

    file_style = ' '.join([
        "text-orange",
        "mt-4",
        "text-sm",
    ])

    pre_style = ' '.join([
        "border",
        "border-white",
        "overflow-x-auto",
        "p-4",
        "mb-8",
    ])

    code_style = ' '.join([
        "!bg-black",
        "!text-sm",
        f"language-{language if language else 'none'}",
    ])

    copy_button_style = ' '.join([
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

    file_html = f'<div class="{file_style}">{file}</div>' if file else ''

    return f"""
    {file_html}
    <div class="relative">
        <pre class="{pre_style}"><code class="{code_style}">{code}</code></pre>
        <button class="{copy_button_style}">copy</button>
    </div>
    """
