from multiprocessing import Pool
from time import time
from sys import argv


def factorize_sync(*number):

    result = [list(filter(lambda x: num % x == 0, range(1, num + 1))) for num in number]
    return result

def factorize(num):
    return list(filter(lambda x: num % x == 0, range(1, num + 1)))

if __name__ == "__main__":

    nums_test = [int(x.strip(", ")) for x in argv[1:]] if len(argv) > 1 else [128, 255, 99999, 10651060, 10651070]

    # call func using multiprocessing
    start = time()
    with Pool() as pool:
        print(pool.map(factorize, nums_test))

    func_mult = start - time()

    # call synchronized func
    start = time()
    print(factorize_sync(*nums_test))
    func_sync = start - time()

    print(f"Multiprocessed func result is {func_mult} while sync code took {func_sync}, the\
        first one is {round(func_mult - func_sync, 2)} faster")

    # check function correctness
        
    a, b, c, d, e  = factorize_sync(128, 255, 99999, 10651060, 10651070)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
