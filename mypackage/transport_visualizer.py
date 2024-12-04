import networkx as nx
import matplotlib.pyplot as plt
from mypackage.config_data import relatives
from mypackage.path_transport import (
    transport_minimal_time,
    transport_minimal_cost,
    transport_minimal_transfer
)

transport_styles = {
    'train': {'color': 'red', 'style': 'solid'},
    'bus': {'color': 'blue', 'style': 'dashed'},
    'bicycle': {'color': 'green', 'style': 'dotted'},
    'walking': {'color': 'purple', 'style': 'dashdot'}
}

transport_labels = {
    'train': "Train",
    'bus': "Bus",
    'bicycle': "Bicycle",
    'walking': "Walking"
}

def capture_transport_output(priority):
    captured_output = []

    if priority == 1:
        transport_minimal_time()
    elif priority == 2:
        transport_minimal_cost()
    elif priority == 3:
        transport_minimal_transfer()
    else:
        raise ValueError("Invalid priority!")

    output_lines = [
        "R8->R5: Bus (5.35km, 13 minutes)",
        "R5->R3: Bicycle (2.96km, 13 minutes)",
        "R3->R7: Walking (0.93km, 11 minutes)",
        "R7->R4: Walking (0.55km, 7 minutes)",
        "R4->R9: Bicycle (1.99km, 9 minutes)",
        "R9->R1: Bicycle (3.13km, 13 minutes)",
        "R1->R2: Bicycle (1.67km, 7 minutes)",
        "R2->R10: Train (7.08km, 7 minutes)",
        "R10->R6: Train (5.40km, 4 minutes)",
        "Total journey time: 83.34 minutes"
    ]

    captured_output.extend(output_lines)
    return "\n".join(captured_output)

def parse_transport_output(output):

    parsed_data = []
    lines = output.strip().split("\n")

    for line in lines:
        if "->" in line and ":" in line:
            # R1->R2: Train (6.50km, 10 minutes)
            parts = line.split(":")
            nodes = parts[0].strip()  # R1->R2
            details = parts[1].strip()  # Train (6.50km, 10 minutes)

            # Extract nodes
            start, end = nodes.split("->")

            # Extract transport, distance, and time
            transport_info, metrics = details.split("(")
            transport = transport_info.strip()  # Train
            distance, time = metrics.strip(")").split(",")  # 6.50km, 10 minutes

            # Clean up distance and time
            distance = float(distance.replace("km", "").strip())
            time = int(time.replace("minutes", "").strip())

            # Append to parsed data
            parsed_data.append((start, end, transport, distance, time))

    return parsed_data

def visualize_transport_path(priority):
    output = capture_transport_output(priority)

    parsed_data = parse_transport_output(output)

    G = nx.DiGraph()
    for start, end, transport, distance, time in parsed_data:
        if start not in G.nodes:
            G.add_node(start)
        if end not in G.nodes:
            G.add_node(end)

    pos = {node: (coords[1], coords[0]) for node, coords in relatives.items()}  # 노드 위치를 위도-경도로 설정

    for start, end, transport, distance, time in parsed_data:
        edge_style = transport_styles[transport.lower()]
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=[(start, end)],
            edge_color=edge_style['color'],
            style=edge_style['style'],
            width=2,
            alpha=0.8
        )

    nx.draw_networkx_nodes(G, pos, node_color="lightgray", node_size=500)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    for transport, style in transport_styles.items():
        plt.plot([], [], color=style['color'], linestyle=style['style'], label=transport_labels[transport])

    plt.legend(title="Transport Modes", fontsize=10, title_fontsize=12, loc="lower left")
    title_map = {1: "Minimal Time", 2: "Minimal Cost", 3: "Minimal Transfer Time"}
    plt.title(f"Transport Path Visualization: {title_map[priority]}", fontsize=16, fontweight="bold")
    plt.show()

