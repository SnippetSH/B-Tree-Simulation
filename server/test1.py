import matplotlib.pyplot as plt
import networkx as nx

# Sample data from the C++ program output
nodes_edges = [
    (0, 10, 0), (1, 5, 0), (0, 20, 1), (1, 15, 0), (0, 30, 2), (1, 25, 0), (1, 35, 0)
]

def visualize_b_tree(nodes_edges):
    G = nx.DiGraph()
    pos = {}
    labels = {}

    for depth, key, index in nodes_edges:
        G.add_node((depth, key))
        pos[(depth, key)] = (index, -depth)
        labels[(depth, key)] = str(key)

    for i in range(len(nodes_edges) - 1):
        depth1, key1, index1 = nodes_edges[i]
        depth2, key2, index2 = nodes_edges[i + 1]
        if depth1 < depth2:
            G.add_edge((depth1, key1), (depth2, key2))

    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold", arrows=False)
    plt.show()

visualize_b_tree(nodes_edges)
