from time import perf_counter


def timer():
    start = perf_counter()

    def inner():
        nonlocal start
        start = perf_counter() - start
        return start

    return inner


a = timer()
print(a())
