from vedo import Plotter, Points, Lines

def visualize_graph(nodes, edges, coords):
    plotter = Plotter(bg='black')

    points = Points([coords[n] for n in nodes], r=10, c='cyan')
    plotter += points

    line_segments = []
    for src, dst, _ in edges:
        if src in coords and dst in coords:
            line_segments.append([coords[src], coords[dst]])
    lines = Lines(line_segments, c='white', alpha=0.6)
    plotter += lines

    plotter.show(interactive=True)
