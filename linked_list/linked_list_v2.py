"""
Linked List V2
===========

* It is an experimental extension on 
    linked list V1 implementation 

Experiment Idea :
-----------------

* To reduce the complexity in linked
    list opeartions which is associated
    with maintaining the indexes

"""
import sys
import inspect
import dataclasses
from typing import Any, Optional, TypeVar, Dict, Union, Iterable, Generator, Tuple, Type
from collections.abc import Iterator

T = TypeVar('T')

class MemoryBlock:
    """
    Represents a memory block in a doubly linked list.

    Attributes:
        data (Any): The data stored in the memory block.
        left (Optional[MemoryBlock]): The left (previous) memory block.
        right (Optional[MemoryBlock]): The right (next) memory block.
    """

    def __init__(self, data: Any, left: Optional['MemoryBlock'] = None, right: Optional['MemoryBlock'] = None):
        """
        Initializes a MemoryBlock instance.

        Args:
            data (Any): The data to store in the memory block.
            left (Optional[MemoryBlock]): The left memory block.
            right (Optional[MemoryBlock]): The right memory block.
        """
        self._data = data
        self._left = left
        self._right = right

    @property
    def data(self) -> 'MemoryBlock':
        """Gets the data stored in the memory block."""
        return self._data

    @property
    def left(self) -> 'MemoryBlock':
        """Gets the left memory block."""
        return self._left
    
    @property
    def right(self) -> 'MemoryBlock':
        """Gets the right memory block."""
        return self._right
    
    @data.setter
    def data(self, value: T) -> T:
        """Sets the data in the memory block."""
        self._data = value
        return self._data
    
    @left.setter
    def left(self, value: T) -> T:
        """Sets the left memory block."""
        self._left = value
        return self._left
    
    @right.setter
    def right(self, value: T) -> T:
        """Sets the right memory block."""
        self._right = value
        return self._right
    
    def __str__(self) -> str:
        """Returns a string representation of the memory block."""
        return f"{self._data}"
    
    def __repr__(self):
        """Returns a detailed string representation of the memory block."""
        return f"MemoryBlock({self._data}, left={self._left}, right={self._right})"

class Index:
    """
    Represents the index of a node in the linked list.

    Attributes:
        from_start (int): The index from the start of the list.
        from_end (int): The index from the end of the list.
        parent (Optional[MemoryBlock]): The parent memory block.
    """

    def __init__(self, from_start: int, from_end: int, parent: Optional['MemoryBlock'] = None):
        """
        Initializes an Index instance.

        Args:
            from_start (int): The index from the start of the list.
            from_end (int): The index from the end of the list.
            parent (Optional[MemoryBlock]): The parent memory block.
        """
        self._from_start = from_start
        self._from_end = from_end
        self._parent = parent

    @property
    def parent(self):
        """Gets the parent memory block."""
        return self._parent
    
    @property
    def from_start(self):
        """Gets the index from the start of the list."""
        return self._from_start
    
    @property
    def from_end(self):
        """Gets the index from the end of the list."""
        return self._from_end
    
    @parent.setter
    def parent(self, value: 'MemoryBlock') -> 'MemoryBlock':
        """Sets the parent memory block."""
        self._parent = value
        return self._parent

    @from_start.setter
    def from_start(self, value: int) -> int:
        """Sets the index from the start of the list."""
        self._from_start = value
        return self._from_start

    @from_end.setter
    def from_end(self, value: int) -> int:
        """Sets the index from the end of the list."""
        self._from_end = value
        return self._from_end

    def __repr__(self):
        """Returns a detailed string representation of the index."""
        return f"{self.__class__.__name__}(from_start={self.from_start}, from_end={self.from_end}, parent={self.parent})"

@dataclasses.dataclass(frozen=True)
class Metadata:
    """
    Metadata for a LinkedList Node.

    Attributes:
        indexation (Optional[Index]): The index information of the node.
    """
    indexation: Optional[Index] = None


