from typing import Optional
from time import time


def converter_thread(in_path: Optional[str], out_path: Optional[str]):
    time_start = time()

    print(f'Elapsed Time: {time() - time_start}s')
