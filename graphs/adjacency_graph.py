from typing import Any, List, TypeVar, Optional, Dict, Union

T = TypeVar('T')


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


class AdjacencyGraph:

    def __init__(self):
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
        add an edge between to nodes
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
        for k, v in self._store.items():
            print(k, f"{v} : {[str(_v) for _v in v._links]}")
    
    def bfs(self, source: Union[str, GraphNode]):
        if not isinstance(source, GraphNode):
            source = self._store[source]
        # track the linear order of arrival of nodes in traversal
        traversal_order_track: str = ''
        
        # visited flag check
        visited: set[GraphNode] = set()
        # visiting queue
        to_visit: List[GraphNode] = [source]
        # 
        while to_visit:
            node = to_visit.pop(0)
            visited.add(node)
            traversal_order_track += f"-> {node}"
            neighbour_nodes = node.get_links()
            for node in neighbour_nodes:
                if node not in visited and node not in to_visit:
                    to_visit.append(node)
        return traversal_order_track.strip('->').strip(' ')

def create_undirected_adjacency_list_graph(method: int = 1):
    """
    We are creating a graph :
        - is undirected
        - is connected
        - uses adjancency list
        
    Graph Representation :

                                    (1)
                                    /
                                   /
                                  /
                                 /
                                /
                             ( 4 )--------(3)
                            /   \         |
                           /     \        |
                          /       \       |
                         /         \  ...(2)
                        /           \/   /
                       /  ........../\  /
                      /../            \/
                    (0)---------------(5)
    """
    graph = AdjacencyGraph()

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

    match method:

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
            graph.add_edge(0, 2)
            graph.add_edge(1, 4)
            graph.add_edge(4, 3)
            graph.add_edge(4, 5)
            graph.add_edge(4, 0)
            graph.add_edge(5, 2)
            graph.add_edge(2, 3)
    
    return graph


def bfs_test_graph_1():
    """
    We are creating a graph :
        - is undirected
        - is connected
        - uses adjancency list
        
    Graph Representation :

        ( 1 )-----( 2 )
          |      /  |  \
          |     /   |   \
          |    /    |    \
          |   /     |   ( 4 )
          |  /      |
        ( 0 )     ( 3 )

    """
    graph = AdjacencyGraph()
    
    # nodes
    node_0 = GraphNode(0, None)
    node_1 = GraphNode(1, None)
    node_2 = GraphNode(2, None)
    node_3 = GraphNode(3, None)
    node_4 = GraphNode(4, None)
    
    # load the nodes
    graph.add_node(node_0)
    graph.add_node(node_1)
    graph.add_node(node_2)
    graph.add_node(node_3)
    graph.add_node(node_4)

    # undirected edges
    graph.add_edge(1, 0)
    graph.add_edge(1, 2)
    graph.add_edge(0, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    
    return graph

def bfs_test_graph_2():
    """
    We are creating a graph :
        - is undirected
        - is connected
        - uses adjancency list
        
    Graph Representation :

                    ( 0 )
                    / | \
                   /  |  \
                  /   |   \
                 /    |    \
                /     |     \
             ( 2 )  ( 3 )  ( 1 )
               |
               |
               |
             ( 4 )
    """
    graph = AdjacencyGraph()
    
    # nodes
    node_0 = GraphNode(0, None)
    node_1 = GraphNode(1, None)
    node_2 = GraphNode(2, None)
    node_3 = GraphNode(3, None)
    node_4 = GraphNode(4, None)
    
    # load the nodes
    graph.add_node(node_0)
    graph.add_node(node_1)
    graph.add_node(node_2)
    graph.add_node(node_3)
    graph.add_node(node_4)

    # undirected edges
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(0, 1)
    graph.add_edge(2, 4)
    
    return graph

if __name__ == '__main__':

    print('-'*10, '-'*10,)
    graph = create_undirected_adjacency_list_graph(method=2)
    graph.print()
    print('-'*10, '-'*10,)
    graph = create_undirected_adjacency_list_graph(method=2)
    graph.print()
    print('-'*10, '-'*10,)

    graph = bfs_test_graph_1()
    result = graph.bfs(0)
    print('BFS of Graph 1 : ', result)

    print('-'*10)

    graph = bfs_test_graph_2()
    result = graph.bfs(0)
    print('BFS of Graph 2 : ', result)
