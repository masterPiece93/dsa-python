"""
Breadth First Search Traveral
=============================

Execution Command : python3 -m traversal.bfs
"""
from typing import Union, List
from representations.adjacency_list import (
    Graph as AdjacencyListGraph,
    GraphNode as AdjacencyListGraphNode
)
from representations.adjacency_matrix import (
    Graph as AdjacencyMatrixGraph,
    GraphNode as AdjacencyMatrixGraphNode,
    Types as AmTypes, # Custom types of Adjacency Matrix Implementation
    Mark
)
from utility import (
    SAMPLE_1,
    SAMPLE_2,
    SAMPLE_3,
    FormulateAdjacencyListGraph,
    FormulateAdjacencyMatrixGraph
)
from enum import Enum
from constants import ADJACENCY_LIST as CONST_ADJACENCY_LIST, ADJACENCY_MATRIX as CONST_ADJACENCY_MATRIX, EDGE_LIST as CONST_EDGE_LIST

__all__ = [
    'BfsMixin'
]

class RepresentationOptions(str, Enum):

    ADJACENCY_LIST = CONST_ADJACENCY_LIST
    ADJACENCY_MATRIX = CONST_ADJACENCY_MATRIX
    EDGE_LIST = CONST_EDGE_LIST

# from singledispatch import singledispatchmethod

class BfsMixin:
    """
    Gives capabilities to a graph to
        do a bfs traversal

    - we have 3 types of graph representations 
    - bfs implementation is seperately implemented
        for all of these implementations
    """

    def bfs(self, source: Union[str, AdjacencyListGraphNode, AdjacencyMatrixGraphNode], graph: AdjacencyMatrixGraph = None):

        match self._name:

            case RepresentationOptions.ADJACENCY_LIST:
                
                return self._for_adjacency_list(source)

            case RepresentationOptions.ADJACENCY_MATRIX:
                
                return self._for_adjacency_matrix(source, graph)
    
    def _for_adjacency_list(self, source: Union[str, AdjacencyListGraphNode]):
        """BFS Implementation for Adjacency List"""
        if not isinstance(source, AdjacencyListGraphNode):
            source = self._store[source]
        # track the linear order of arrival of nodes in traversal
        traversal_order_track: str = ''
        
        # visited flag check
        visited: set[AdjacencyListGraphNode] = set()
        # visiting queue
        to_visit: List[AdjacencyListGraphNode] = [source]
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
    
    def _for_adjacency_matrix(self, source: Union[str, AdjacencyMatrixGraphNode], graph: AdjacencyMatrixGraph):
        """BFS Implementation for Adjacency Matrix"""

        def _get_neighbour_vertices(graph: AdjacencyMatrixGraph, node: AdjacencyMatrixGraphNode) -> List[AdjacencyMatrixGraphNode]:
            """Provides Neighbouring Nodes
            [Utility]"""
            adjacency_matrix: AmTypes.AdjacencyMatrix = graph.matrix
            index: int = graph.label_index_map[node.label]
            marks: List[Mark] = adjacency_matrix[index]
            neighbours: List[AdjacencyMatrixGraphNode] = []
            for idx, mark in enumerate(marks):
                if mark.state == True:
                    neighbours.append(graph.store[graph.index_label_map[idx]])
            return neighbours
        
        if not isinstance(source, AdjacencyMatrixGraphNode):
            source = self._store[source]
        # track the linear order of arrival of nodes in traversal
        traversal_order_track: str = ''
        
        # visited flag check
        visited: set[AdjacencyListGraphNode] = set()
        # visiting queue
        to_visit: List[AdjacencyListGraphNode] = [source]
        # 
        while to_visit:
            node = to_visit.pop(0)
            visited.add(node)
            traversal_order_track += f"-> {node} "
            neighbour_nodes = _get_neighbour_vertices(graph, node)
            for node in neighbour_nodes:
                if node not in visited and node not in to_visit:
                    to_visit.append(node)
        return traversal_order_track.strip('->').strip(' ')
    

# ====
# main
# ====
def main(representation: RepresentationOptions = RepresentationOptions.ADJACENCY_LIST):

    print('\t\t-----')
    print('\t\t BFS')
    print('\t\t-----')

    match representation:
        
        case RepresentationOptions.ADJACENCY_LIST:
                
                class Graph(AdjacencyListGraph, BfsMixin):
                    """
                    Test Graph
                        - Type : Adjacency List
                        - Traversal : BFS
                    """
                
                graph = Graph()
                FormulateAdjacencyListGraph.sample_1(graph)
                print(FormulateAdjacencyListGraph.sample_1.__doc__)
                print(SAMPLE_1)
                result = graph.bfs(0)
                print('\tBFS of Graph 1 : ', result)
                assert result == '0 -> 1 -> 2 -> 3 -> 4' # expected order of bfs from node 0

                print('\n', '-'*10, '\n')

                graph = Graph()
                graph = FormulateAdjacencyListGraph.sample_2(graph)
                print(FormulateAdjacencyListGraph.sample_2.__doc__)
                print(SAMPLE_2)
                result = graph.bfs(0)
                print('\tBFS of Graph 2 : ', result)
                assert result == '0 -> 2 -> 3 -> 1 -> 4' # expected order of bfs from node 0

                print('\n', '-'*10, '\n')

                graph = Graph()
                graph = FormulateAdjacencyListGraph.sample_3(graph)
                print(FormulateAdjacencyListGraph.sample_3.__doc__)
                print(SAMPLE_3)
                result = graph.bfs(0)
                print('\tBFS of Graph 3 : ', result)
                assert result == '0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6' # expected order of bfs from node 0

                print('\t\t\n--x--\n')
        
        case RepresentationOptions.ADJACENCY_MATRIX:

            class Graph(AdjacencyMatrixGraph, BfsMixin):
                """
                Test Graph
                    - Type : Adjacency Matrix
                    - Traversal : BFS
                """
            
            graph = Graph(total_nodes=5)
            FormulateAdjacencyMatrixGraph.sample_1(graph)
            print(FormulateAdjacencyMatrixGraph.sample_1.__doc__)
            print(SAMPLE_1)
            result = graph.bfs(0, graph)
            print('\tBFS of Graph 1 : ', result)
            expected = '0 -> 1 -> 2 -> 3 -> 4'
            assert result == expected, f"{expected=} , got {result}" # expected order of bfs from node 0

            print('\n', '-'*10, '\n')

            graph = Graph(total_nodes=5)
            graph = FormulateAdjacencyMatrixGraph.sample_2(graph)
            print(FormulateAdjacencyMatrixGraph.sample_2.__doc__)
            print(SAMPLE_2)
            result = graph.bfs(0, graph)
            print('\tBFS of Graph 2 : ', result)
            expected='0 -> 1 -> 2 -> 3 -> 4'
            assert result == expected, f"{expected=} , got {result}" # expected order of bfs from node 0
            print('\n', '-'*10, '\n')

            graph = Graph(total_nodes=7)
            graph = FormulateAdjacencyMatrixGraph.sample_3(graph)
            print(FormulateAdjacencyMatrixGraph.sample_3.__doc__)
            print(SAMPLE_3)
            result = graph.bfs(0, graph)
            print('\tBFS of Graph 3 : ', result)
            expected='0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6'
            assert result == expected, f"{expected=} , got {result}" # expected order of bfs from node 0
            print('\t\t\n--x--\n')
    
        case RepresentationOptions.EDGE_LIST:
            ...
        
    
# ==========
# entrypoint
# ==========
if __name__ == '__main__':
    main(representation=RepresentationOptions.ADJACENCY_MATRIX)

