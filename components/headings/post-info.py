def function(published: str, last_edit: str, read_time: str) -> str:
    style = ' '.join([
        "text-sm",
        "text-center",
    ])

    mark_style = ' '.join([
        "bg-gray",
        "text-white",
    ])

    return f'''
    <div class="{style}">
        <span>Published: <mark class="{mark_style}">{published}</mark></span>
        <span>Last Edit: <mark class="{mark_style}">{last_edit}</mark></span>
        <span>Read Time: <mark class="{mark_style}">{read_time} min</mark></span>
    </div>
    '''
