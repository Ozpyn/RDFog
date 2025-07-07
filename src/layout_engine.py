import networkx as nx
import numpy as np

def compute_layout(nodes, edges, method="spring"):
    G = nx.Graph()
    for _, vals in nodes.items():
        for node in vals:
            G.add_node(node)
    for src, dst, _ in edges:
        G.add_edge(src, dst)

    if method == "spring":
        layout_2d = nx.spring_layout(G, dim=3)
    else:
        layout_2d = nx.random_layout(G, dim=3)

    # Convert to dict of (x, y, z)
    coords = {node: layout_2d[node] for _, vals in nodes.items() for node in vals}
    return coords
