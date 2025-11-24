# Linked List <sup>Python</sup>

```
        head
           \
            \
    None <- [1st elem] <=> [2nd elem] <=> [3rd elem] ..... <=> [nth elem] -> None
                                                                    \
                                                                     \
                                                                    tail

`<-`    : denotes a link to left side
`->`    : denotes a link to right side
`<=>`   : denotes a coloated visualisation of link from left and right.
            * `<-` + `->` = `<=>`

```

* Here we have targeted to aechieve all the operations supported by a python list to be implemented via linked list implementation .

* A Singly linked LinkedList and doubly linked LinkedList does not differ much !!

        - Nodes
                - single linked list : a node used , contains provision for link only to it's right node only OR you can design it to contain the link to it's left node only .
                - doubly linked list : a node used , contains provision for link to both it's left and right node .
        
        - Start and End Pointer
                - single linked list : only contains , head pointer , pointing to the first node of linked list
                - doubly linked list : contains both head and tail pointer , head pointing to the first node and tail pointing to the last node of the list .
        
        - Accessibility
                - single linked list : elements can be accessed only in one direction .
                        - For e.g : If i am on node `N` , I can only access node - `N+1` ( if linked left-to-right ) .
                - doubly linked list : elements can be accessed in either direction
                        - FOr e.g : If i am on node `N` , I can access both `N-1` and `N+1` .

* A Python List Implements for following `dunder` methods that give it's features that we see in real life with `lists`

        ```python
        def __rmul__(self):
        """
        """
        ...

        def __mul__(self, value: int):
        """
        """
        ...

        def __imul__(self, value: int) -> 'LinkedList':
        """
        """
        ...

        def __add__(self, other: 'LinkedList') -> 'LinkedList':
        """
        """
        ...

        def __iadd__(self, other: 'LinkedList') -> Self:
        """
        """
        ...

        def __lt__(self, other: 'LinkedList') -> Optional[bool]:
        """
        """
        ...

        def __ge__(self, other: 'LinkedList'):
        """
        """
        ...

        def __gt__(self, other: 'LinkedList'):
        """
        """
        ...

        def __le__(self, other: 'LinkedList'):
        """
        """
        ...

        def __eq__(self, other: 'LinkedList'):
        """
        """
        ...

        def __ne__(self, other: 'LinkedList'):
        """
        """
        ...

        def __delitem__(self, index: int):
        """
        """
        ...

        def __contains__(self, value: Union[Any, LinkedListNode]) -> bool:
        """
        """
        ...

        def __getitem__(self, key):
        """
        """
        ...

        def __setitem__(self):
        """
        """
        ...

        def __iter__(self):
        """
        """
        ...

        def __len__(self):
        """
        """
        ...

        def __sizeof__(self):
        """
        """
        ...

        def print_detailed_size_information(self):
        """
        """
        ...

        def __reversed__(self):
        """
        """
        ...

        def __str__(self) -> str:
        """
        Returns a string representation of the linked list.

        Returns:
                str: The string representation of the linked list.
        """
        ```