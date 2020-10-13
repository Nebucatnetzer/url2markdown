import argparse


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("URL",
                        help="The URL of the article to convert to Markdown.",
                        type=str)
    parser.add_argument("--topics", help="A list of comma separated topics.")
    parser.add_argument("--topics", help="A list of comma separated topics e.g. 'foo,bar'.")
    return parser.parse_args()

