"""

"""

SOLUTION_VERSION = '1.1'

def frequency(of_numbers, in_container):
    """
    
    >>> frequency([10, 2, 3, 0, 111, 6], [5, 3, 2, 2, 1, 5, 5, 7, 5, 10, 6])
    [1, 2, 1, 0, 0, 1]

    >>> frequency([], [5, 3, 2, 2, 1, 5, 5, 7, 5, 10, 6])
    []

    >>> frequency([10, 2, 3, 0, 111, 6], [])
    [0, 0, 0, 0, 0, 0]
    """

    if SOLUTION_VERSION == '1.0':
        if not of_numbers:
            return []
        if not in_container:
            return [0]*len(of_numbers)
        frequencies: list = [0]*len(of_numbers)
        frequencies_store: dict = {}
        for num in in_container:    # O(N)
            if num in of_numbers:   # O(N)
                if num in frequencies_store:
                    frequencies_store[num] += 1
                else:
                    frequencies_store[num] = 1

        for idx, num in enumerate(of_numbers):
            if num in frequencies_store:
                frequencies[idx] = frequencies_store[num]
        return frequencies
    
    if SOLUTION_VERSION == '1.1':
        if not of_numbers:
            return []
        if not in_container:
            return [0]*len(of_numbers)

        # prepare result structure : O(N)
        frequencies: dict = {}
        for num in of_numbers:
            frequencies[num] = 0
        
        for num in in_container:        # O(N)
            if num in frequencies:      # O(1)
                frequencies[num] += 1

        return list(frequencies.values())
    
    raise NotImplementedError(f"not implemented")

if __name__ == '__main__':
    SOLUTION_VERSION = '1.1'
    value=frequency([10, 2, 3, 0, 111, 6], [5, 3, 2, 2, 1, 5, 5, 7, 5, 10, 6])
    print(value)