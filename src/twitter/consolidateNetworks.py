
if __name__ == '__main__':

    out_file = open("huge_network.txt", "a")

    edges = set()

    for name in ['final_network.txt']:

        file = open(name, 'r')

        for pair in file.readlines():

            print(pair)
            from_node, to_node = pair.split(" ")
            to_node = to_node[:-1]

            if not str(from_node) == 'None':

                edges.add((from_node, to_node))

    for (start, end) in edges:

        out_file.write("{} {}\n".format(start, end))

    out_file.close()
