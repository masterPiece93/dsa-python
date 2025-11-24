"""
Factors of Number

SOLUTION_VERSION : controls the implementation
    of the solution currently in use .

Run
    python3 armstrong.py
Tests
    python3 -m doctest -v factors.py
"""
import math
import dataclasses
from typing import Iterable, Callable

SOLUTION_VERSION = '2.0'

@dataclasses.dataclass
class Mem:
    number: int
    factors: set

@dataclasses.dataclass
class Data:
    each_number: int
    mem: Mem


def loop(container: Iterable[int], logic: Callable, mem: Mem):
    """
    iterative loop : foreach

    >>> loop([1,2,3,4], lambda loop_data: print(f"{loop_data=}"), Mem(number=12, factors=set()))
    loop_data=Data(each_number=1, mem=Mem(number=12, factors=set()))
    loop_data=Data(each_number=2, mem=Mem(number=12, factors=set()))
    loop_data=Data(each_number=3, mem=Mem(number=12, factors=set()))
    loop_data=Data(each_number=4, mem=Mem(number=12, factors=set()))
    """
    loop_data = Data(
        each_number=0,
        mem=mem
    )
    for num in container:
        loop_data.each_number = num
        logic(loop_data)

def check_divison(data: Data):
    """
    In Each Loop we execute these statements

    >>> data=Data(each_number=2, mem=Mem(number=12, factors=set()));check_divison(data);data
    Data(each_number=2, mem=Mem(number=12, factors={2, 6}))

    >>> data=Data(each_number=2, mem=Mem(number=0, factors=set()));check_divison(data);data
    Data(each_number=2, mem=Mem(number=0, factors={0, 2}))
    """
    if data.each_number in data.mem.factors:
        return
    if data.mem.number % data.each_number == 0:
        data.mem.factors.add(data.each_number)
        data.mem.factors.add(data.mem.number // data.each_number)


def factors(number):
    """
    Complexity : O(N)

    Positive cases
    >>> factors(10) == {1, 2, 5, 10}
    True
    >>> factors(15) == {1, 3, 5, 15}
    True
    >>> factors(25) == {1, 5, 25}
    True
    >>> factors(7) == {1, 7}
    True
    >>> factors(19) == {1, 19}
    True

    Edge Cases
    >>> factors(0) == set()
    True
    >>> factors(1) == {1}
    True
    """
    if SOLUTION_VERSION == '1.0':
        mem = Mem(number=number, factors=set())     # O(1)
        loop(                                       # X O(N)
            range(1, number),
            logic=check_divison,                    # + O(2)
            mem=mem
        )
        return mem.factors
    if SOLUTION_VERSION == '1.1':
        mem = Mem(number=number, factors=set())     # O(1)
        loop(                                       # X O(N/2) => O(N)
            range(1, number//2),
            logic=check_divison,                    # + O(2)
            mem=mem
        )
        return mem.factors
    if SOLUTION_VERSION == '2.0':
        mem = Mem(number=number, factors=set())         # O(1)
        loop(                                           # X O(√n)
            range(1, math.ceil(math.sqrt(number))+1),
            logic=check_divison,                        # + O(2)
            mem=mem
        )
        return mem.factors

    raise NotImplemented(f'{SOLUTION_VERSION=} not operationsl yet')

if __name__ == '__main__':
    print(factors(25))
