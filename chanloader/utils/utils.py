import os


def base_path() -> str:
    """Path to the project."""
    return os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))


def file_exists(file_name: str, out_path: str) -> bool:
    """Check if file exists.

    Parameters
    ----------
    file_name: str
        Name of the file.
    out_path: str
        Path to the output lol.

    Returns
    -------
    bool:
        `True` if file already exits, otherwise `False`.
    """
    file_path = out_path + file_name
    if os.path.isfile(file_path):
        return True
    return False


def output_path(path: str, board_name: str, post_id: str) -> str:
    """Generate output path for files.

    Parameters
    ----------
    path: str
        Base output path.
    board_name: str
        The name of the game ni🅱🅱a.
    post_id: str
        Post ID. Will be the name of the file.

    Returns
    -------
    path: str
        The output path to the file.
    """
    out_path = path + '/' + board_name + '/thread_' + post_id + '/'
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    return out_path


def current_path():
    return os.getcwd()



print(current_path())
