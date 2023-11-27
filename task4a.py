# Import necessary module
from loader3 import load_graph_for_bfs # Import a function to load a graph for BFS

# Function to get all edges in the graph
def get_all_edges(graph):
    edges = set()
    for u in range(graph.get_card_V()):
        for edge in graph.get_adj_list(u):
            v = edge.get_v()
            # Ensure each edge is added once (for undirected graphs)
            if (v, u) not in edges:
                edges.add((u, v))
    return edges

# Kruskal's Algorithm to find the Minimum Spanning Tree
def kruskals_algorithm(graph):
    edges = []
    for u in range(graph.get_card_V()):
        for edge in graph.get_adj_list(u):
            v = edge.get_v()
            edges.append((u, v, 1))  # Use a default weight of 1

    edges = sorted(edges, key=lambda edge: edge[2])

    forests = {vertex: {vertex} for vertex in range(graph.get_card_V())}

    spanning_tree = set()
    for edge in edges:
        u, v, _ = edge
        if forests[u] != forests[v]:
            spanning_tree.add(edge)
            merged_forest = forests[u].union(forests[v])
            for vertex in merged_forest:
                forests[vertex] = merged_forest

    return spanning_tree

# Load the graph data for BFS from a CSV file
graph, station_to_index, index_to_station = load_graph_for_bfs("London_underground_data.csv")
# Assuming 'graph' is your tube network graph
# Assuming graph is your AdjacencyListGraph instance
spanning_tree = kruskals_algorithm(graph)

all_edges = get_all_edges(graph)
spanning_tree_edges = {(u, v) for u, v, _ in spanning_tree}  # Extract just the vertex pairs

severable_edges = all_edges - spanning_tree_edges

# Print edges that can be severed to disconnect the network
for edge in severable_edges:
    print(f"{index_to_station[edge[0]]} -- {index_to_station[edge[1]]}")