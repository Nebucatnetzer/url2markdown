from newspaper import Article


def downloader(url):
    article = Article(url)
    article.download()
    return article
