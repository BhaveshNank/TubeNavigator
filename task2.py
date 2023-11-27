# Import necessary modules
from loader import load_graph_from_csv # Import a function to load a graph from a CSV file
from dijkstra import dijkstra # Import Dijkstra's algorithm implementation
from adjacency_list_graph import AdjacencyListGraph # Import a custom graph implementation

# Function to get user input for start and destination stations
def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

# Function to convert a dictionary-based graph to an adjacency list graph
def convert_graph(dictionary_graph):
    stations = list(dictionary_graph.keys())
    station_to_index = {station: index for index, station in enumerate(stations)}
    index_to_station = {index: station for station, index in station_to_index.items()}
    
# Create an adjacency list graph and populate it with edges (weight of 1 for all edges)
    graph = AdjacencyListGraph(len(stations), weighted=True)

    for start_station, destinations in dictionary_graph.items():
        u = station_to_index[start_station]
        for end_station in destinations.keys():
            v = station_to_index[end_station]
            graph.insert_edge(u, v, 1)  # Each edge has a weight of 1

    return graph, station_to_index, index_to_station

# Main function to run the program
def main():
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    graph, station_to_index, index_to_station = convert_graph(dictionary_graph)

    start_station, destination_station = get_user_input()

    start_index = station_to_index.get(start_station)
    destination_index = station_to_index.get(destination_station)

 # Check if the entered stations exist in the network
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

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
