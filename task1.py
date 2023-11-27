# Import necessary modules
from loader import load_graph_from_csv # Import a function to load a graph from a CSV file
from dijkstra import dijkstra # Import Dijkstra's algorithm implementation
from adjacency_list_graph import AdjacencyListGraph  # Import a custom graph implementation
import time # Import the time module for measuring execution time

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
    
    # Create an adjacency list graph and populate it with edges and weights
    graph = AdjacencyListGraph(len(stations), weighted=True)

    for start_station, destinations in dictionary_graph.items():
        u = station_to_index[start_station]
        for end_station, duration in destinations.items():
            v = station_to_index[end_station]
            graph.insert_edge(u, v, duration)  # Use actual duration as weight

    return graph, station_to_index, index_to_station

# Main function to run the program
def main():
    # Load the graph data from a CSV file
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    # Convert the loaded dictionary-based graph to an adjacency list graph
    graph, station_to_index, index_to_station = convert_graph(dictionary_graph)
    # Get user input for start and destination stations
    
    start_station, destination_station = get_user_input()
   
    # Get the indices of start and destination stations in the grap
    start_index = station_to_index.get(start_station)
    destination_index = station_to_index.get(destination_station)

    if start_index is None or destination_index is None:
        print("One or more of the stations entered do not exist in the network.")
        return

    # start = time.time()

    distances, predecessors = dijkstra(graph, start_index)

    # end = time.time()

    if distances[destination_index] == float('infinity'):
        print(f"No path found from {start_station} to {destination_station}.")
    else:
        path = []
        current = destination_index
        total_duration = 0
        while current != None:
            path.insert(0, index_to_station[current])
            prev = predecessors[current]
            if prev != None:
                # Use the original graph dictionary to get the duration
                total_duration += dictionary_graph[index_to_station[prev]][index_to_station[current]]
            current = prev

        print("Path from {} to {}:".format(start_station, destination_station))
        for station in path:
            print(station)
        print("Total journey time: {} minutes".format(total_duration))

    # total_time = end - start
    # print(total_time)
    
if __name__ == "__main__":
    main()
