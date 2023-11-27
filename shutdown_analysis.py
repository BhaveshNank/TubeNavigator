# File: modify_graph_for_shutdown.py

import copy
from loader import load_graph_from_csv
from adjacency_list_graph import AdjacencyListGraph
from dijkstra import dijkstra
from task1 import convert_graph


def read_shutdown_routes(filename="shutdown_routes.txt"):
    shutdown_routes = []
    with open(filename, "r") as file:
        for line in file:
            start_station, end_station = line.strip().split(',')
            shutdown_routes.append((start_station, end_station))
    return shutdown_routes


def modify_graph_for_shutdown(graph, shutdown_routes, station_to_index):
    modified_graph = copy.deepcopy(graph)  # Create a deep copy of the graph

    for start_station, end_station in shutdown_routes:
        start_index = station_to_index.get(start_station)
        end_index = station_to_index.get(end_station)

        if start_index is not None and end_index is not None:
            # Use the correct method name to remove the edge
            modified_graph.delete_edge(start_index, end_index)

    return modified_graph



def main():
    # Load the original graph and convert it
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    graph, station_to_index, index_to_station = convert_graph(dictionary_graph)
    
    # Read shutdown routes from the file
    shutdown_routes = read_shutdown_routes()

    # Modify the graph based on shutdown routes
    modified_graph = modify_graph_for_shutdown(graph, shutdown_routes, station_to_index)

    # Generate and display the histogram for the modified graph
    # (You can use the same logic as in your previous histogram script)

if __name__ == "__main__":
    main()

