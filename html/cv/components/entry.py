def function(title: str, subtitle: str, date: str, description: str) -> str:
    title_style = " ".join([
        "text-xl",
        "text-slate-800",
    ])

    subtitle_style = " ".join([
        "text-slate-800",
        "font-serif",
    ])

    date_style = " ".join([
        "font-light",
    ])

    description_style = " ".join([
        "font-serif",
        "text-gray-600",
    ])

    return f'''
    <div class="mx-1">
        <div class="flex justify-between items-center mb-1">
            <div>
                <h3 class="{title_style}">{title}</h1>
                <h4 class="{subtitle_style}">{subtitle}</h2>
            </div>
            <p class="{date_style}">{date}</p>
        </div>
        <div class="{description_style}">
            <p>{description}</p>
        </div>
    </div>
    '''
