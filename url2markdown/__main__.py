#!/usr/bin/env python
from url2markdown.cli import cli
from url2markdown.downloader import downloader
from url2markdown.file import write_to_file
from url2markdown.header import Header


def main(url, topics):
    article = downloader(url)
    header = Header(article, topics)
    write_to_file(article, header.build_header())


if __name__ == "__main__":
    args = cli()
    if args.url:
        main(args.url, args.topics)
    if args.file:
        with args.file as input_file:
            for line in input_file:
                try:
                    url, topics = line.split(' ')
                except ValueError:
                    url = line
                    topics = []
                main(url, topics)
