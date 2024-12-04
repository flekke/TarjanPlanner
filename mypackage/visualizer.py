import networkx as nx  
import matplotlib.pyplot as plt  
from .shortest_path import relatives

def draw_graph():

    G = nx.DiGraph()

    for name, (lat, lon) in relatives.items():
        G.add_node(name, pos=(lon, lat)) 

    for loc1 in relatives:
        for loc2 in relatives:
            if loc1 != loc2:
                G.add_edge(loc1, loc2)

    path = ['R8', 'R5', 'R3', 'R7', 'R4', 'R9', 'R1', 'R2', 'R10', 'R6']
    edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]

    pos = nx.get_node_attributes(G, 'pos')

    plt.figure(figsize=(12, 8))
    plt.gca().set_facecolor("#f0f0f5")

    nx.draw(
        G, 
        pos, 
        with_labels=False, 
        node_size=300, 
        node_color="lightgray", 
        edge_color="gray", 
        alpha=0.4
    )

    path_node_colors = ["#FF7F0E" if node in path else "lightgray" for node in G.nodes()]
    path_node_sizes = [600 if node in path else 300 for node in G.nodes()]

    nx.draw_networkx_nodes(G, pos, node_color=path_node_colors, node_size=path_node_sizes)

    nx.draw_networkx_edges(
        G, 
        pos, 
        edgelist=edges_in_path, 
        edge_color="#1f77b4", 
        width=3, 
        arrowstyle="-|>", 
        arrowsize=20
    )

    nx.draw_networkx_labels(
        G, 
        pos, 
        labels={node: node for node in G.nodes()}, 
        font_size=10, 
        font_color="black", 
        font_weight="bold"
    )

    plt.title("Shortest path", fontsize=16, fontweight="bold", color="#333333")
    plt.show()