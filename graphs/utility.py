"""
Test Graphs for usage
"""
from adjacency_graph import GraphNode


class FormulateAdjacencyGraph:
    """
    Utility functions to arrange nodes in a
        adjancency graph for sample use . 
    """
    @staticmethod
    def sample_1(graph):
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

    @staticmethod
    def sample_2(graph):
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

    @staticmethod
    def sample_3(graph):
        """
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list
            
        Graph Representation :

                     ( 0 )
                    -------
                    /      \
                   /        \
                  /          \
                 /            \
                /              \
              ( 1 )           ( 2 )
               / \             / \
              /   \           /   \
             /     \         /     \
          ( 3 )   ( 4 )    ( 5 )  ( 6 )

        """
        
        # nodes
        node_0 = GraphNode(0, None)
        node_1 = GraphNode(1, None)
        node_2 = GraphNode(2, None)
        node_3 = GraphNode(3, None)
        node_4 = GraphNode(4, None)
        node_5 = GraphNode(5, None)
        node_6 = GraphNode(6, None)
        
        # load the nodes
        graph.add_node(node_0)
        graph.add_node(node_1)
        graph.add_node(node_2)
        graph.add_node(node_3)
        graph.add_node(node_4)
        graph.add_node(node_5)
        graph.add_node(node_6)

        # undirected edges
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 5)
        graph.add_edge(2, 6)
        
        return graph
