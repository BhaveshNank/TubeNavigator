from loader import load_graph_from_csv
from dijkstra import dijkstra
from adjacency_list_graph import AdjacencyListGraph

def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

def convert_graph(dictionary_graph):
    stations = list(dictionary_graph.keys())
    station_to_index = {station: index for index, station in enumerate(stations)}
    index_to_station = {index: station for station, index in station_to_index.items()}

    graph = AdjacencyListGraph(len(stations), weighted=True)

    for start_station, destinations in dictionary_graph.items():
        u = station_to_index[start_station]
        for end_station in destinations.keys():
            v = station_to_index[end_station]
            graph.insert_edge(u, v, 1)  # Each edge has a weight of 1

    return graph, station_to_index, index_to_station

def main():
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    graph, station_to_index, index_to_station = convert_graph(dictionary_graph)

    start_station, destination_station = get_user_input()

    start_index = station_to_index.get(start_station)
    destination_index = station_to_index.get(destination_station)

    if start_index is None or destination_index is None:
        print("One or more of the stations entered do not exist in the network.")
        return

    distances, predecessors = dijkstra(graph, start_index)

    # Check if a path exists to the destination
    if distances[destination_index] == float('infinity'):
        print(f"No path found from {start_station} to {destination_station}.")
    else:
        # Reconstruct the path from start_station to destination_station
        path = []
        current = destination_index
        while current != None:
            path.insert(0, index_to_station[current])
            current = predecessors[current]

        # Display the path and total number of stations
        print("Path from {} to {}:".format(start_station, destination_station))
        for station in path:
            print(station)
        print("Total number of stations: {}".format(distances[destination_index]))

if __name__ == "__main__":
    main()
