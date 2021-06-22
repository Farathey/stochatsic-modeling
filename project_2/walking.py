from random import random
import scipy.stats as stats
import numpy as np
from graphing import Graph, Node


def random_walk(graph: Graph, current_node: Node) -> Node:
    '''
    Returns randomly selceted from graph node connected to node passed as parameter. Each neighbouring node has equal probability to be selected.

    Parameters:
    -----------

    graph : Graph object
        Graph we are walking through.

    current_node : Node object
        Node we are starting from. It can be passed as already specified object or using Graph method find_node(). 
    '''
    # Here we create probability list for each neighbouring node with each value being multiple of unit value so each neighbouring node has identical chance of being selected
    # We use it as a distribution of probabilities
    probability = [1/len(current_node.neighbours_list) *
                   i for i in range(1, len(current_node.neighbours_list)+1)]
    random_value = random()

    for i in range(len(probability)):
        # Here we handle what happens if our random value is smaller than the first value in probability list -> we return first node in our neighbours list
        if random_value >= 0 and random_value < probability[0]:
            return graph.find_node(current_node.neighbours_list[0])

        # Here we handle what happens if our random value is greater than penultimate value and smaller or equal to 1 -> we return last node in our neighbours list
        elif random_value > probability[-2] and random_value <= 1:
            return graph.find_node(current_node.neighbours_list[-1])

        # Here we handle other possibilities
        elif random_value >= probability[i] and random_value < probability[i+1]:
            return graph.find_node(current_node.neighbours_list[i+1])


def metropolis_walk(graph: Graph, current_node: Node, function_list: list, steps_num: int) -> list:
    '''
    Function which walks through the graph using Metropolis method. Returns a list with values indicating visited nodes.

    Parameters:
    ----------

    graph : Graph object
        Graph we are walking through.

    current_node : Node object
        Node we are starting from. It can be passed as already specified object or using Graph method find_node(). 

    function_list : list
        List of values created by the function f(i) = π(i)/π_rw(i).

    steps_num : int
        Number of steps we want to take.
    '''
    T = steps_num
    t = 0
    values = np.zeros(T)
    values[0] = current_node.value
    nodes = [current_node]

    # modified loop from exercises
    while t < T-1:
        t += 1
        # Generate a candidate
        new_node = random_walk(graph, nodes[t-1])

        # Calculate the acceptance ratio
        alpha = min(1, function_list[(new_node.value)-1] /
                    function_list[(nodes[t-1].value)-1])

        # Accept or reject
        u = stats.uniform.rvs(0, 1)
        if u <= alpha:
            values[t] = new_node.value
            nodes.append(new_node)

        else:
            values[t] = values[t-1]
            nodes.append(nodes[t-1])

    return values


if __name__ == '__main__':
    test_edges = [(1, 2), (2, 3)]
    test_graph = Graph(edges_list=test_edges)

    test_node1 = test_graph.find_node(1)
    test_node2 = test_graph.find_node(2)
    test_node3 = test_graph.find_node(3)
    test_1 = random_walk(test_graph, test_node2)
    assert (test_1 == test_node1) or (test_1 == test_node3)
    test_f = [1, 1, 1]
    test_steps = 10
    new_test_list = metropolis_walk(test_graph, test_node2, test_f, test_steps)
    for i in range(test_steps):
        test = new_test_list[i]
        assert test == 1 or test == 2 or test == 3
