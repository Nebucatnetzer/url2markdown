import markdownify


def write_to_file(article, header):
    markdown = markdownify.markdownify(article.html, heading_style='ATX')
    with open(str(article.title) + ".md", 'w') as f:
        f.write(header)
        f.write('------')
        f.write('\n')
    with open(str(article.title) + ".md", 'a') as f:
        f.write(markdown)
