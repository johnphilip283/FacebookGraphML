import networkx as nx
import matplotlib.pyplot as plt
import random
import scipy

file = open('twitter_combined.txt', 'r')
g = nx.DiGraph()
lines = file.readlines()
random.shuffle(lines)
lines = lines[:2000]

plt.figure(figsize=(15, 13))
for idx, line in enumerate(lines):

    print('Working on line [{0} / {1}]'.format(idx + 1, len(lines)))
    from_node, to_node = line.split(' ')
    g.add_edge(from_node, to_node)

nx.draw(g)
plt.show()
