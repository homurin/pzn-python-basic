def createHtml(tag, text, **attributes):
    print(attributes)
    print(attributes.items())
    html = f'<{tag}'
    for key, val in attributes.items():
        html += f' {key}="{val}"'
    html += f'>{text}</{tag}>'
    return html


print(createHtml('a', 'hello world', href='http://url/to/link',
                 style='text-alight="center"'))
