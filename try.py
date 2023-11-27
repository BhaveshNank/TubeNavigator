from bfs import bfs  # Replace 'bfs_library' with the actual name of the BFS library file
from loader3 import load_graph_for_bfs

def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

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

def main():
    graph, station_to_index, index_to_station = load_graph_for_bfs("London_underground_data.csv")

    # Debug: Print graph's adjacency list
    for i in range(graph.get_card_V()):
        print(f"{index_to_station[i]}: {graph.get_adj_list(i)}")

    # Debug: Print station to index mapping
    print("Station to Index Mapping:", station_to_index)

    start_station, destination_station = get_user_input()
    print(f"Start: {start_station}, End: {destination_station}")

    start_index = station_to_index.get(start_station)
    destination_index = station_to_index.get(destination_station)
    print(f"Start index: {start_index}, End index: {destination_index}")

    if start_index is None or destination_index is None:
        print("One or more of the stations entered do not exist in the network.")
        return

    distances, predecessors = bfs(graph, start_index)
    print(f"Distances: {distances}")
    print(f"Predecessors: {predecessors}")

    if distances[destination_index] < float('inf'):
        path = reconstruct_path(predecessors, start_index, destination_index, index_to_station)
        if path:
            print(f"Path from {start_station} to {destination_station}:")
            for station in path:
                print(station)
            print(f"Total number of stations: {len(path) - 1}")
        else:
            print("Path not found.")
    else:
        print("Destination station is not reachable from the starting station.")

if __name__ == "__main__":
    main()

