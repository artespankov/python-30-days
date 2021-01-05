import sys


def checkout(*args):
    print(f'checkout{args}')


def commit(*args):
    print(f'commit{args}')


commands = {
    'checkout': checkout,
    'co': checkout,
    'commit': commit,
    'ci': commit,
}



def filter(function, iterable):
    for e in iterable:
        if function(e):
            yield e


def is_even(number):
    return number % 2 == 0


def map(function, *iterables):
    iters = [iter(iterable) for iterable in iterables]
    while True:
        try:
            args = [next(it) for it in iters]
            yield function(*args)
        except StopIteration:
            break

def square(x):
    return x ** 2


def add(a, b):
    return a + b


if __name__ == "__main__":
    # cmd, *args = sys.argv[1:]
    # commands[cmd](*args)

    a = [1, 2, 3, 4, 5, 6, 7]

    for e in filter(is_even, a):
        print(e)

    for e in map(square, a):
        print(e)

    for e in map(lambda a, b: a + b, [1, 2, 3], [4, 5, 6]):
        print(e)


