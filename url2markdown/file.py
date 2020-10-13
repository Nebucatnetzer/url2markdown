import os.path
import markdownify


def _build_path(title):
    ressources_folder = "~/03_documents/ressources/"
    base_filename = str(title)
    short_path = os.path.join(ressources_folder, base_filename + ".md")
    return os.path.expanduser(short_path)


def write_to_file(article, header):
    file_path = _build_path(article.title)
    markdown = markdownify.markdownify(article.html, heading_style='ATX')
    with open(file_path, 'w') as f:
        f.write(header)
        f.write('------')
        f.write('\n')
    with open(file_path, 'a') as f:
        f.write(markdown)
