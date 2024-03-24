head = '''
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/css/output.css">
<link id="highlight-style" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/styles/atom-one-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/10.7.0/highlight.min.js"></script>
'''


def function(part: str) -> str:
    document_style = " ".join([
        "max-w-4xl",
        "mx-auto",
    ])

    body_style = " ".join([
        "px-10",
    ])

    if part == "document":
        return f"""
        {head}
        <div class="{document_style}">
        """
    elif part == "body":
        return f"""
        <div class="{body_style}">
        """
    else:
        raise ValueError(f"part must be either 'document' or 'body', not {part}")
