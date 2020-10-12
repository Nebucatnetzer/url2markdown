from newspaper import Article


def downloader(url):
    article = Article(url)
    article.download()
    article.parse()
    return article
