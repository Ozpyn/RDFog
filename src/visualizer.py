import vedo

def visualize_graph(nodes_dict, edges, coords):
    plotter = vedo.Plotter(bg='grey')

    print(nodes_dict)

    for color in nodes_dict:
        points = [coords[n] for n in nodes_dict[color]]
        plotter += vedo.Points(points, r=10, c=color)
    
    lines = [
        [coords[src], coords[dst]]
        for src, dst, _ in edges if src in coords and dst in coords
    ]        
    plotter += vedo.Lines(lines, c='white', alpha=0.6)

    plotter.show(interactive=True)
