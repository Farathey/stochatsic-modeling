import networkx as nx
import matplotlib.pyplot as plt


class Node():
    '''
    Node class representing node in graph. It stores its "identificator" as a numeric value and its list of neighbours.

    Attributes:
    ----------

    value : int
        Numeric value acting as nodes id.
    '''

    def __init__(self, value: int) -> None:
        self.__value = value
        self.neighbours_list = []

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, new_value) -> None:
        self.__value = new_value


class Graph():
    '''
    Graph class representing undirected graph.

    Attributes:
    ----------

    (optional) nodes_list : list
        List storing Nodes object.

    (optional) edges_list : list
        List storing tuples of connections between different nodes.

    Examples:
    ---------

    1. Creating empty graph

            new_graph = Graph()

    2. Creating graph with given nodes but without specified connections

            nodes = [Node(1), Node(2), Node(3)]\n
            new_graph = Graph(nodes_list = nodes)

        It give us graph with 3 disconnected nodes

    3. Creating graph with given edges and nodes specified by those edges

            edges = [(1, 2), (2, 3), (3, 4)]\n
            new_graph = Graph(edges_list = edges)

        It gives us graph with 4 connected which can be represented nodes as " 1--2--3--4 "
    '''

    def __init__(self, nodes_list: list = None, edges_list: list = None) -> None:
        self.nodes_list = []
        if nodes_list != None:
            self.add_nodes_from(nodes_list)

        self.edges_list = []
        if edges_list != None:
            self.add_edges_from(edges_list)

    def add_node(self, node: Node) -> None:
        '''
        Adds node to the graph.

        Parameters:
        ----------

        node : Node object
            Node which is to be added to graph
        '''
        if isinstance(node, Node):
            if node not in self.nodes_list:
                self.nodes_list.append(node)
        else:
            print("Wrong node type. All nodes should be Node objects.")

    def add_nodes_from(self, new_nodes_list: list) -> None:
        '''
        Adds nodes from the new_nodes_list to the graph.

        Parameters:
        ----------

        new_nodes_list : list
            List of Nodes objects which is to be added to graph.
        '''
        for node in new_nodes_list:
            self.add_node(node)

    def add_edge(self, edge: tuple) -> None:
        '''
        Adds edge to the graph. If any of the nodes specified in edge does't exist it also is added to the graph.

        Parameters:
        ----------

        edge : tuple
            Edge which is to be added to graph.
        '''
        if edge not in self.edges_list:
            self.edges_list.append(edge)

        # adds nodes to the graph if they are not present
        if self.check_node(edge[0]) == False:
            self.add_node(Node(edge[0]))

        if self.check_node(edge[1]) == False:
            self.add_node(Node(edge[1]))

        # adds neighbouring nodes to each others lists if  they are connected by the method
        for node in self.nodes_list:
            if node.value == edge[0] and edge[1] not in node.neighbours_list:
                node.neighbours_list.append(edge[1])

            if node.value == edge[1] and edge[0] not in node.neighbours_list:
                node.neighbours_list.append(edge[0])

    def add_edges_from(self, new_edges_list: list) -> None:
        '''
        Adds edges from the new_edges_list to the graph.

        Parameters:
        ----------

        new_edges_list : list
            List of edges tuples which is to be added to graph.
        '''
        for edge in new_edges_list:
            self.add_edge(edge)

    def print_graph(self) -> None:
        '''
        Prints out the nodes of the graph with the list of each nodes' neighbours in the format "node -> list of neighbours".
        '''
        for node in self.nodes_list:
            print(f'{node.value} -> {node.neighbours_list}')

    def draw_graph(self) -> None:
        "Draws the graph using networkx and matplotlib.pyplot libraries."
        G = nx.Graph(self.edges_list)
        nx.draw_networkx(G)
        plt.show()

    def check_node(self, value: int) -> bool:
        '''
        Checks if the node with given value is present in the graph. If it is function returns True else it returns False.

        Parameters:
        ----------

        value : int
            Value of the node which is to be found in graph. 
        '''
        for node in self.nodes_list:
            if node.value == value:
                return True

        return False

    def find_node(self, value: int) -> Node:
        '''
        Finds the node with given value is present in the graph and returns it. If it wasn't found returns None.

        Parameters:
        ----------

        value : int
            Value of the node which is to be found in graph. 
        '''
        for node in self.nodes_list:
            if node.value == value:
                return node

        return None


if __name__ == "__main__":
    test_edges = [(1, 2), (2, 3), (3, 4)]
    test_graph = Graph(edges_list=test_edges)
    for node in test_graph.nodes_list:
        assert node.value == 1 or node.value == 2 or node.value == 3 or node.value == 4

    assert test_graph.edges_list == [(1, 2), (2, 3), (3, 4)]

    test_graph.add_node(Node(5))
    for node in test_graph.nodes_list:
        assert node.value == 1 or node.value == 2 or node.value == 3 or node.value == 4 or node.value == 5

    test_graph.add_edge((2, 5))
    assert test_graph.edges_list == [(1, 2), (2, 3), (3, 4), (2, 5)]
