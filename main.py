import time
import sys
from src.rdf_parser import parse_rdf, extract_nodes_and_edges
from src.layout_engine import compute_layout
from src.visualizer import visualize_graph
from src.federated_query import get_federated_triples, triples_to_graph

# Utility: get size in KB/MB
def format_size(obj):
    size = sys.getsizeof(obj)
    if size < 1024:
        return f"{size} B"
    elif size < 1024 ** 2:
        return f"{size / 1024:.1f} KB"
    else:
        return f"{size / (1024 ** 2):.1f} MB"

# Timing decorator with extra metrics
def timeit(label):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"\n[{label}] Starting...")
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start

            print(f"[{label}] Completed in {duration:.4f} seconds")
            print(f"[{label}] Approx. memory: {format_size(result)}")
            return result
        return wrapper
    return decorator

# Wrapped functions
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

# Main pipeline
if __name__ == "__main__":
    # Option 1: Use federated data
    triples = get_federated_triples()
    graph = triples_to_graph(triples)

    # Option 2: Use local file (keep for fallback/testing)
    # rdf_path = "data/example.owl"
    # graph = timed_parse_rdf(rdf_path)

    nodes, edges = timed_extract_nodes_and_edges(graph)
    coords = timed_compute_layout(nodes, edges)
    timed_visualize_graph(nodes, edges, coords)
