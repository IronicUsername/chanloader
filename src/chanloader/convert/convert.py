from typing import Optional
from time import time

from converter import Converter


def converter_thread(in_path: Optional[str], out_path: Optional[str]):
    time_start = time()
    c = Converter()

    info = c.probe('/Users/deniz/Desktop/gondola/1587562550752.webm')
    print(info)
    print(f'Elapsed Time: {time() - time_start}s')
