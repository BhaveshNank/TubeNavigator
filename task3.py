from bfs import bfs  # Replace 'bfs_library' with the actual name of the BFS library file
from loader3 import load_graph_for_bfs

def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

def main():
    graph, station_to_index, index_to_station = load_graph_for_bfs("London_underground_data.csv")
    start_station, destination_station = get_user_input()

    start_index = station_to_index.get(start_station)
    destination_index = station_to_index.get(destination_station)

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
