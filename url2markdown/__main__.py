#!/usr/bin/env python
from url2markdown.cli import cli
from url2markdown.downloader import downloader
from url2markdown.file import write_to_file
from url2markdown.header import Header


def main():
    args = cli()
    article = downloader(args.URL)
    header = Header(article, args.topics)
    write_to_file(article, header.build_header())


if __name__ == "__main__":
    main()
