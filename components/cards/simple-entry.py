import os


def function(title: str, date: str, link: str) -> str:
    if not link.startswith('/'):
        raise ValueError('Link must start with /')

    if not os.path.exists(link.lstrip('/')):
        raise ValueError('Link does not exist')

    return f'''
    <div class="m-2">
        <p>
        >> <a href="{link}">{title}</a> | {date}
        </p>
    </div>
    '''
