import markdownify


def write_to_file(article, header):
    with open(str(article.title) + ".md", 'a') as f:
    markdown = markdownify.markdownify(article.html, heading_style='ATX')
        f.write(header)
        f.write(markdown)
