import url2markdown.header as header


def test_build_header_dict(create_article):
    article = create_article()
    header._build_header_dict(article)
    assert False


def test_get_topics_from_cli():
    header._get_topics_from_cli()
    assert False
