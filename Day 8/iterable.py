class Range:

    def __init__(self, end, step=1):
        self.current = 0
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration()
        else:
            return_val = self.current
            self.current += self.step
            return return_val


def range_(end, step):
    current = 0
    while current < end:
        yield current
        current += step


for i in Range(10, 2):
    print(i)

r = range_(10, 2)
r.__next__()

for i in r:
    print(i)

print(dir(r))

xx = range(20)
print(xx.__next__())
xxx = (i for i in range(20))
print(xxx.__next__())
print(dir(xx))
print(dir(xxx))