"""
Graph Representations : Adjacency List
=====================   ==============

The graph must exist in computer memory first.

So, this module represents/prepares a graph 
    in an organisation scheme which is named
    as - Adjacency List

Pseudocode of Adjacency List representation :
    - we'll create a hashmap ( here we'll use python dict for this purpose )
    - we'll create a linked list ( here we'll use python list for this purpose )
    - we'll store key,value pairs, where
        - 'key' will be the graph vertice ( i.e node )
        - 'value' will be the LinkedList of vertices to which an
            edge exists .

How we have implemented Adjacency List :
    - we keep a dict
        - this dict will store
            - 'key' as label/name of the node/vertex
            - 'value' as the object of that node/vertex
            - we don't keep 'value' as a list because the node object itself
                contains that list
    - whenever we want to add a node that connects , we call add method
        on that node object , it appends it in it's list
"""
from typing import Any, List, TypeVar, Optional, Dict, Union
from constants import ADJACENCY_LIST

T = TypeVar('T')

__all__ = [
    'GraphNode',
    'Graph'
]

# memory block that holds data
class MemoryBlock:
    """
    Represents a memory block in a doubly linked list.

    Attributes:
        data (Any): The data stored in the memory block.
    """

    def __init__(self, data: Any):
        """
        Initializes a MemoryBlock instance.

        Args:
            data (Any): The data to store in the memory block.
        """
        self._data: T = data
        self._links: List['MemoryBlock'] = []

    @property
    def data(self) -> T:
        """Gets the data stored in the memory block."""
        return self._data
    
    @data.setter
    def data(self, value: T) -> T:
        """Sets the data in the memory block."""
        self._data = value
        return self._data
    
    def __str__(self) -> str:
        """Returns a string representation of the memory block."""
        return f"{self._data}"
    
    def __repr__(self):
        """Returns a detailed string representation of the memory block."""
        return f"MemoryBlock({self._data}, links={self._links})"

# memory representation of graph vertice
class GraphNode(MemoryBlock):

    def __init__(self, label: str, data: Any):
        self._label = label
        super().__init__(data)

    @property
    def label(self):
        return self._label

    def link(self, link_to: 'GraphNode'):
        if link_to not in self._links:
            self._links.append(link_to)

    def get_links(self):
        return self._links
    
    def __str__(self) -> str:
        """Returns a string representation of the memory block."""
        return f"{self._label}"
    
    def __repr__(self):
        """Returns a detailed string representation of the memory block."""
        return f"GraphNode({self._label}, data={self._data}, links={self._links})"

# Graph
class Graph:

    def __init__(self):
        self._name = ADJACENCY_LIST
        self._store: Dict[str, GraphNode] = {}
    
    @property
    def store(self) -> Dict[str, GraphNode]:
        return self._store

    def add_node(self, node: GraphNode):
        if node.label in self._store:
            raise Exception('node already exists')
        self._store[node.label] = node

    def add_link(self, node_from: Union[str, GraphNode], node_to: Union[str, GraphNode]) -> None:
        """
        add a link from a node to
            another node
        """
        if isinstance(node_from, GraphNode):
            _from = node_from
        else:
            _from = self._store[node_from]
        if isinstance(node_to, GraphNode):
            _to = node_to
        else:
            _to = self._store[node_to]
        _from.link(_to)

    def add_edge(self, node_a: Union[str, GraphNode], node_b: Union[str, GraphNode]) -> None:
        """
        add an edge between two nodes
            - links both the nodes to
                each other
        """
        if not isinstance(node_a, GraphNode):
            node_a = self._store[node_a]
        if not isinstance(node_b, GraphNode):
            node_b = self._store[node_b]
        node_a.link(node_b)
        node_b.link(node_a)
    
    def print(self):
        print("label value : list of nodes")
        for k, v in self._store.items():
            print(' ',k, f"\t{v}   : {[str(_v) for _v in v._links]}")


def _create_undirected_adjacency_list_graph(sample: int = 1):
    """
    We are creating a graph :
        - is undirected
        - is connected
        - uses adjancency list
        
    * Graph Visual Representation :

    Sample 1 :

                                +---+                             
                                | 1 |                             
                                ----+                             
                               /                                  
                              /                                   
                             /                                    
                            /                                     
                           /                                      
                          /                                       
                         /                                        
                    +---+                     +---+               
                    | 4 |---------------------| 3 |               
                    +---+                     +---+               
                      |  \                      |                 
                      |   -\                    |                 
                      |     \                   |                 
                      |      -\               +---+               
                      |        -\          ---| 2 |               
                      |          \.   ----/   +---+              -
                      |          --\-/       /                    
-                     |     ----/   \       /                     
                      | .--/         -\    /                      
                    +---+             +---+                       
                    | 0 |-------------| 5 |                       
                    +---+             +---+
                     
    Sample 2 :

                                +---+              
                                | 1 |              
                               -+---+              
                              /                    
                             /                     
                            /                      
                           /                       
                          /                        
                         /                         
                        /                          
                    +---+                     +---+
                    | 4 |---------------------| 3 |
                    +---+\                    +---+
                      |   -\                    |  
                      |     -\                  |  
                      |       \                 |  
                      |        -\             +---+
                      |          \            | 2 |
                      |           -\          ----+
                      |             -\       /     
-                     |               \     /      
                      |                -\  /       
                    +-|-+             +---+        
                    | 0 |             | 5 |        
                    +---+             +---+        
    """
    graph = Graph()

    # nodes
    node_0 = GraphNode(0, None)
    node_1 = GraphNode(1, None)
    node_2 = GraphNode(2, None)
    node_3 = GraphNode(3, None)
    node_4 = GraphNode(4, None)
    node_5 = GraphNode(5, None)
    
    # load the nodes
    graph.add_node(node_0)
    graph.add_node(node_1)
    graph.add_node(node_2)
    graph.add_node(node_3)
    graph.add_node(node_4)
    graph.add_node(node_5)

    match sample:

        case 1:

            # links of node-0
            graph.add_edge(0, 2)
            graph.add_edge(0, 4)
            graph.add_edge(0, 5)
            # links of node-1
            graph.add_edge(1, 4)
            # links of node-2
            graph.add_edge(2, 0)
            graph.add_edge(2, 3)
            graph.add_edge(2, 5)
            # links of node-3
            graph.add_edge(3, 2)
            graph.add_edge(3, 4)
            # links of node-4
            graph.add_edge(4, 0)
            graph.add_edge(4, 1)
            graph.add_edge(4, 3)
            graph.add_edge(4, 5)
            # links of node-5
            graph.add_edge(5, 0)
            graph.add_edge(5, 2)
            graph.add_edge(5, 4)

        case 2:
            graph.add_edge(1, 4)
            graph.add_edge(4, 3)
            graph.add_edge(4, 5)
            graph.add_edge(4, 0)
            graph.add_edge(5, 2)
            graph.add_edge(2, 3)
    
    return graph

# main
def main():
    """
    Demonstrating Adjacency list representaion of
        some graphs
    """
    print(main.__doc__, '\n')
    print(_create_undirected_adjacency_list_graph.__doc__)

    print('* Graph Adjacency List Representations : \n')
    print('-'*10, 'Sample 1', '-'*10,)
    graph = _create_undirected_adjacency_list_graph(sample=1)
    graph.print()
    print('\n\n')
    print('-'*10, 'Sample 2', '-'*10,)
    graph = _create_undirected_adjacency_list_graph(sample=2)
    graph.print()
    print('-'*10, '-'*10,)

#entrypoint
if __name__ == '__main__':
    main()