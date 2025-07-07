import rdflib

def get_classes(graph):
    query = "SELECT ?class WHERE {?class a owl:Class .}"
    results = graph.query(query)
    return [str(row['class']) for row in results]

def get_objects(graph):
    query = "SELECT ?object WHERE {?object a owl:ObjectProperty .}"
    results = graph.query(query)
    return [str(row['object']) for row in results]

def get_data(graph):
    query = "SELECT ?data WHERE {?data a owl:DatatypeProperty .}"
    results = graph.query(query)
    return [str(row['data']) for row in results]



def get_instances(graph, class_type):
    query = "SELECT ?instance WHERE {?instance a <" + class_type + "> .}"
    results = graph.query(query)
    return [str(row['instance']) for row in results]

def get_query_objects(graph, type):
    query = "SELECT ?subject ?object WHERE {?subject " + type + " ?object .}"
    results = graph.query(query)
    return [str(row['object']) for row in results]

def parse_rdf(filepath):
    g = rdflib.Graph()
    g.parse(filepath)    
    return g

def extract_nodes_and_edges(graph):
    nodes = set()
    edges = []
    for subj, pred, obj in graph:
        nodes.update([str(subj), str(obj)])
        edges.append((str(subj), str(obj), str(pred)))

    # SPARQL queries
    class_query = get_classes(graph)
    object_type_query = get_objects(graph)
    data_type_query = get_data(graph)

    classes = {c: get_instances(graph, c) for c in class_query}
    #print(classes)
    data = {d: get_query_objects(graph, d) for d in data_type_query}

    
    color_list = [
        "Blue", "Pink", "Cyan", "Yellow", "Magenta", "Orange", "Purple",
        "Aqua", "Lime", "Teal", "Navy", "Olive", "Black", "Brown", "Coral",
        "Gold", "Silver", "Maroon", "Turquoise", "Violet"
    ]
    class_color_map = {}
    color_dict = {}

    # Assign a unique color to each class key
    for idx, key in enumerate(classes.keys()):
        color = color_list[idx % len(color_list)]
        class_color_map[key] = color

    for node in nodes:
        if node in classes:
            color = class_color_map.get(node, "Brown")
            color_dict.setdefault(color, []).append(node)
        elif any(node in sublist for sublist in classes.values()):
            for key, value in classes.items():
                if node in value:
                    color = class_color_map.get(key, "Brown")
                    color_dict.setdefault(color, []).append(node)
        elif node in data or any(node in sublist for sublist in data.values()):
            color_dict.setdefault("Green", []).append(node)
        elif node in object_type_query:
            color_dict.setdefault("Red", []).append(node)
        else:
            if "xsd:" in node:
                color_dict.setdefault("Light Grey", []).append(node)
            else:
                color_dict.setdefault("Dark Grey", []).append(node)
 
    return color_dict, edges
