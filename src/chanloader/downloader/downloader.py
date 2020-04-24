from multiprocessing.pool import ThreadPool
import threading
from typing import Any, Optional, Tuple
from time import time
from urllib.parse import urlparse

import requests
from tqdm import tqdm

from chanloader.utils import file_exists, output_path

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


def download_thread(url: str, out_path: Optional[str] = '') -> None:
    """Download all media from a thread.

    Parameters
    ----------
    url: str
        URL to the thread.
    out_path: Optional[str] = ''
        The path to the output. If not given than it will create a path in the project root.
    """
    time_start = time()

    if 'boards.4chan.org' in url:
        board = urlparse(url).path.split('/')[1]
        thread_id = urlparse(url).path.split('/')[3]
    else:
        print('No valid URL!')
        return

    if not out_path:
        out_path = output_path(board, thread_id)
    elif not out_path.endswith('/'):
        out_path = out_path + '/'

    session = requests.Session()
    session.headers.update(HEADERS)
    urls = []
    with session.get(url=f'https://a.4cdn.org/{board}/thread/{thread_id}.json') as re:
        data = re.json()
        for post in data['posts']:
            if 'tim' in post:
                dload_url = f'https://i.4cdn.org/{board}/{post["tim"]}{post["ext"]}'
                dload_info = session, dload_url, out_path
                urls.append(dload_info)

    pool = ThreadPool(8)
    lock = threading.Lock()

    for url in urls:
        pool.apply_async(_download, args=(lock, url))
    pool.close()
    pool.join()

    print(f'Elapsed Time: {time() - time_start}s')
    print(f'The thread was saved under: {out_path}')


def _download(lock: threading.Lock, entry: Tuple[Any, str, str]) -> None:
    """Download a file with given path.

    Parameters
    ----------
    lock: threading.Lock
        Lock for threading.
    entry: Tuple
        All the data needed to download a file.
        Contains request `session`, `file_url` and `out_path`.
    """
    session, file_url, out_path = entry
    file_name = file_url.split('/')[-1]

    with lock:
        if not file_exists(file_name, out_path):
            with session.get(url=file_url, stream=True) as re:
                total_size = int(re.headers.get('content-length', 0))
                block_size = 1024
                t = tqdm(total=total_size, unit='iB', unit_scale=True)

                if re.status_code == 200:
                    print(f'downloading {file_name} ...')
                    with open(out_path + file_name, 'wb') as f:
                        for data in re.iter_content(block_size):
                            t.update(len(data))
                            f.write(data)
                        print(f'Done with {file_name}.')
        else:
            print(f'File {file_name} already exists! skipping..')


# download_thread('https://boards.4chan.org/gif/thread/16897929', '/Users/deniz/Desktop/gondola')
