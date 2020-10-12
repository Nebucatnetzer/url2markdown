from newspaper import Article
from url2markdown.downloader import downloader


def test_get_content():
    article = downloader('https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html')
    assert type(article) == Article
