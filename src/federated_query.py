from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef

def get_triples_from_endpoint(endpoint_url):
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery("""
        SELECT ?s ?p ?o WHERE { ?s ?p ?o }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    triples = []
    for result in results["results"]["bindings"]:
        s = result["s"]["value"]
        p = result["p"]["value"]
        o = result["o"]["value"]
        triples.append((s, p, o))
    return triples

def get_federated_triples():
    endpoints = [
        "http://localhost:3030/ds/sparql",
        "http://localhost:3031/ds/sparql"
    ]
    all_triples = []
    for endpoint in endpoints:
        all_triples.extend(get_triples_from_endpoint(endpoint))
    return all_triples

def triples_to_graph(triples):
    g = Graph()
    for s, p, o in triples:
        g.add((URIRef(s), URIRef(p), URIRef(o)))
    return g