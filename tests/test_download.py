from newspaper import Article
from url2markdown.downloader import downloader


def test_get_content():
    article = downloader('https://www.20min.ch/story/corona-zahlen-auf-einen-blick-803083076953')
    assert type(article) == Article
