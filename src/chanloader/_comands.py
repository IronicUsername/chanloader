from os import path
from typing import Optional

import click

from chanloader.downloader import download_thread


@click.command()
@click.argument(
    'thread_url',
    required=True
)
@click.option(
    '-o',
    '--output_path',
    type=click.Path(exists=True),
    required=False
)
def download(thread_url: str, output_path: Optional[str]):
    if output_path is not None and not path.isdir(output_path):
        print('`output_path` has to exist and be a directory')
        raise click.Abort()

    download_thread(thread_url, output_path)
