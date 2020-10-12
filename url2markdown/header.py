def _get_topics_from_cli():
    pass


def _build_header_dict(article):
    header = {}
    header['topics'] = _get_topics_from_cli()
    if article.authors:
        header['authors'] = article.authors
    if article.keywords:
        header['topics'].append(article.keywords)
    if not header['topics']:
        header['topics'] = ['to_categorise']
    return header


def build_header(header):
    yaml = ""
    return yaml
