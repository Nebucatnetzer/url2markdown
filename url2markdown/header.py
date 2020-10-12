def _get_topics_from_cli():
    pass


def _build_header_dict(article):
    header = {}
    header['topics'] = _get_topics_from_cli()
    if article.authors:
        header['authors'] = article.authors
    if article.keywords:
        if header['topics']:
            header['topics'].append(article.keywords)
        else:
            header['topics'] = article.keywords
    if not header['topics']:
        header['topics'] = ['to_categorise']
    return header


def _build_header_string(raw_header):
    header = "- meta:\n"
    for key, value in raw_header.items():
        if key:
            content = ""
            for child in value:
                content += " [[" + child + "]]"
        header += "  - {0}:".format(key) + content + "\n"
    return header


def build_header(article):
    raw_header = _build_header_dict(article)
    header = _build_header_string(raw_header)
    return header
