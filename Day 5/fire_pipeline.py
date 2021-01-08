import fire
from getpass import getpass
import inspect
from collections import OrderedDict


class Auth:

    def login(self, username=None):
        if username is None:
            username = input("Username: ")
        if username in (None, ""):
            print("A username is required")
            return
        pw = getpass("Password: ")
        return username, pw


def login(username=None):
    if username is None:
        username = input("Username: ")
    if username in (None, ""):
        print("A username is required")
        return
    pw = getpass("Password: ")
    return username, pw


class Pipeline(object):
    def __init__(self):
        self.auth = Auth()
        self.login = login

    def scrape(self, tag="python", query_filter="Votes", max_pages=50, pagesize=25):
        base_url = 'https://stackoverflow.com/questions/tagged/'
        datas = []
        for p in range(max_pages):
            page_num = p + 1
            url = f"{base_url}{tag}?tab={query_filter}&page={page_num}&pagesize={pagesize}"
            datas.append(url)
        return datas


if __name__ == "__main__":
    #  python3 fire_pipeline.py login --username "JOHN"
    #  python3 fire_pipeline.py scrape --tag Javascript
    # fire.Fire(Pipeline)

    sig = inspect.signature(login)
    print(sig.parameters.values())
