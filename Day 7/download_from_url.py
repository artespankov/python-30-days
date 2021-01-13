import os
import requests
from download_util import download_file

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)


url = "https://media.timeout.com/images/105236338/image.jpg"
r = requests.get(url, stream=True)
r.raise_for_status()

downloaded_image_path = os.path.join(DOWNLOADS_DIR, 'cali.jpg')

# smallish items
with open(downloaded_image_path, 'wb') as f:
    f.write(r.content)

download_file(url, DOWNLOADS_DIR, fname="memento.jpg")
