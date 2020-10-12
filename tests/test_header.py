import url2markdown.header as header


def test_undefined_topics(create_article):
    article = create_article()
    result = header._build_header_dict(article)
    assert result['topics'][0] == 'to_categorise'


def test_get_topics_from_cli():
    header._get_topics_from_cli()
    assert False
