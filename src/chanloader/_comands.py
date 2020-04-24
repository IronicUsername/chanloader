from os import path
from typing import Optional

import click

from chanloader.convert import converter_thread
from chanloader.downloader import download_thread

cli = click.Group()


@click.command()
@click.argument('thread_url', required=True)
@click.option('-o', '--output_path', type=click.Path(exists=True))
def download(thread_url: str, output_path: Optional[str]):
    """Download caller.

    Parameters
    ----------
    thread_url: str
        URL to the desired thread.
    output_path: Optional[str]
        Existing output path to output folder.

    Raises
    ------
    click.UsageError
        Throws when the given path does not exist or is invalid.
    """
    if output_path is not None and not path.isdir(output_path):
        raise click.UsageError(message='`output_path` has to exist and be a directory')

    download_thread(thread_url, output_path)


@click.command()
@click.argument('in_path', required=True)
@click.option('-o', '--out_path', type=click.Path(exists=True), required=False)
def convert(in_path, out_path):
    converter_thread(in_path, out_path)
    pass


@click.command()
@click.argument('endpoint', required=True, type=click.STRING)
@click.option('-t', '--thread_url', type=click.STRING, required=False)
@click.option('-o', '--output_path', type=click.STRING, required=False)
@click.pass_context
def selecta(ctx, endpoint: str, thread_url: Optional[str], output_path: Optional[str] = ''):
    """Choose between `download` and `convert` function.
    Give optional arguments for each case.
    Booyakasha! Checkit!
    https://www.youtube.com/watch?v=b00lc92lExw.

    Parameters
    ----------
    ctx: [type]
        idk dude... the docs told me.
        https://click.palletsprojects.com/en/7.x/advanced/#invoking-other-commands.
    endpoint: str
        The requested functionallity. Choose between `download` and `convert`.
    thread_url: Optional[str]
        URL to the desired 4chan thread.
    output_path: Optional[str] = ''
        Existing output path to output folder.

    Raises
    ------
    click.UsageError
        If the given endpoint does not exist.
    """
    endpoints = {
        'download': download,
        'convert': convert,
    }

    if endpoint in endpoints:
        if endpoint == 'download':
            ctx.invoke(download, thread_url=thread_url, output_path=output_path)
        elif endpoint == 'convert':
            ctx.invoke(convert, in_path='', out_path='')
    else:
        raise click.UsageError(message='Function not aviable!\n\n'
                                       'Aviable functions:\n'
                                       '- download -t <thread url>  -o <optional ouptut path>\n'
                                       '- convert\n')
