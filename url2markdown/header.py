from datetime import datetime


class Header():
    def __init__(self, article, cli_topics):
        self.article = article
        if cli_topics:
            self.cli_topics = cli_topics.split(',')
        else:
            self.cli_topics = []


    def _build_header_dict(self):
        header = {}
        header['topics'] = self.cli_topics
        header['date'] = []
        if self.article.authors:
            header['authors'] = self.article.authors
        if self.article.keywords:
            if header['topics']:
                header['topics'].append(self.article.keywords)
            else:
                header['topics'] = self.article.keywords
        if not header['topics']:
            header['topics'] = ['to_categorise']
        if self.article.url:
            header['url'] = self.article.url
        if self.article.publish_date:
            header['date'].append(
                self.article.publish_date.strftime('%Y-%m-%d'))
        else:
            header['date'].append(datetime.now().strftime('%Y-%m-%d'))
        return header


    def _build_header_string(self, raw_header):
        header = "- meta:\n"
        for key, value in raw_header.items():
            if value and type(value) == list:
                content = ""
                for child in value:
                    content += " [[" + child + "]]"
                header += "  - {0}:".format(key) + content + "\n"
            elif value:
                content = " " + str(value)
                header += "  - {0}:".format(key) + content + "\n"
        return header


    def build_header(self):
        raw_header = self._build_header_dict()
        self.header = self._build_header_string(raw_header)
        return self.header
