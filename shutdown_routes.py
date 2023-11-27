from loader3 import load_graph_for_bfs
from task4a import kruskals_algorithm, get_all_edges  # Replace with actual file name and function names

def save_shutdown_routes_to_file(shutdown_routes, filename="shutdown_routes.txt"):
    with open(filename, "w") as file:
        for route in shutdown_routes:
            file.write(f"{route[0]},{route[1]}\n")

def main():
    graph, station_to_index, index_to_station = load_graph_for_bfs("London_underground_data.csv")
    spanning_tree = kruskals_algorithm(graph)

    all_edges = get_all_edges(graph)
    spanning_tree_edges = {(u, v) for u, v, _ in spanning_tree}  # Extract just the vertex pairs

    severable_edges = all_edges - spanning_tree_edges

    # Convert edge indices to station names
    shutdown_routes = [(index_to_station[edge[0]], index_to_station[edge[1]]) for edge in severable_edges]

    # Save the shutdown routes to a file
    save_shutdown_routes_to_file(shutdown_routes)

if __name__ == "__main__":
    main()
