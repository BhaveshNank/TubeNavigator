import random
import timeit
from loader import load_graph_from_csv
from dijkstra import dijkstra
from adjacency_list_graph import AdjacencyListGraph

def convert_to_adjacency_list_graph(dictionary_graph):
    stations = list(dictionary_graph.keys())
    station_to_index = {station: index for index, station in enumerate(stations)}
    graph = AdjacencyListGraph(len(stations), weighted=True)

    for start_station, destinations in dictionary_graph.items():
        start_index = station_to_index[start_station]
        for end_station, weight in destinations.items():
            end_index = station_to_index[end_station]
            graph.insert_edge(start_index, end_index, weight)
    
    return graph, station_to_index

def run_test(graph, station_to_index, start_station, end_station):
    start_index = station_to_index[start_station]
    dijkstra_run = lambda: dijkstra(graph, start_index)
    time_taken = timeit.timeit(dijkstra_run, number=1)
    return time_taken

def main():
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    graph, station_to_index = convert_to_adjacency_list_graph(dictionary_graph)
    stations = list(dictionary_graph.keys())
    sizes = [50, 100, 150, 200]  # Adjust this based on your dataset
    test_results = []

    for size in sizes:
        subset_stations = random.sample(stations, min(size, len(stations)))
        start_station, end_station = random.sample(subset_stations, 2)

        duration = run_test(graph, station_to_index, start_station, end_station)
        test_results.append((size, start_station, end_station, duration))

        print(f"Size: {size}, Start: {start_station}, End: {end_station}, Time: {duration:.4f} seconds")

    # Print summary of test results
    for size, start, end, duration in test_results:
        print(f"Test with size {size}: From {start} to {end} took {duration:.4f} seconds.")

if __name__ == "__main__":
    main()
