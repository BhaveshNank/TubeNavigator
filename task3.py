from bfs import bfs  # Replace 'bfs_library' with the actual name of the BFS library file
from loader3 import load_graph_from_csv
from task1 import get_user_input



def main():
    graph = load_graph_from_csv("London_underground_data.csv")
    start_station, destination_station = get_user_input()

    # Assuming that your graph uses indices, convert station names to indices
    start_index = graph.get_index_of_station(start_station)
    destination_index = graph.get_index_of_station(destination_station)

    if start_index is None or destination_index is None:
        print("One or more of the stations entered do not exist in the network.")
        return

    # Perform BFS
    distances, predecessors = bfs(graph, start_index)

    # Get the distance for the destination station
    distance_to_destination = distances[destination_index]
    
    if distance_to_destination < float('inf'):
        print("The number of stops from {} to {} is: {}".format(start_station, destination_station, distance_to_destination))
        # Optionally print the path using the print_path function
    else:
        print("Destination station is not reachable from the starting station.")

if __name__ == "__main__":
    main()
