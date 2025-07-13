import vedo

def visualize_graph(nodes_dict, edges, coords):
    plotter = vedo.Plotter(bg='grey')

    for color in nodes_dict:
        points = [coords[n] for n in nodes_dict[color]]
        plotter += vedo.Points(points, r=10, c=color[0])
    
    lines = [
        [coords[src], coords[dst]]
        for src, dst, _ in edges if src in coords and dst in coords
    ]        
    plotter += vedo.Lines(lines, c='white', alpha=0.6)

    #Create Legend
    colors = [color[0] for color in nodes_dict]
    texts = [(color)[1] for color in nodes_dict]

    x_start = 0.95
    y_start = 0.05
    y_spacing = 0.05
    
    for i, (color, text) in enumerate(zip(colors, texts)):
        text_width = len(text) * 0.01
        x_pos = x_start - text_width
        y_pos = y_start + i * y_spacing
        legend_text = vedo.Text2D(f"{text.capitalize()}", c=color, pos=(x_pos, y_pos), s=1)
        plotter.add(legend_text)

    plotter.show(interactive=True)