class LinkedListNode(MemoryBlock):
    """
    Represents a node in a doubly linked list.

    Attributes:
        metadata (Metadata): Metadata associated with the node.
    """

    def __init__(self, data, left=None, right=None, metadata: Metadata = Metadata()):
        """
        Initializes a LinkedListNode instance.

        Args:
            data (Any): The data to store in the node.
            left (Optional[MemoryBlock]): The left memory block.
            right (Optional[MemoryBlock]): The right memory block.
            metadata (Metadata): Metadata associated with the node.
        """
        self._metadata = metadata
        if metadata.indexation:
            metadata.indexation.parent = self
        super().__init__(data, left, right)

    @property
    def metadata(self):
        """Gets the metadata associated with the node."""
        return self._metadata


class LRIterator(Iterator):
    """
    Iterator for traversing a linked list from left to right.

    Attributes:
        _pointer (Optional[MemoryBlock]): The current memory block being traversed.
    """

    def __init__(self, ll: 'LinkedList'):
        """
        Initializes the iterator.

        Args:
            ll (LinkedList): The linked list to iterate over.
        """
        self._pointer: Optional[MemoryBlock] = ll.head.right
    
    def __next__(self):
        """
        Returns the next memory block in the iteration.

        Raises:
            StopIteration: If the end of the list is reached.
        """
        if self._pointer:
            value = self._pointer
            self._pointer = self._pointer.right
            return value
        else:
            raise StopIteration


class RLIterator(Iterator):
    """
    Iterator for traversing a linked list from right to left.

    Attributes:
        _pointer (Optional[MemoryBlock]): The current memory block being traversed.
    """

    def __init__(self, ll: 'LinkedList'):
        """
        Initializes the iterator.

        Args:
            ll (LinkedList): The linked list to iterate over.
        """
        self._pointer: Optional[MemoryBlock] = ll.tail.left

    def __next__(self):
        """
        Returns the next memory block in the iteration.

        Raises:
            StopIteration: If the start of the list is reached.
        """
        if self._pointer:
            value = self._pointer
            self._pointer = self._pointer.left
            return value
        else:
            raise StopIteration

