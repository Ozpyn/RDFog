import time
from src.rdf_parser import parse_rdf, extract_nodes_and_edges
from src.layout_engine import compute_layout
from src.visualizer import visualize_graph

# Timing decorator
def timeit(label):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{label}] Starting...")
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            duration = end - start
            print(f"[{label}] Completed in {duration:.4f} seconds")
            return result
        return wrapper
    return decorator

# Wrapped functions with time tracking
@timeit("RDF Parsing")
def timed_parse_rdf(path):
    return parse_rdf(path)

@timeit("Node/Edge Extraction")
def timed_extract_nodes_and_edges(graph):
    return extract_nodes_and_edges(graph)

@timeit("Layout Computation")
def timed_compute_layout(nodes, edges):
    return compute_layout(nodes, edges)

@timeit("Graph Visualization")
def timed_visualize_graph(nodes, edges, coords):
    return visualize_graph(nodes, edges, coords)

# Main execution
if __name__ == "__main__":
    rdf_path = "data/example.owl"
    graph = timed_parse_rdf(rdf_path)
    nodes, edges = timed_extract_nodes_and_edges(graph)
    coords = timed_compute_layout(nodes, edges)
    timed_visualize_graph(nodes, edges, coords)
