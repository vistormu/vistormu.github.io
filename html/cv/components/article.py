def function(title: str, subtitle: str) -> str:
    title_style = " ".join([
        "text-xl",
        "text-slate-800",
        "leading-none",
        "mb-2",
    ])

    subtitle_style = " ".join([
        "font-serif",
        "text-gray-600",
    ])

    return f'''
    <div class="mx-1 my-2.5">
        <h3 class="{title_style}">{title}</h3>
        <p class="{subtitle_style}">{subtitle}</p>
    </div>
    '''