class LinkedList:
    """
    Doubly Linked List Implementation

    -----
    Usage
    -----

    # Prepare
    >>> ll = LinkedList()
    >>> ll.append(3)
    >>> ll.prepend(4)
    >>> ll.append(8)
    >>> print(ll)
    [4, 3, 8]

    # Fetch Node data
    >>> value=ll[1]
    >>> value.data
    3
    
    # Prepend Node
    >>> ll.prepend(6)
    >>> print(ll)
    [6, 4, 3, 8]

    # Get Node by Index
    >>> value=ll[2]
    >>> value.data
    3

    # Index Map
    >>> ll.index_store
    {0: MemoryBlock(6, left=None, right=4), 1: MemoryBlock(4, left=6, right=3), 2: MemoryBlock(3, left=4, right=8), 3: MemoryBlock(8, left=3, right=None)}
    
    # Length
    >>> len(ll)
    4

    # Iteration
    >>> [v.data for v in ll]
    [6, 4, 3, 8]

    # Reverse Iteration
    # # ( It Sets the order of linkedlist in reverse )
    >>> ll.root_iterator_cls=RLIterator
    >>> [v.data for v in ll]
    [8, 3, 4, 6]

    # Reverse Iteration : Method 2
    # # - using Operations.reversed(...) function
    >>> ll.root_iterator_cls=LRIterator
    >>> print([v.data for v in Operations.reversed(ll)])
    [8, 3, 4, 6]

    # Reverse Iteration : Method 3
    # # - using builtin reversed(...) function
    >>> ll.root_iterator_cls=LRIterator
    >>> print([v.data for v in reversed(ll)])
    [8, 3, 4, 6]

    ---

    NOTES
        - does not support -ve indices as of now

    """

    def __init__(self, root_iterator_cls: Union[str, Type[Iterator]] = 'LRIterator'):
        """
        Initializes a LinkedList instance.

        Args:
            root_iterator_cls (Iterator): The iterator class used for traversal.
        """
        # Positioning Markers
        self._head = LinkedListNode(-1)
        self._tail = LinkedListNode(-1)
        # Initialization
        self._head._right = self._tail
        self._head._left = None
        self._tail._left = self._head
        self._tail._right = None
        # Index Map
        self._index_store: Dict[int, LinkedListNode] = {}
        # Config
        # # Root Iterator
        self.root_iterator_cls: Iterator = root_iterator_cls
    
    @property
    def head(self) -> LinkedListNode:
        """Gets the head node of the list."""
        return self._head
    
    @property
    def tail(self) -> LinkedListNode:
        """Gets the tail node of the list."""
        return self._tail
    
    @property
    def index_store(self) -> LinkedListNode:
        """Gets the index store of the list."""
        return self._index_store
    
    def append(self, data: Any):
        """
        Adds a new element at the end of the list.

        Args:
            data (Any): The data to append.

        Complexity:
            O(1)
        """
        # current : last-element <--- Tail
        # new : last-element <--- . <--- Tail
        last_element: LinkedListNode = self._tail.left
        
        # adjusting indexes
        index = self._tail.data
        index += 1
        new_node_index = Index(from_start=index, from_end=None)
        # creation
        new_node: LinkedListNode = LinkedListNode(data, metadata=Metadata(indexation=new_node_index))
        self._tail.left = new_node
        if last_element is self._head:
            # last_element is head
            last_element.right = new_node
            new_node.left = None
            self._head.data += 1
        else:
            self._joint(last_element, new_node)
        # storing adjusted indexes
        self._index_store[index] = new_node
        self._tail.data = index
    
    def prepend(self, data: Any):
        """
        Adds a new element at the beginning of the list.

        Args:
            data (Any): The data to prepend.

        Complexity:
            O(N)
        """
        # current : Head ---> first-element
        # new : Head ---> . ---> first-element
        first_element: LinkedListNode = self._head.right
        new_node_index = Index(from_start=0, from_end=None)
        # creation
        new_node: LinkedListNode = LinkedListNode(data, metadata=Metadata(indexation=new_node_index))
        self._head.right = new_node
        if first_element is self._tail:
            # first_element is tail
            self._tail.left = new_node
            new_node.right = None
            self._head.data += 1
        else:
            self._joint(new_node, first_element)
        # adjusting indexes
        index = self._tail.data
        index += 1
        for idx in range(index, 0, -1):
            self._index_store[idx] = self._index_store[idx-1]
            self._index_store[idx].metadata.indexation.from_start = idx
        else:
            self._index_store[0] = new_node
        self._tail.data = index
    
    def sort(self):
        raise NotImplementedError('...')
    
    def reverse(self):
        """
        Reverses a linked list

        Complexity:
            O(1)
        """
        temp = self._head._right
        while temp:
            current_node = temp
            next_node = temp._right
            current_node._left, current_node._right = current_node._right, current_node._left
            temp = next_node
        self._head._right, self._tail._left = self._tail._left, self._head._right
    
    def pop(self):
        raise NotImplementedError('...')
    
    def insert(self):
        raise NotImplementedError('...')
    
    def index(self):
        raise NotImplementedError('...')
    
    def extend(self):
        raise NotImplementedError('...')
    
    def count(self):
        raise NotImplementedError('...')
    
    def copy(self):
        raise NotImplementedError('...')
    
    def clear(self):
        raise NotImplementedError('...')
    
    def remove(self):
        raise NotImplementedError('...')
    
    def delete(self, node: LinkedListNode):
        """
        special functionality
            - it saves the time to search the node
        """
        raise NotImplementedError('...')
    
    def _joint(self, left_node: LinkedListNode, right_node: LinkedListNode) -> None:
        """
        Joins two memory blocks.

        Args:
            left_node (LinkedListNode): The left memory block.
            right_node (LinkedListNode): The right memory block.
        """
        left_node.right = right_node
        right_node.left = left_node
    
    def __rmul__(self):
        raise NotImplementedError('...')

    def __mul__(self):
        raise NotImplementedError('...')
    
    def __imul__(self):
        raise NotImplementedError('...')
    
    def __add__(self, other: 'LinkedList') -> 'LinkedList':
        new_ll = LinkedList()
        _pointer = self._head._right
        while _pointer:
            new_ll.append(_pointer.data)
            _pointer = _pointer.right
        _pointer = other._head._right
        while _pointer:
            new_ll.append(_pointer.data)
            _pointer = _pointer.right
        return new_ll
    
    def __iadd__(self):
        raise NotImplementedError('...')
    
    def __lt__(self, other: 'LinkedList') -> Optional[bool]:

        self_pointer = self._head._right
        other_pointer = other._head._right

        # iterative check for inequality resolution
        while self_pointer and other_pointer:
            if self_pointer.data < other_pointer.data:
                return True
            if self_pointer.data > other_pointer.data:
                return False
            # elements are equal
            self_pointer = self_pointer._right
            other_pointer = other_pointer.right
        # exact equality case
        if self_pointer == other_pointer == None:
            return False
        # shorter length case
        if self_pointer == None:
            return True
        if other_pointer == None:
            return False
        

    def __ge__(self, other: 'LinkedList'):
        self_pointer = self._head._right
        other_pointer = other._head._right

        # iterative check for inequality resolution
        while self_pointer and other_pointer:
            if self_pointer.data > other_pointer.data:
                return True
            if self_pointer.data < other_pointer.data:
                return False
            # elements are equal
            self_pointer = self_pointer._right
            other_pointer = other_pointer.right
        # exact equality case
        if self_pointer == other_pointer == None:
            return True
        # shorter length case
        if self_pointer == None: # LHS shorter
            return False
        if other_pointer == None: # RHS shorter
            return True
    
    def __gt__(self, other: 'LinkedList'):

        self_pointer = self._head._right
        other_pointer = other._head._right

        # iterative check for inequality resolution
        while self_pointer and other_pointer:
            if self_pointer.data > other_pointer.data:
                return True
            if self_pointer.data < other_pointer.data:
                return False
            # elements are equal
            self_pointer = self_pointer._right
            other_pointer = other_pointer.right
        # exact equality case
        if self_pointer == other_pointer == None:
            return False
        # shorter length case
        if self_pointer == None: # LHS shorter
            return False
        if other_pointer == None: # RHS shorter
            return True
        
    
    def __le__(self, other: 'LinkedList'):
        self_pointer = self._head._right
        other_pointer = other._head._right

        # iterative check for inequality resolution
        while self_pointer and other_pointer:
            if self_pointer.data < other_pointer.data:
                return True
            if self_pointer.data > other_pointer.data:
                return False
            # elements are equal
            self_pointer = self_pointer._right
            other_pointer = other_pointer.right
        # exact equality case
        if self_pointer == other_pointer == None:
            return True
        # shorter length case
        if self_pointer == None:
            return True
        if other_pointer == None:
            return False
    
    def __eq__(self, other: 'LinkedList'):
        """
        Comapring two linked lists for equlity
        """
        self_pointer = self._head._right 
        other_pointer = other.head.right

        while self_pointer and other_pointer:
            if self_pointer.data != other_pointer.data:
                return False
            self_pointer = self_pointer._right
            other_pointer = other_pointer.right
        if self_pointer == other_pointer == None:
            return True
        return False
    
    def __ne__(self, other: 'LinkedList'):
        return not self.__eq__(other)
    
    def __delitem__(self, index: int):

        _pointer = self._head._right
        while _pointer:
            if _pointer.metadata.indexation.from_start == index:
                prev_node = _pointer.left
                next_node = _pointer.right
                # link prev --> next
                if prev_node:
                    prev_node.right = next_node
                else:
                    # this means current pointer is first node
                    self._head.right = next_node
                # link next <-- prev
                if next_node:
                    next_node.left = prev_node
                else:
                    # this means current pointer is last node
                    self._tail.left = prev_node
                # resume the pointer
                _pointer = _pointer.right
                break # break from here & resume in next loop --- (1)
            _pointer = _pointer.right
        else:
            # if loop completes without being able to search a valid index
            return
        
        # decrement the indexes of remaining nodes --- (1) resuming from prev loop break
        while _pointer:
            _pointer.metadata.indexation.from_start -= 1
            self._index_store[_pointer.metadata.indexation.from_start] = _pointer
            _pointer = _pointer.right
        else:
            # new last node index stored in metadata of last node
            new_last_index = self._tail._left.metadata.indexation.from_start
            # updating tail with last index value
            self._tail._data = new_last_index
            # removing the stale index entry from index_store
            self._index_store.pop(self._tail._left.metadata.indexation.from_start+1, None)
        
    def __contains__(self, value: Union[Any, LinkedListNode]) -> bool:
        _pointer = self._head.right
        while _pointer:
            if (isinstance(value, LinkedListNode) and _pointer.data == value.data) or _pointer.data == value:
                return True
            _pointer = _pointer.right
        return False
    
    def __getitem__(self, key):
        """
        Gets an item from the linked list by index or slice.

        Args:
            key (int or slice): The index or slice to retrieve.

        Returns:
            LinkedListNode or LinkedList: The node or sublist corresponding to the key.

        Raises:
            TypeError: If the key is not an integer or slice.
        """
        if isinstance(key, int):
            # Handle integer indexing
            return self._index_store[key]
        elif isinstance(key, slice):
            # Handle slicing
            _ll = LinkedList()
            step = key.step if key.step is not None else 1
            stop = key.stop if key.stop and 0 <= key.stop < len(self._index_store) else len(self._index_store)
            start = key.start if key.start and 0 <= key.start < len(self._index_store) else 0
            
            for idx in range(start, stop, step):
                obj = self._index_store[idx]
                _ll.append(obj.data)
            return _ll
        else:
            raise TypeError("Invalid key type")

    def __setitem__(self):
        raise NotImplementedError('...')
    
    def __iter__(self):
        """
        Returns an iterator for the linked list.

        Returns:
            Iterator: The iterator for the linked list.
        """
        if inspect.isclass(self.root_iterator_cls):
            return self.root_iterator_cls(self)
        else:
            # memory efficient approach
            if self.root_iterator_cls == 'LRIterator':
                return LRIterator(self)
            if self.root_iterator_cls == 'RLIterator':
                return RLIterator(self)
            raise NotImplementedError('root_iterator_cls specified isn`t supported yet')

    def __len__(self):
        """
        Returns the length of the linked list.

        Returns:
            int: The length of the linked list.
        """
        return self._tail.data - self._head.data + 1
    
    def __sizeof__(self):
        # Calculate the size of all nodes
        all_nodes_size = sys.getsizeof(self._head) + sys.getsizeof(self._tail)
        for node in iter(self):
            all_nodes_size += sys.getsizeof(node)

        # Calculate the size of the idex store
        index_store_size = sys.getsizeof(self._index_store)

        # Calculate the size of the iterator class reference
        iterator_class_ref_size = sys.getsizeof(self.root_iterator_cls)
        
        # Add the size of the object itself (base object size)
        # This is typically the size of an empty instance of the class
        base_object_size = super().__sizeof__() 

        return base_object_size + iterator_class_ref_size + index_store_size + all_nodes_size
    
    def print_detailed_size_information(self):
        # Calculate the size of all nodes
        all_nodes_size = sys.getsizeof(self._head) + sys.getsizeof(self._tail)
        for node in iter(self):
            all_nodes_size += sys.getsizeof(node)

        # Calculate the size of the idex store
        index_store_size = sys.getsizeof(self._index_store)

        # Calculate the size of the iterator class reference
        iterator_class_ref_size = sys.getsizeof(self.root_iterator_cls)
        
        # Add the size of the object itself (base object size)
        # This is typically the size of an empty instance of the class
        base_object_size = super().__sizeof__()
        
        total = base_object_size + iterator_class_ref_size + index_store_size + all_nodes_size
        percent = lambda field: field/total*100 
        cols = ['base_object_size', 'iterator_class_ref_size', 'index_store_size', 'all_nodes_size']
        data = [
            cols,
            [locals()[v_name] for v_name in cols] + ['bytes'],
            [percent(locals()[v_name]) for v_name in cols] + ['%']
        ]

        # Using f-strings (Python 3.6+)
        header = f"| {data[0][0]:<10} | {data[0][1]:^5} | {data[0][2]:>10} | {data[0][3]:>10} |"
        print("-" * len(header))
        print(header)
        print("-" * len(header))
        for row in data[1:]:
            print(f"| {row[0]:^16.2f} | {row[1]:^23.2f} | {row[2]:^16.2f} | {row[3]:^14.2f} | {row[4]:^16} | ")
        print("-" * len(header))
        print(f"* Total Size : {total}")
        print("\n")
    
    def __reversed__(self):
        """
        Returns a reversed iterator for the linked list.

        Returns:
            Iterator: The reversed iterator for the linked list.
        """
        if self.root_iterator_cls == RLIterator:
            for pointer in LRIterator(self):
                yield pointer
        else:
            for pointer in RLIterator(self):
                yield pointer
    
    def __str__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        return f"[{', '.join([str(node.data) for node in iter(self)]).strip(',')}]"

