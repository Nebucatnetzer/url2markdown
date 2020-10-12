import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="url2markdown",
    version="0.0.1",
    author="Nebucatnetzer",
    author_email="andreas+pypi@zweili.ch",
    description="A package to download the content of a wesbite as a Markdown file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nebucatnetzer/url2markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
