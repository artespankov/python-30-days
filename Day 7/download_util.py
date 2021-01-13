import os
import shutil
import requests


def download_file(url, directory, fname=None):
    if fname is None:
        fname = os.path.basename(url)
    path = os.path.join(directory, fname)
    with requests.get(url, stream=True) as r:
        with open(path, 'wb') as f:
            shutil.copyfileobj(fsrc=r.raw, fdst=f)
