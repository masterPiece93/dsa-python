"""
Depth First Search Traveral
===========================

Execution Command : python3 -m traversal.dfs
"""
from typing import Union, List
from representations.adjacency_list import Graph as AdjacencyGraph, GraphNode
from utility import FormulateAdjacencyGraph
from enum import Enum
from constants import ADJACENCY_LIST as CONST_ADJACENCY_LIST, ADJACENCY_MATRIX as CONST_ADJACENCY_MATRIX, EDGE_LIST as CONST_EDGE_LIST

__all__ = [
    'DfsMixin'
]


class RepresentationOptions(str, Enum):

    ADJACENCY_LIST = CONST_ADJACENCY_LIST
    ADJACENCY_MATRIX = CONST_ADJACENCY_MATRIX
    EDGE_LIST = CONST_EDGE_LIST


class DfsMixin:
    """
    Gives capabilities to a graph to
        do a dfs traversal
    
    - we have 3 types of graph representations 
    - dfs implementation is seperately implemented
        for all of these implementations
    """
    
    def dfs(self, source: Union[str, GraphNode]):

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
                    node = to_visit.pop()
                    visited.add(node)
                    traversal_order_track += f"-> {node} "
                    neighbour_nodes = node.get_links()
                    
                    for node in reversed(neighbour_nodes):
                        
                        if node not in visited and node not in to_visit:
                            to_visit.append(node)
                return traversal_order_track.strip('->').strip(' ')


# main
def main(representation: RepresentationOptions = RepresentationOptions.ADJACENCY_LIST):

    print('\t\t-----')
    print('\t\t DFS')
    print('\t\t-----')

    match representation:

        case RepresentationOptions.ADJACENCY_LIST:
            
            class Graph(AdjacencyGraph, DfsMixin):
                """
                Test Graph
                    - Type : Adjacency
                    - Traversal : DFS
                """
            
            graph = Graph()
            FormulateAdjacencyGraph.sample_1(graph)
            print(FormulateAdjacencyGraph.sample_1.__doc__)
            result = graph.dfs(0)
            print('\tDFS of Graph 1 : ', result)
            assert result == '0 -> 1 -> 2 -> 3 -> 4' # expected order of bfs from node 0

            print('\n', '-'*10, '\n')

            graph = Graph()
            FormulateAdjacencyGraph.sample_2(graph)
            print(FormulateAdjacencyGraph.sample_2.__doc__)
            result = graph.dfs(0)
            print('\tDFS of Graph 2 : ', result)
            assert result == '0 -> 2 -> 4 -> 3 -> 1' # expected order of bfs from node 0

            print('\n', '-'*10, '\n')

            graph = Graph()
            FormulateAdjacencyGraph.sample_3(graph)
            print(FormulateAdjacencyGraph.sample_3.__doc__)
            result = graph.dfs(0)
            print('\tDFS of Graph 3 : ', result)
            assert result == '0 -> 1 -> 3 -> 4 -> 2 -> 5 -> 6' # expected order of bfs from node 0

            print('\t\t--x--\n')

        case RepresentationOptions.ADJACENCY_MATRIX:
            ...
        
        case RepresentationOptions.EDGE_LIST:
            ...
        
# entrypoint
if __name__ == '__main__':
    main()