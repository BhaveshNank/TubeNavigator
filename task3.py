# Import necessary modules
from bfs import bfs  # Import Breadth-First Search (BFS) algorithm implementation
from loader3 import load_graph_for_bfs # Import a function to load a graph for BFS

# Function to get user input for start and destination stations
def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

# Function to reconstruct the path from predecessors
def reconstruct_path(predecessors, start_index, end_index, index_to_station):
    path = []
    current = end_index
    while current != start_index:
        path.insert(0, index_to_station[current])
        current = predecessors[current]
        if current is None:
            return None  # Path not found
    path.insert(0, index_to_station[start_index])
    return path


# Main function to run the program
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
        path = reconstruct_path(predecessors, start_index, destination_index, index_to_station)
        if path:
            print(f"Path from {start_station} to {destination_station}:")
            for station in path:
                print(station)
            print(f"Total number of stations: {len(path) - 1}")  # Subtract 1 because path includes the starting station
        else:
            print("No path found.")
    else:
        print("Destination station is not reachable from the starting station.")

# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()
