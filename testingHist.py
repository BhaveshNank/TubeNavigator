import matplotlib.pyplot as plt
from loader import load_graph_from_csv
from dijkstra import dijkstra
from adjacency_list_graph import AdjacencyListGraph
from task1 import convert_graph
import copy

def read_shutdown_stations(filename):
    shutdown_stations = []
    with open(filename, 'r') as file:
        for line in file:
            start, end = line.strip().split(',')
            shutdown_stations.append((start, end))
    return shutdown_stations

def modify_graph_for_shutdown(graph, shutdown_stations, station_to_index):
    modified_graph = copy.deepcopy(graph)
    for start_station, end_station in shutdown_stations:
        start_index = station_to_index.get(start_station)
        end_index = station_to_index.get(end_station)
        if start_index is not None and end_index is not None:
            modified_graph.delete_edge(start_index, end_index)
            modified_graph.delete_edge(end_index, start_index)  # If undirected
    return modified_graph

def calculate_journey_time(graph, start_station, end_station, station_to_index):
    start_index = station_to_index[start_station]
    end_index = station_to_index[end_station]
    distances, _ = dijkstra(graph, start_index)
    return distances[end_index]

def main():
    original_data = load_graph_from_csv("London_underground_data.csv")
    graph, station_to_index, index_to_station = convert_graph(original_data)

    start_station = 'Uxbridge'
    end_station = 'Upminster'
    pre_closure_journey_time = calculate_journey_time(graph, start_station, end_station, station_to_index)

    shutdown_stations = read_shutdown_stations('shutdown_routes.txt')
    modified_graph = modify_graph_for_shutdown(graph, shutdown_stations, station_to_index)
    post_closure_journey_time = calculate_journey_time(modified_graph, start_station, end_station, station_to_index)

    # Histograms
    plt.figure(figsize=(10, 6))
    plt.hist([pre_closure_journey_time], bins=20, color='blue', alpha=0.7, label='Pre-Closure')
    plt.hist([post_closure_journey_time], bins=20, color='red', alpha=0.7, label='Post-Closure')
    plt.xlabel('Journey Time')
    plt.ylabel('Frequency')
    plt.title(f'Journey Time from {start_station} to {end_station}')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
