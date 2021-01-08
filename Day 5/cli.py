
# RAW
from getpass import getpass
name = input("What's your name?\n")
pw = getpass("What's your password?\n")
print(name, pw)

if __name__ == "__main__":

    # SYS
    import sys
    try:
        name = sys.argv[1]
    except IndexError:
        name = input("What's your name?\n")
    pw = getpass("What's your password?\n")
    print(name, pw)


    def my_const_fun(*args, **kwargs):
        print("const", args, kwargs)


    def my_defautt_fun(*args, **kwargs):
        print("default", args, kwargs)


    # ARGPARSE
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs="+")  # one or more int arguments
    parser.add_argument("--xaction", dest="math_is_fun", action="store_const", const=my_const_fun,
                        default=my_defautt_fun)
    args = parser.parse_args()
    args.math_is_fun(args.integers)


    # GOOGLE's FIRE
    import fire

    def login(name=None):
        if name is None:
            name = input("What's your name?\n")
        pw = getpass("What's your password?\n")
        return name, pw

    #  python cli_fire.py --name Pupa
    fire.Fire(login)
