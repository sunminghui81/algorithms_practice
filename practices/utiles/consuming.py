import time


def consuming(func):
    a = time.time()
    def inner(*args, **kwargs):
        r = func(*args, **kwargs)
        print('used', time.time() - a, 'seconds')
        return r
    return inner