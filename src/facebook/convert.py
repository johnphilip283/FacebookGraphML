import networkx

g = networkx.read_edgelist("facebook_combined.txt")
networkx.write_adjlist(g, "facebook_combined.adjlist")
