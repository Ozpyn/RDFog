from rdflib import Graph

def parse_rdf(filepath):
    g = Graph()
    g.parse(filepath)
    return g

def extract_nodes_and_edges(graph):
    nodes = set()
    edges = []
    for subj, pred, obj in graph:
        nodes.update([str(subj), str(obj)])
        edges.append((str(subj), str(obj), str(pred)))
    return list(nodes), edges
