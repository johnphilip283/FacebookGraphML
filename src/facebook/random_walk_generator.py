import networkx as nx
import random


def gen_random_walk(graph: nx.Graph, length, outfile):

    start_node = random.choice(list(graph.nodes))
    walk = [start_node]

    for x in range(length):

        neighbors = list(graph.neighbors(start_node))

        if len(neighbors) == 0:
            break
        else:
            start_node = random.choice(neighbors)
            walk.append(start_node)

    else:
        walk = " ".join(walk) + "\n"
        print(walk)
        outfile.write(walk)


if __name__ == '__main__':

    file = open("random_walk_corpus.txt", "w")

    graph = nx.read_edgelist("facebook_combined.txt")

    for x in range(12000 * 20):
        print("Walk #{}: ".format(x + 1), end="")
        gen_random_walk(graph, 5, file)
