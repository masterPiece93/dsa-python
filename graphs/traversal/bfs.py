"""
Breadth First Search Traveral
=============================

Execution Command : python3 -m traversal.bfs
"""
from typing import Union, List
from representations.adjacency_list import Graph as AdjacencyListGraph, GraphNode
from utility import FormulateAdjacencyGraph
from enum import Enum
from constants import ADJACENCY_LIST as CONST_ADJACENCY_LIST, ADJACENCY_MATRIX as CONST_ADJACENCY_MATRIX, EDGE_LIST as CONST_EDGE_LIST

__all__ = [
    'BfsMixin'
]

class RepresentationOptions(str, Enum):

    ADJACENCY_LIST = CONST_ADJACENCY_LIST
    ADJACENCY_MATRIX = CONST_ADJACENCY_MATRIX
    EDGE_LIST = CONST_EDGE_LIST


class BfsMixin:
    """
    Gives capabilities to a graph to
        do a bfs traversal

    - we have 3 types of graph representations 
    - bfs implementation is seperately implemented
        for all of these implementations
    """

    def bfs(self, source: Union[str, GraphNode]):

        match self._name:

            case RepresentationOptions.ADJACENCY_LIST:
                
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
                    traversal_order_track += f"-> {node} "
                    neighbour_nodes = node.get_links()
                    for node in neighbour_nodes:
                        if node not in visited and node not in to_visit:
                            to_visit.append(node)
                return traversal_order_track.strip('->').strip(' ')


# main
def main(representation: RepresentationOptions = RepresentationOptions.ADJACENCY_LIST):

    print('\t\t-----')
    print('\t\t BFS')
    print('\t\t-----')

    match representation:
        
        case RepresentationOptions.ADJACENCY_LIST:
                
                class Graph(AdjacencyListGraph, BfsMixin):
                    """
                    Test Graph
                        - Type : Adjacency
                        - Traversal : BFS
                    """
                
                graph = Graph()
                FormulateAdjacencyGraph.sample_1(graph)
                result = graph.bfs(0)
                print('BFS of Graph 1 : ', result)
                assert result == '0 -> 1 -> 2 -> 3 -> 4' # expected order of bfs from node 0

                print('-'*10)

                graph = Graph()
                graph = FormulateAdjacencyGraph.sample_2(graph)
                result = graph.bfs(0)
                print('BFS of Graph 2 : ', result)
                assert result == '0 -> 2 -> 3 -> 1 -> 4' # expected order of bfs from node 0

                print('-'*10)

                graph = Graph()
                graph = FormulateAdjacencyGraph.sample_3(graph)
                result = graph.bfs(0)
                print('BFS of Graph 3 : ', result)
                assert result == '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6' # expected order of bfs from node 0

                print('\t\t--x--\n')
        
        case RepresentationOptions.ADJACENCY_MATRIX:
            ...
        
        case RepresentationOptions.EDGE_LIST:
            ...
        
    

# entrypoint
if __name__ == '__main__':
    main()

