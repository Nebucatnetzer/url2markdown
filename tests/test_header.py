import url2markdown.header as header


def test_undefined_topics(create_article):
    article = create_article()
    result = header._build_header_dict(article)
    assert result['topics'][0] == 'to_categorise'


def test_get_topics_from_cli():
    header._get_topics_from_cli()
    assert False


def test_dict_to_string(create_article):
    article = create_article()
    article.keywords = ['foo', 'bar', 'baz']
    raw_header = header._build_header_dict(article)
    string = header._build_header_string(raw_header)
    assert string == '- meta:\n  - topics: [[foo]] [[bar]] [[baz]]\n  - date: [[2020-10-09]]\n  - authors: [[Daniel Waldmeier]] [[Kei Zuefall]]\n  - url: https://www.20min.ch/story/corona-zahlen-auf-einen-blick-803083076953\n'
