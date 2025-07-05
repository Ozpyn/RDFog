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

    
    color_dict = {}
    for node in nodes:
        if node in classes:
            color_dict.setdefault("Blue", []).append(node)
        elif any(node in sublist for sublist in classes.values()):
            for key, value in classes.items():
                if node in value:
                    match(key):
                        case 'ex:Device':
                            color_dict.setdefault("Pink", []).append(node)
                        case 'ex:Sensor':
                            color_dict.setdefault("Cyan", []).append(node)
                        case 'ex:SensorType':
                            color_dict.setdefault("Yellow", []).append(node)
                        case 'ex:Server':
                            color_dict.setdefault("Magenta", []).append(node)
                        case 'ex:Network':
                            color_dict.setdefault("Orange", []).append(node)
                        case 'ex:Location':
                            color_dict.setdefault("Purple", []).append(node)
                        case 'ex:Application':
                            color_dict.setdefault("Aqua", []).append(node)
                        case 'ex:User':
                            color_dict.setdefault("Lime", []).append(node)
                        case 'ex:OperatingSystem':
                            color_dict.setdefault("Teal", []).append(node)
                        case 'ex:Alert':
                            color_dict.setdefault("Navy", []).append(node)
                        case 'ex:CriticalAlert':
                            color_dict.setdefault("Olive", []).append(node)
                        case 'ex:MobileDevice':
                            color_dict.setdefault("Black", []).append(node)
                        case _:
                            color_dict.setdefault("Brown", []).append(node)
                            
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
