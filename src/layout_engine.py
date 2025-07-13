import networkx as nx
import numpy as np
import random

def compute_layout(nodes, edges, method="spring"):
    G1 = nx.Graph()
    G2 = nx.Graph()
    
    # Assign nodes randomly to G1 or G2
    for _, vals in nodes.items():
        for node in vals:
            if random.random() < 0.5:
                G1.add_node(node)
            else:
                G2.add_node(node)

    # Create a combined graph
    G_combined = nx.Graph()
    G_combined.add_nodes_from(G1.nodes(data=True))
    G_combined.add_nodes_from(G2.nodes(data=True))
    for src, dst, _ in edges:
        G_combined.add_edge(src, dst)

    pos = {}
    if method == "spring":
        layout_3d_1 = nx.spring_layout(G1, dim=3, center=(-1, 0, 0))
        layout_3d_2 = nx.spring_layout(G2, dim=3, center=(1, 0, 0))
        pos.update(layout_3d_1)
        pos.update(layout_3d_2)
    else:
        layout_3d_1 = nx.random_layout(G1, dim=3, center=(-3, 0, 0))
        layout_3d_2 = nx.random_layout(G2, dim=3, center=(3, 0, 0))
        pos.update(layout_3d_1)
        pos.update(layout_3d_2)

    # Safely gather coordinates from combined graph
    coords = {node: pos[node] for node in G_combined.nodes if node in pos}
    return coords
