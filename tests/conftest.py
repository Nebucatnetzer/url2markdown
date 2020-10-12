import pytest

from newspaper import Article

@pytest.fixture
def create_article():
    def _create_article():
        url = 'https://www.20min.ch/story/corona-zahlen-auf-einen-blick-803083076953'
        article = Article(url)
        article.download()
        article.parse()
        return article
    return _create_article
