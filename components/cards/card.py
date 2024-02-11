def function(title: str, description: str, date: str, link: str) -> str:
    header: str = f'<div class="card-header">{title}</div>'
    description = f'<div class="card-description">{description}</div>'
    date = f'<div class="card-date">{date if link else "coming soon"}</div>'
    button: str = f'''
    <div class="card-button-container">
        <a href="{link}" class="card-button">
            <span>READ</span>
            <div class="icon-container">
                <div class="black-square"></div>
                <div class="circle"></div>
            </div>
        </a>
    </div>
    ''' if link else ""

    return f'<div class="card">\n{header}\n{description}\n{date}\n{button}\n</div>\n'
