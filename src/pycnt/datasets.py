from importlib import resources

def get_flatland():
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.PosixPath
        Path to file.

    References
    ----------
    .. [1] E.A. Abbot, 'Flatland', Seeley & Co., 1884.
    """
    with resources.path('pycnt.data', 'flatland.txt') as f:
        data_file_path = f
    return data_file_path

