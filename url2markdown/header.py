from datetime import datetime


def _get_topics_from_cli():
    pass


def _build_header_dict(article):
    header = {}
    header['topics'] = _get_topics_from_cli()
    header['date'] = []
    if article.authors:
        header['authors'] = article.authors
    if article.keywords:
        if header['topics']:
            header['topics'].append(article.keywords)
        else:
            header['topics'] = article.keywords
    if not header['topics']:
        header['topics'] = ['to_categorise']
    if article.url:
        header['url'] = article.url
    if article.publish_date:
        header['date'].append(article.publish_date.strftime('%Y-%m-%d'))
    else:
        header['date'].append(datetime.now().strftime('%Y-%m-%d'))
    return header


def _build_header_string(raw_header):
    header = "- meta:\n"
    for key, value in raw_header.items():
        if value and type(value) == list:
            content = ""
            for child in value:
                content += " [[" + child + "]]"
            header += "  - {0}:".format(key) + content + "\n"
        elif value:
            content = " " + str(value)
            header += "  - {0}:".format(key) + content + "\n"
    return header


def build_header(article):
    raw_header = _build_header_dict(article)
    header = _build_header_string(raw_header)
    return header
