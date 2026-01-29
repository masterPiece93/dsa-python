"""
Test Graphs for usage

Here you'll get some graphs prepared for usage
    in your main codebase
"""
from representations.adjacency_list import GraphNode as AdjacencyListGraphNode, Graph as AdjacencyListGraph
from representations.adjacency_matrix import GraphNode as AdjacencyMatrixGraphNode, Graph as AdjacencyMatrixGraph
from typing import Final

SAMPLE_1: Final[str] = """

    Graph Representation :

        +--------+                  +-------+                                         
        |        |                  |       |                                         
        |   1    |------------------|   2   |                                         
        |        |                  |       |                                         
        +--------+               -/-+-------+\                                        
            |                  -/      |     -\                                      
            |                -/        |       -\                                    
            |              -/          |         -\                                  
            |            -/            |           \            	                    
            |          -/              |            -\                               
            |        -/   -            |              -\                             
            |      -/                  |                \                            
            |    -/                    |                 -\                          
        +--------+                  +-------+              -\  +-------+             
        |        |                  |       |                -\|       |             
        |   0    |                  |   3   |                  |   4   |             
        |        |                  |       |                  |       |             
        +--------+                  +-------+                  +-------+             

"""

SAMPLE_2: Final[str] = """
  
    Graph Representation :

                         +---+                
                       - | 0 | -              
                      /  +---+  \            -
                     /     |     \            
                    /      |      \           
                   /       |       \          
                  /        |        \         
                 /         |         \        
            +---+        +---+        +---+   
            | 2 |        | 3 |        | 1 |   
            +---+        +---+        +---+   
              |                               
              |                               
              |                               
            +---+                  -          
            | 4 |                             
            +---+            

"""

SAMPLE_3: Final[str] = """

    Graph Representation :

                              +---+                     
                            - | 0 | -                   
                           /  +---+  \                  
                          /           \                 
                         /             \                
                        /               \               
                       /                 \              
                      /                   \             
                 +---+                     +---+        
                 | 2 |                     | 1 |        
                 ----+                     +---+        
                /     \                   /     \       
               /       \                 /       \      
              /         \               /         \     
             /           \             /           \    
         +---+           +---+     +---+           +---+
         | 3 |           | 4 |     | 5 |           | 6 |
         +---+           +---+     +---+           +---+

"""


class FormulateAdjacencyListGraph:
    """
    Sample Graphs in Adjacency List Format
    ======================================
    Utility functions to arrange nodes in a
        adjancency graph for sample use . 
    """
    @staticmethod
    def sample_1(graph: AdjacencyListGraph):
        """
        Sample Graph 1
        ==============
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list                                                                                                             
        """
        
        # nodes
        node_0 = AdjacencyListGraphNode(0, None)
        node_1 = AdjacencyListGraphNode(1, None)
        node_2 = AdjacencyListGraphNode(2, None)
        node_3 = AdjacencyListGraphNode(3, None)
        node_4 = AdjacencyListGraphNode(4, None)
        
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
    def sample_2(graph: AdjacencyListGraph):
        """
        Sample Graph 2
        ==============
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list     
        """
        
        # nodes
        node_0 = AdjacencyListGraphNode(0, None)
        node_1 = AdjacencyListGraphNode(1, None)
        node_2 = AdjacencyListGraphNode(2, None)
        node_3 = AdjacencyListGraphNode(3, None)
        node_4 = AdjacencyListGraphNode(4, None)
        
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
    def sample_3(graph: AdjacencyListGraph):
        """
        Sample Graph 3
        ==============
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list         
        """
        
        # nodes
        node_0 = AdjacencyListGraphNode(0, None)
        node_1 = AdjacencyListGraphNode(1, None)
        node_2 = AdjacencyListGraphNode(2, None)
        node_3 = AdjacencyListGraphNode(3, None)
        node_4 = AdjacencyListGraphNode(4, None)
        node_5 = AdjacencyListGraphNode(5, None)
        node_6 = AdjacencyListGraphNode(6, None)
        
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


class FormulateAdjacencyMatrixGraph:
    """
    Sample Graphs in Adjacency Matrix Format
    ========================================
    Utility functions to arrange nodes in a
        adjancency graph for sample use . 
    """
    @staticmethod
    def sample_1(graph: AdjacencyMatrixGraph):
        """
        Sample Graph 1
        ==============
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list                                                                                                                  
        """
        
        # nodes
        node_0 = AdjacencyMatrixGraphNode(0, None)
        node_1 = AdjacencyMatrixGraphNode(1, None)
        node_2 = AdjacencyMatrixGraphNode(2, None)
        node_3 = AdjacencyMatrixGraphNode(3, None)
        node_4 = AdjacencyMatrixGraphNode(4, None)
        
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
    def sample_2(graph: AdjacencyMatrixGraph):
        """
        Sample Graph 2
        ==============
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list 
        """
        
        # nodes
        node_0 = AdjacencyMatrixGraphNode(0, None)
        node_1 = AdjacencyMatrixGraphNode(1, None)
        node_2 = AdjacencyMatrixGraphNode(2, None)
        node_3 = AdjacencyMatrixGraphNode(3, None)
        node_4 = AdjacencyMatrixGraphNode(4, None)
        
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
    def sample_3(graph: AdjacencyMatrixGraph):
        """
        Sample Graph 3
        ==============
        We are creating a graph :
            - is undirected
            - is connected
            - uses adjancency list
        """
        
        # nodes
        node_0 = AdjacencyMatrixGraphNode(0, None)
        node_1 = AdjacencyMatrixGraphNode(1, None)
        node_2 = AdjacencyMatrixGraphNode(2, None)
        node_3 = AdjacencyMatrixGraphNode(3, None)
        node_4 = AdjacencyMatrixGraphNode(4, None)
        node_5 = AdjacencyMatrixGraphNode(5, None)
        node_6 = AdjacencyMatrixGraphNode(6, None)
        
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
