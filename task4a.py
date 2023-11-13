from loader3 import load_graph_for_bfs

def kruskals_algorithm(graph):
    # Sort edges based on weight
    edges = sorted(graph.edges, key=lambda edge: edge.weight)

    spanning_tree = set()
    forests = {vertex: {vertex} for vertex in graph.vertices}

    for edge in edges:
        u, v = edge.vertices
        if forests[u] != forests[v]:  # If u and v are in different trees
            spanning_tree.add(edge)
            # Merge the two trees
            merged_forest = forests[u].union(forests[v])
            for vertex in merged_forest:
                forests[vertex] = merged_forest

    return spanning_tree

graph = load_graph_for_bfs("London_underground_data.csv") 
# Assuming 'graph' is your tube network graph
spanning_tree = kruskals_algorithm(graph)
severable_edges = set(graph.edges) - spanning_tree

for edge in severable_edges:
    print(f"{edge.start} -- {edge.end}")
