import itertools


def fib(n):
    result = []

    fib1 = 0
    fib2 = 1
    result.append(fib1)
    result.append(fib2)
    if n == 1:
        return result
    for i in range(2, n+2):
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 <= n:
            result.append(fib2)
    return(result)


class FibonacchiLst:
    _instance = 0
    fib1 = 0
    fib2 = 1
    i = 0

    def __init__(self, instance):
        self._instance = instance

    def __iter__(self):
        pass

    def __next__(self):
        if self.i == 0:
            self.i += 1
            return self.fib1
        elif self.i == 1:
            self.i += 1
            return self.fib2
        else:
            self.fib1, self.fib2 = self.fib2, self.fib1 + self.fib2
            if self.fib2 <= self._instance:
                return self.fib2


def fib_iter(iterable_obj):
    start, *a, end = iterable_obj
    *res, = itertools.islice(fib(end), start, end)
    return res


def my_genn():
    res = []
    fib1 = 0
    fib2 = 1
    i = 0
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        yield fib2
        res.append(fib2)
        i += 1


def fib_iter_gen(n):
    g = my_genn()
    i = 0  
    while True:
        el = next(g) 
        if el > n:
            break
        print(el)
        i += 1


def test_fib_1():
    assert fib(1) == [0, 1], "Тривиальный случай n = 1, список [0, 1]"
def test_fib_2():
    assert fib(4) == [0, 1, 1, 2, 3], "fib(4) должно быть [0, 1, 1, 2, 3]"

if __name__ == '__main__':
    print('function fib(10)')
    print(fib(1))

    a = FibonacchiLst(5)
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())
    print(a.__next__())

    print(fib_iter(range(14)))
    fib_iter_gen(14)

    test_fib_1()
    test_fib_2()
