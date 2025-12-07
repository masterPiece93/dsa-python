from typing import Union, List
from adjacency_graph import AdjacencyGraph, GraphNode
from utility import FormulateAdjacencyGraph


class DfsMixin:
    """
    Gives capabilities to a graph to
        do a dfs traversal
    """
    def dfs(self, source: Union[str, GraphNode]):
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


class Graph(AdjacencyGraph, DfsMixin):
    """
    Test Graph
        - Type : Adjacency
        - Traversal : DFS
    """


# main
def main():

    print('\t\t-----')
    print('\t\t DFS')
    print('\t\t-----')

    graph = Graph()
    FormulateAdjacencyGraph.sample_1(graph)
    result = graph.dfs(0)
    print('DFS of Graph 1 : ', result)
    assert result == '0 -> 1 -> 2 -> 3 -> 4' # expected order of bfs from node 0

    print('-'*10)

    graph = Graph()
    FormulateAdjacencyGraph.sample_2(graph)
    result = graph.dfs(0)
    print('DFS of Graph 2 : ', result)
    assert result == '0 -> 2 -> 4 -> 3 -> 1' # expected order of bfs from node 0

    print('-'*10)

    graph = Graph()
    FormulateAdjacencyGraph.sample_3(graph)
    result = graph.dfs(0)
    print('DFS of Graph 3 : ', result)
    assert result == '0 -> 1 -> 3 -> 4 -> 2 -> 5 -> 6' # expected order of bfs from node 0

    print('\t\t--x--\n')

# entrypoint
if __name__ == '__main__':
    main()