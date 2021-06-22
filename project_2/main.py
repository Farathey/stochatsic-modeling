'''
TODO:
    -> code review
    -> description
'''
import numpy as np
import matplotlib.pyplot as plt
from random import choices
from graphing import Graph
from walking import random_walk, metropolis_walk

# list of connections between nodes
edges = [(1, 2), (2, 3), (3, 4), (3, 5), (2, 6),
         (1, 7), (3, 6), (3, 7), (4, 7)]

# Here we generate our graph and show it
graph = Graph(edges_list=edges)
graph.draw_graph()

# stationary distribution of our graph
pi = [1/20, 2/20, 8/20, 2/20, 2/20, 2/20, 3/20]

# distribution we want to achive
pi_rw = [2/20, 3/20, 5/20, 2/20, 1/20, 3/20, 4/20]

# function f(i) = π(i)/π_rw(i)
f = []
for i in range(len(pi)):
    f.append(pi[i]/pi_rw[i])

# Here we select randomly starting node from our graph - using random.choices() gives us same probability for all nodes to be chosen
starting_node = choices(graph.nodes_list)

# Two copies for safty reasons = we don't want to overwrite startng positions for boths walks so they can start from the same position
current_node = starting_node[0]
current_node_copy = starting_node[0]

# print(f'starting node: {current_node.value}')

# Here we do our classical random walk to show that our stationary distribution is just right
random_walk_values = [current_node.value]
for i in range(5000):
    current_node = random_walk(graph, current_node)
    random_walk_values.append(current_node.value)

# Auxilary list to show our stationary distribution
pi_rw_plot = [None]
for i in pi_rw:
    pi_rw_plot.append(i)

# Here we plot both stationary distribution and density histogram of our classic random walk
fig, (ax0, ax1) = plt.subplots(2)
l0 = ax0.plot(pi_rw_plot, color="#1a8ee9")[0]
hist0 = ax0.hist(random_walk_values, bins=np.arange(1, 9)-0.5, density=True,
                 color="#F5D09F", edgecolor="#A89276", linewidth=2)[2]

# Here we do our random walk with Metropolis method to achive our given distribution
values = metropolis_walk(graph, current_node_copy, f, 5000)

# Auxilary list to show our new stationary distribution
pi_plot = [None]
for i in pi:
    pi_plot.append(i)

# Here we plot both stationary distribution and density histogram of our Metropolis method random walk
l1 = ax1.plot(pi_plot, color="#f91718")[0]
hist1 = ax1.hist(values, bins=np.arange(1, 9)-0.5, density=True, color="#4f9ced",
                 edgecolor="#94c2f3", linewidth=2)[2]
ax1.annotate('text', (0.5, 0.25))

# Here we set cosmetics such as legend, titles, and adjustements
labels = ['Π_rw distribution', 'random walk density histogram',
          'Π distribution', 'metropolis method random walk density histogram']
fig.legend([l0, hist0, l1, hist1], labels,
           loc="center right", borderaxespad=8)
ax0.set_title(
    'Comparison of the probability density distribution obtained in the random walk with given distribution Π_rw')
ax0.set_ylim(0, 0.5)

ax1.set_title(
    'Comparison of the probability density distribution obtained in the Metropolis walk with predicted distribution Π')
ax1.set_ylim(0, 0.5)
plt.subplots_adjust(right=0.65)
plt.show()

# And here are the steps taken in our random walk
fig, ax = plt.subplots(1, 1)
ax = plt.step(range(0, 5001), random_walk_values)
plt.title("Random walk")
plt.show()

# And here are the steps taken in our Metropolis walk
fig, ax = plt.subplots(1, 1)
ax = plt.step(range(0, 5000), values)
plt.title("Metropolis method random walk")
plt.show()
