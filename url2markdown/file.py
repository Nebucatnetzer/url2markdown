import markdownify


def write_to_file(article, header):
    markdown = markdownify.markdownify(article.html)
    with open(str(article.title) + ".md", 'a') as f:
        f.write(header)
        f.write(markdown)
