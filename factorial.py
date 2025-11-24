"""
Palindrome Number
=================

SOLUTION_VERSION = '1.0'
    looping approach
    - complexity : O(N)
SOLUTION_VERSION = '1.1'
    same approach in units broken way
    - complexity : O(N)
SOLUTION_VERSION = '1.2'
    same approach with recursion
    - complexity : O(N)

---

Run
    python3 factorial.py
Tests
    python3 -m doctest -v factorial.py
"""
from typing import Callable, Any

SOLUTION_VERSION = '1.2'


class Refrence:
    """
    Create a object around a value.

    used to make existing python's
        call-by-value to act as default
        mechanism of call-by-object-reference
    """
    def __init__(self, value: Any):
        self.v = value


class IntRef(Refrence):
    """
    Int Reference Placeholder

    Use when you want to use an integer
        as pass-by-reference

    >>> variable = IntRef(2); variable.v
    2

    >>> variable = IntRef(2); variable.v += 1; variable.v
    3
    """
    pass


class StrRef(Refrence):
    """
    Str Reference Placeholder

    Use when you want to use an string
        as pass-by-reference
    
    >>> variable = StrRef('ankit')
    >>> variable.v
    'ankit'

    >>> variable = StrRef('ankit'); variable.v += ' yadav'
    >>> variable.v
    'ankit yadav'
    """
    pass

def factorial(number: int):
    """
    >>> factorial(5)
    120

    >>> factorial(10)
    3628800

    >>> factorial(0)
    1

    >>> factorial(1)
    1
    """

    if SOLUTION_VERSION == '1.0':
        # raw
        # ===
        factorial_value = 1
        while number != 1 and number != 0:
            factorial_value *= number
            number -= 1
        return factorial_value
    if SOLUTION_VERSION == '1.1':
        # units broken
        # ============
        factorial_value = IntRef(1)
        number = IntRef(number)

        def logic(number: IntRef, factorial_value: IntRef):
            factorial_value.v *= number.v
            number.v -= 1

        def loop(condition: Callable, logic: Callable):
            while condition(number):
                logic(number, factorial_value)
        
        loop(
            lambda number: number.v != 1 and number.v != 0,
            logic=logic
        )
        return factorial_value.v
    
    if SOLUTION_VERSION == '1.2':
        # with recursion
        # ==============
        def fact(number): # while loop
            
            # condition
            if number == 1:
                return number
            if number == 0:
                return 1
            
            # logic
            next_number = number - 1
            factorial_value = number * fact(next_number)

            return factorial_value

        return fact(number)
    raise NotImplementedError(f"not implemented")

if __name__ == '__main__':
    SOLUTION_VERSION == '1.2'
    assert factorial(5)==120
