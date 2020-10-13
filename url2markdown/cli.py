import argparse


def cli():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file',
                       type=argparse.FileType('r'),
                       help="A file containing one URL per line.")
    group.add_argument('--url',
                       help="The URL of the article to convert to Markdown.",
                       type=str)
    parser.add_argument("--topics", help="A list of comma separated topics e.g. 'foo,bar'.")
    return parser.parse_args()

