"""
Graph Representations : Adjacency Matrix
=====================   ================

The graph must exist in computer memory first.

So, this module represents/prepares a graph 
    in an organisation scheme which is named
    as - Adjacency Matrix

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
from typing import Any, List, TypeVar, Dict, Union, ClassVar
from graphs.constants import ADJACENCY_MATRIX

__all__ = [
    'GraphNode',
    'Graph'
]


# memory representation of graph vertice
class GraphNode:

    def __init__(self, label: str, data: Any):
        self._label = label
        self._data = data

    @property
    def data(self):
        return self._data
    
    @property
    def label(self):
        return self._label

    def __str__(self) -> str:
        """Returns a string representation of the memory block."""
        return f"{self._label}"
    
    def __repr__(self):
        """Returns a detailed string representation of the memory block."""
        return f"GraphNode({self._label}, data={self._data}"


class Mark:
    """
    It represents/stores a True/False state .

    - allows to display alternate symbol for True and False
    - provides standard methods for controlling True and False values
    """
    
    DEFAULT_STATE: ClassVar[bool] = False
    DEFAULT_DISPLAY_STATE: ClassVar[Dict[bool, Any]] = {True: '1', False: '0'}

    def __init__(self, inital_state=DEFAULT_STATE):
        self._state: bool = inital_state
        self._display_state = self.DEFAULT_DISPLAY_STATE
    
    @property
    def state(self) -> bool:
        return self._state
    
    @state.setter
    def state(self, value: bool) -> bool:
        self._state = value
        return self._state
    
    def __str__(self) -> str:
        return str(self._display_state[self._state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__str__()})"

    def on(self):
        self._state = True
    
    def off(self):
        self._state = False
    
# Graph
class Graph:

    def __init__(self, total_nodes: int = 1):
        self._name = ADJACENCY_MATRIX
        self._store: Dict[str, GraphNode] = {}
        self._matrix: List[List[bool]] = [[ Mark() for __ in range(total_nodes)] for _ in range(total_nodes)]
        self._label_index_map: Dict[str, str] = {}
        self._counter = 0

    @property
    def store(self) -> Dict[str, GraphNode]:
        return self._store

    def add_node(self, node: GraphNode):
        if node.label in self._store:
            raise Exception('node already exists')
        # registers a node for reference by label
        self._store[node.label] = node
        # registers the label against the indexed in adjacency matrix
        self._label_index_map[node.label]=self._counter
        self._counter += 1

    def add_link(self, node_from: Union[str, GraphNode], node_to: Union[str, GraphNode]) -> None:
        """
        add a link from a node to
            another node
        """
        if isinstance(node_from, GraphNode):
            _from = node_from.label
        else:
            _from = self._store[node_from].label
        if isinstance(node_to, GraphNode):
            _to = node_to.label
        else:
            _to = self._store[node_to].label
        
        # get index for labels
        _from = self._label_index_map[_from]
        _to = self._label_index_map[_to]
        
        # mark in adjacency matrix
        self._matrix[_from][_to].on()

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
        self.add_link(node_a, node_b)
        self.add_link(node_b, node_a)
    
    def print(self):
        print('+  ', ' '.join(map(str, self._store)), '\n')
        keys = list(self._store.keys())
        seperator = ' '*max([len(str(v)) for v in keys])
        for idx, row in enumerate(self._matrix):
            print(keys[idx], ' ', seperator.join(map(str, row)))

def _create_undirected_adjacency_matrix_graph(sample: int = 1):
    """
    We are creating a graph :
        - is undirected
        - is connected
        - uses adjancency matrix
        
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
    graph = Graph(total_nodes=6)

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
    Demonstrating Adjacency matrix representaion of
        some graphs
    """
    print(main.__doc__, '\n')
    print(_create_undirected_adjacency_matrix_graph.__doc__)

    print('* Graph Adjacency List Representations : \n')
    print('-'*10, 'Sample 1', '-'*10, '\n')
    graph = _create_undirected_adjacency_matrix_graph(sample=1)
    graph.print()
    print('\n\n')
    print('-'*10, 'Sample 2', '-'*10, '\n')
    graph = _create_undirected_adjacency_matrix_graph(sample=2)
    graph.print()
    print('-'*10, '-'*10,)

#entrypoint
if __name__ == '__main__':
    main()