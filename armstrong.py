"""
Armstrong Number

Run
    python3 armstrong.py
Tests
    python3 -m doctest -v armstrong.py
"""

import math

def digits_reversed(number):
    """
    Fetching Digits in reversed order
    Complexity : O(N)

    >>> print([d for d in digits_reversed(123456789)])
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    """
    while number:
        yield number%10
        number//=10

def digits(number):
    """
    Fetching Digits in original order
    Complexity : O(N+M) => O(N)

    >>> print([d for d in digits(123456789)])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    all_digits = list(digits_reversed(number))
    for digit in reversed(all_digits):
        yield digit

def iterative_loop(container, logic, op='INCR'):
    """
    A simple iteration over container.
    - can be iterated forward through 0-th to n-th index
    - can be iterated backwards through n-th to 0-th index
    
    Complexity : O(N/2) => O(N)

    >>> iterative_loop([1, 2, 3, 4], lambda _, pointer: print(pointer))
    0
    1
    2
    3

    >>> iterative_loop([1, 2, 3, 4], lambda _, pointer: print(pointer), op='DECR')
    3
    2
    1
    0
    """
    import operator
    
    length = len(container)
    class IndexPointer:
        """
        Index Pointer
        """
        def __init__(self, start: int, op=operator.add, qty=1):
            self._idx: int = start
            self._op = op
            self._qty = qty

        @property
        def idx(self) -> int:
            return self._idx
        
        def move(self):
            self._idx = self._op(self._idx, self._qty)

        def __lt__(self, b):
            return operator.lt(self._idx, b)
        def __gt__(self, b):
            return operator.gt(self._idx, b)

        def __str__(self):
            return str(self._idx)
    
    if op=='INCR':
        pointer = IndexPointer(0)
        while pointer < length:
            logic(container, pointer)
            pointer.move()
    elif op=='DECR':
        pointer = IndexPointer(length-1, op=operator.sub)
        while pointer > -1:
            logic(container, pointer)
            pointer.move()
    else:
        raise Exception('xxx')
    
    

def armstrong(number: int):
    """
    Checks If Number is Armstrong
    Complexity O(N)

    Negetive Cases
    >>> armstrong(123456)
    False

    Positive Cases
    >>> armstrong(153)
    True
    >>> armstrong(371)
    True
    >>> armstrong(9474)
    True
    """

    all_digits = list(digits_reversed(number))
    total_digits = len(all_digits)

    class Variables:
        DIGIT_SUM = 0

    # inner loop logic
    def logic_layer(container, index_pointer):
        digit = container[index_pointer.idx]
        Variables.DIGIT_SUM += math.pow(digit, total_digits)
        if Variables.DIGIT_SUM > number:
            raise Exception('break:sum-exceeded')
        
    # loop processing
    try:
        iterative_loop(all_digits, logic_layer)
    except Exception as e:
        if 'break' in str(e):
            print(e)
            return False
        raise e
    else:
        # post loop
        if Variables.DIGIT_SUM == number:
            return True
    return False

if __name__ == '__main__':
    number = 9474
    is_armstrong = armstrong(number)
    print(f"{number=} {is_armstrong=}")
