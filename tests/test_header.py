import url2markdown.header as header


def test_undefined_topics(create_article):
    article = create_article()
    string_header = header.Header(article, [])
    result = string_header._build_header_dict()
    assert result['topics'][0] == 'to_categorise'


def test_dict_to_string(create_article):
    article = create_article()
    article.keywords = ['foo', 'bar', 'baz']
    string_header = header.Header(article, [])
    string = string_header.build_header()
    assert string == '- meta:\n  - topics: [[foo]] [[bar]] [[baz]]\n  - date: [[2020-11-09]]\n  - url: https://www.republik.ch/2020/11/09/kann-die-schweiz-auf-rendite-aus-kriegs-material-verzichten\n'
