from src.rdf_parser import parse_rdf, extract_nodes_and_edges
from src.layout_engine import compute_layout
from src.visualizer import visualize_graph

rdf_path = "data/example.owl"
graph = parse_rdf(rdf_path)
nodes, edges = extract_nodes_and_edges(graph)
coords = compute_layout(nodes, edges)
visualize_graph(nodes, edges, coords)
