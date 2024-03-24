def function(title: str, subtitle: str, date: str) -> str:
    title_style = " ".join([
        "text-xl",
        "text-slate-800",
    ])

    subtitle_style = " ".join([
        "font-serif",
        "text-gray-600",
    ])

    date_style = " ".join([
        "font-light",
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
    </div>
    '''
