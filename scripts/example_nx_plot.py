import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
    ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')]
)

val_map = {
    'A': 1.0,
    'D': 0.5714285714285714,
    'H': 0.0
}
integer_colors = [val_map.get(node, 0.25) for node in G.nodes()]
red_edges = [('A', 'C'), ('E', 'C')]
edge_colours = ['black' if not edge in red_edges else 'red'
                for edge in G.edges()]
black_edges = [edge for edge in G.edges() if edge not in red_edges]
pos = nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color=integer_colors, node_size=500)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True, arrowsize=20)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True, arrowsize=20)
# nx.draw(G)

plt.savefig('outputs/example_nx_plot.png', dpi=300)