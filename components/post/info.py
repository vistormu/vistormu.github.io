def info(published: str, last_edit: str, read_time: str) -> str:
    style = ' '.join([
        "text-sm",
        "text-center",
        "mb-16"
    ])

    mark_style = ' '.join([
        "bg-gray",
        "text-white",
    ])

    big_dot = "•"

    return f'''
    <div class="{style}">
        <span>published on <mark class="{mark_style}">{published}</mark></span>
        {big_dot}
        <span>last edited on <mark class="{mark_style}">{last_edit}</mark></span>
        {big_dot}
        <span><mark class="{mark_style}">{read_time} min</mark> read</span>
    </div>
    '''
