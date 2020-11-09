import pytest

from newspaper import Article


@pytest.fixture
def create_article():
    def _create_article():
        url = 'https://www.republik.ch/2020/11/09/kann-die-schweiz-auf-rendite-aus-kriegs-material-verzichten'
        article = Article(url)
        article.download()
        article.parse()
        return article
    return _create_article
