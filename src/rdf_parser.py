import rdflib
import random

def parse_rdf(filepath):
    g = rdflib.Graph()
    g.parse(filepath)    
    return g

def generate_random_hex_color():
    """Generate a random hex color"""
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def get_individuals_with_types(graph):
    """Get all individuals with their types"""
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?individual ?type WHERE {
        ?individual a owl:NamedIndividual .
        ?individual rdf:type ?type .
        FILTER(?type != owl:NamedIndividual)
    }
    """
    results = graph.query(query)
    
    individuals = {}
    for row in results:
        individual = str(row['individual'])
        individual_type = str(row['type'])
        individuals[individual] = individual_type
        
    return individuals

def get_relationships_between_individuals(graph):
    """Get relationships between individuals"""
    query = """
    PREFIX owl: <http://www.w3.org/2002/07/owl#>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    
    SELECT ?subject ?predicate ?object WHERE {
        ?subject a owl:NamedIndividual .
        ?object a owl:NamedIndividual .
        ?subject ?predicate ?object .
        FILTER(?predicate != rdf:type)
    }
    """
    results = graph.query(query)
    
    edges = []
    for row in results:
        subject = str(row['subject'])
        predicate = str(row['predicate'])
        obj = str(row['object'])
        edges.append((subject, obj, predicate))
    
    return edges

def extract_nodes_and_edges(graph):
    """Extract individuals as nodes, colored by type"""
    
    # Get all individuals with their types
    individuals = get_individuals_with_types(graph)
    
    # Get relationships between individuals
    edges = get_relationships_between_individuals(graph)
    
    # Create color mapping for each unique type
    unique_types = set(individuals.values())
    type_color_map = {}
    
    for individual_type in unique_types:
        type_color_map[individual_type] = generate_random_hex_color()
    
    # Group nodes by their color (type)
    color_dict = {}
    
    for individual, individual_type in individuals.items():
        color = type_color_map[individual_type]
        color_dict.setdefault((color, individual_type), []).append(individual)
    
    # Print debug information
    print("Individual Type Color Mapping:")
    for individual_type, color in type_color_map.items():
        count = sum(1 for itype in individuals.values() if itype == individual_type)
        print(f"  {individual_type}: {color} ({count} individuals)")
    
    print(f"\nTotal individuals: {len(individuals)}")
    print(f"Total relationships: {len(edges)}")
    
    return color_dict, edges
