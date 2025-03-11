import click
import pymupdf


def filter_for_uris():
    pass


def get_all_links_gen(filename: str):
    """Gets all links from a filename that's a PDF"""
    with pymupdf.open(filename, filetype="pdf") as doc:
        for page in doc:
            links = page.get_links()
            for link in links:
                if link["kind"] == pymupdf.LINK_URI:
                    yield link
                else:
                    continue


@click.command()
@click.option("-s", "--search", prompt=True)
@click.argument('files', nargs=-1, type=click.Path(exists=True))
def get_links(files):
    results = dict()
    for file in files:
        links = [ link.uri for link in get_all_links_gen(file) ]
        # results[file] = links
        if search:
            if search in links:
                click.echo("Found")
    click.echo(results)


if __name__ == "__main__":
    get_links()
