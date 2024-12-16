def url(path: str, description: str | None = None) -> str:
    if not description:
        description = path

    return f'<a href="{path}">{description}</a>'
