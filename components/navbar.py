def function(*items: str) -> str:
    items_html = ""
    for item in items:
        anchor = item.replace(" ", "-").lower()
        items_html += f"<a href='#{anchor}'>{item}</a>"

    return f'''
    <div class="card-carousel w-full flex justify-between">
        {items_html}
    </div>
    '''
