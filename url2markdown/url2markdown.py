#!/usr/bin/env python
from cli import cli
from downloader import downloader
from file import write_to_file
from header import Header


def main():
    args = cli()
    print(args.topics)
    article = downloader(args.URL)
    header = Header(article, args.topics)
    write_to_file(article, header.build_header())


if __name__ == "__main__":
    main()