class Operations:
    """
    Utility class for performing operations on linked lists.
    """

    @staticmethod
    def reversed(ll: LinkedList, method=1) -> Generator[LinkedListNode, None, None]:
        """
        Generates linked list nodes in reverse order.

        Args:
            ll (LinkedList): The linked list to reverse.
            method (int): The method to use for reversal (1 or 2).

        Returns:
            Generator[LinkedListNode, None, None]: A generator for the reversed nodes.

        Complexity:
            O(N)
        """
        if not issubclass(ll.root_iterator_cls, Iterator):
            raise Exception('must implement typing.Iterator class')
        
        if ll.root_iterator_cls == LRIterator:
            if method == 1:
                pointer = ll.tail.left
                while pointer:
                    yield pointer
                    pointer = pointer.left 
            elif method == 2:
                for pointer in RLIterator(ll):
                    yield pointer
        elif ll.root_iterator_cls == RLIterator:
            if method == 1:
                pointer = ll.head.right
                while pointer:
                    yield pointer
                    pointer = pointer.right 
            elif method == 2:
                for pointer in RLIterator(ll):
                    yield pointer
        else:
            raise NotImplementedError('`root_iterator_cls` not specified')
    
    @staticmethod
    def enumerate(ll: Union[LinkedList, Generator[LinkedListNode, None, None]] ) -> Generator[Tuple[int, LinkedListNode], None, None]:
        """
        Enumerates the nodes in the linked list.

        Args:
            ll (LinkedList or Generator): The linked list or generator to enumerate.

        Returns:
            Generator[Tuple[int, LinkedListNode], None, None]: A generator for the enumerated nodes.
        """
        _iterator: Iterator = iter(ll)
        for pointer in _iterator:
            yield (pointer.metadata.indexation.from_start, pointer)
    
    @staticmethod
    def ll_from(obj: Iterable) -> LinkedList:
        """
        Converts an iterable to a linked list.

        Args:
            obj (Iterable): The iterable to convert.

        Returns:
            LinkedList: The resulting linked list.
        """
        _ll = LinkedList()
        for value in obj:
            _ll.append(value)
        return _ll

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(2)
    ll.append(3)
    ll.prepend(4)
    ll.append(8)
    print(ll)
    print(len(ll.index_store))
    print(ll.tail.data)
    ll.root_iterator_cls=RLIterator
    print([v.data for v in ll])

    print("="*10)

    ll2 = LinkedList()
    ll2.append(2)
    ll2.append(6)
    ll2.append(9)
    ll2.prepend(7)
    
    print("---------------------------------------------")
    print("Original Linked List ( default : LRIterator )")
    print("---------------------------------------------")
    print("Index   :", [v.metadata.indexation.from_start for v in ll2])
    print("Element :", [v.data for v in ll2])
    print("enumerate: ", [{i: v.data} for i,v in enumerate(ll2)])
    print("Op.enumerate: ", [{i: v.data} for i,v in Operations.enumerate(ll2)])

    print()

    print("---------------------------------------------")
    print("Original Linked List ( with : RLIterator )")
    print("---------------------------------------------")
    ll2.root_iterator_cls = RLIterator
    print("Index   :", [v.metadata.indexation.from_start for v in ll2])
    print("Element :", [v.data for v in ll2])
    print("enumerate: ", [{i: v.data} for i,v in enumerate(ll2)])
    print("Op.enumerate: ", [{i: v.data} for i,v in Operations.enumerate(ll2)])
    ll2.root_iterator_cls = LRIterator # resetting to default
    print()

    print("---------------------------------------------")
    print("Original Linked List ( default : LRIterator )")
    print("\t- with `reversed` usage")
    print("---------------------------------------------")
    print("Index   :", [v.metadata.indexation.from_start for v in reversed(ll2)])
    print("Element :", [v.data for v in reversed(ll2)])
    print("enumerate: ", [{i: v.data} for i,v in enumerate(reversed(ll2))])
    print("Op.enumerate: ", [{i: v.data} for i,v in Operations.enumerate(reversed(ll2))])
    
    print("---------------------------------------------")
    print("Original Linked List ( with : RLIterator )")
    print("\t- with `reversed` usage")
    print("---------------------------------------------")
    ll2.root_iterator_cls = RLIterator
    print("Index   :", [v.metadata.indexation.from_start for v in reversed(ll2)])
    print("Element :", [v.data for v in reversed(ll2)])
    print("enumerate: ", [{i: v.data} for i,v in enumerate(reversed(ll2))])
    print("Op.enumerate: ", [{i: v.data} for i,v in Operations.enumerate(reversed(ll2))])
    ll2.root_iterator_cls = LRIterator # resetting to default
    
    print("="*10)

    ll2.reverse()
    print(ll2)
    ll2.root_iterator_cls = RLIterator
    print([v.data for v in ll2])
    
    ll4 = LinkedList()
    ll4.append(2)
    ll4.append(3)
    ll4.prepend(4)
    ll4.append(8)

    l4 = [4, 2, 3, 8]

    print(f"{ll4} | {sys.getsizeof(ll4)}")
    print(f"{l4} | {sys.getsizeof(l4)}")
    print(f"LinkedList takes {sys.getsizeof(ll4)/sys.getsizeof(l4)} times more space")
    print(f"Python list works in {sys.getsizeof(l4)/sys.getsizeof(ll4)*100} % of space as taken by Linked List")
    # ll4.root_iterator_cls = 'RLIterator'
    print(sys.getsizeof(type))

    ll4.print_detailed_size_information()

    print([v.data for v in ll4])

    ll_a=Operations.ll_from([])
    ll_b=Operations.ll_from([])
    print(ll_a == ll_b)
    

    print("Linked List InEquality Test:")
    print("============================")
    print('Initial Values :')
    list_a = Operations.ll_from([1, 5, 10])
    list_b = Operations.ll_from([1, 2, 20])
    list_c = Operations.ll_from([1, 5])
    list_d = Operations.ll_from([2, 1, 3])
    print(
    f"\tlist_a : {list_a}\n"
    f"\tlist_b : {list_b}\n"
    f"\tlist_c : {list_c}\n"
    f"\tlist_d : {list_d}\n"
    )
    print('Results :')
    print('----------------------------------------')
    print(f'|       Test      |  Got  |  Expected  |')
    print('----------------------------------------')
    print(f'| list A < list B | {(list_a > list_b)!s:^5} | {True!s:^10} |')     # True (because 5 > 2 at index 1)
    print(f'| list A < list D | {(list_a < list_d)!s:^5} | {True!s:^10} |')     # True (because 1 < 2 at index 0)
    print(f'| list C < list A | {(list_c < list_a)!s:^5} | {True!s:^10} |')     # True (list_c is a prefix of list_a)
    print(f'| list A < list C | {(list_a <= list_c)!s:^5} | {False!s:^10} |')    # False
    print("\n=========================================\n")

    combined_a_and_b = list_a+list_b
    assert all([v in combined_a_and_b for v in list_a]) and all([v in combined_a_and_b for v in list_b]) and len(combined_a_and_b) == len(list_a) + len(list_b)
    assert combined_a_and_b[:len(list_a)] == list_a
    assert combined_a_and_b[len(list_a):len(list_b)+len(list_a)] == list_b
    
    test_ll_a = Operations.ll_from([1, 2, 3, 4])
    del test_ll_a[1]
    print(test_ll_a)
    print({k:f"{v.data}" for k, v in test_ll_a.index_store.items()})
    assert test_ll_a[1].data == 3

    del test_ll_a[10]
    print(test_ll_a)
    print({k:f"{v.data}" for k, v in test_ll_a.index_store.items()})

    del test_ll_a[len(test_ll_a)-1]
    print(test_ll_a)
    print({k:f"{v.data}" for k, v in test_ll_a.index_store.items()})
    assert test_ll_a[len(test_ll_a)-1].data == 3

    del test_ll_a[0]
    print(test_ll_a)
    print({k:f"{v.data}" for k, v in test_ll_a.index_store.items()})
    assert test_ll_a[0].data == 3
