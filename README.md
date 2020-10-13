# url2markdown

!!!url2markdown is still under development and not suited for production yet!!!

url2markdown lets you download an URL and save it as a Markdown file.
Additionally you can provide a list of tags which will get added to the top of
the file. The main idea behind the script is to download articles and feed them
to an Obsidia.md vault already extended with internal Obsidian links.

```
url2markdown https://docs.python.org/3/howto/argparse.html --tags=Python,CLI
```

## Features

- Provide an URL on the command line.
- Provide a text file with a list of URLs and tags.

## Installation

Install url2markdown by cloning the repository and inside it run:

```bash
make init
```

## Usage

Currently you have to navigate into the repository and run `python3 url2markdown` in order to run the programm.

```bash
usage: url2markdown [-h] (--file FILE | --url URL) [--topics TOPICS]

optional arguments:
  -h, --help       show this help message and exit
  --file FILE      A file containing one URL per line.
  --url URL        The URL of the article to convert to Markdown.
  --topics TOPICS  A list of comma separated topics e.g. 'foo,bar'.
```

You can either provide the URL to an article or a file containing multiple
URLs. Make sure that you only have one URL per line. On the command line you
can optionally provide topics to which the Markdown version of the article
should get linked to.

```bash
python3 url2markdown --url https://docs.python.org/3/library/argparse.html --topics Python,command line
```

If you provide a file add the topics right behind the
URL separated by a space:

```
https://docs.python.org/3/library/argparse.html Python,command line,argparse
https://docs.pytest.org/en/latest/parametrize.html Python,pytest,argparse
```

## Contribute

- Issue Tracker: github.com/Nebucatnetzer/url2markdown/issues
- Source Code: github.com/Nebucatnetzer/url2markdown

### Development

If you want to start developing run the following two commands to make sure
your'e ready to go:

```bash
make init
make test
```

## Support

You can open an issue at the Github repository however I don't garantee any
support whatsever since this is a fully personal project more seen as an
excersice.

## License

The project is licensed under the GPLv3 license.
