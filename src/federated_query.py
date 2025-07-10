from SPARQLWrapper import SPARQLWrapper, JSON
from rdflib import Graph, URIRef, Literal

def get_triples_from_endpoint(endpoint_url):
    print(f"Querying endpoint: {endpoint_url}")
    try:
        sparql = SPARQLWrapper(endpoint_url)
        sparql.setQuery("""
            SELECT ?s ?p ?o WHERE { ?s ?p ?o }
        """)
        sparql.setReturnFormat(JSON)
        
        results = sparql.query().convert()
        
        triples = []
        if "results" in results and "bindings" in results["results"]:
            for result in results["results"]["bindings"]:
                s = result["s"]["value"]
                p = result["p"]["value"]
                o = result["o"]["value"]
                triples.append((s, p, o))
        
        print(f"Extracted {len(triples)} triples from {endpoint_url}")
        return triples
        
    except Exception as e:
        print(f"Error querying {endpoint_url}: {e}")
        import traceback
        traceback.print_exc()
        return []

def get_federated_triples():
    endpoints = [
        "http://localhost:3030/ds/sparql",
        "http://localhost:3031/ds/sparql"
    ]
    all_triples = []
    for endpoint in endpoints:
        triples = get_triples_from_endpoint(endpoint)
        all_triples.extend(triples)
    
    print(f"Total triples from all endpoints: {len(all_triples)}")
    return all_triples

def triples_to_graph(triples):
    g = Graph()
    for s, p, o in triples:
        # Handle URIs and literals properly
        if isinstance(s, str) and s.startswith("http"):
            s_node = URIRef(s)
        else:
            s_node = Literal(s)
        
        if isinstance(p, str) and p.startswith("http"):
            p_node = URIRef(p)
        else:
            p_node = Literal(p)
            
        if isinstance(o, str) and o.startswith("http"):
            o_node = URIRef(o)
        else:
            o_node = Literal(o)
            
        g.add((s_node, p_node, o_node))
    return g