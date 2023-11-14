from loader import load_graph_from_csv
from task1 import dijkstra
from print_path import print_path as print_path_func

def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

def main():
    graph = load_graph_from_csv("London_underground_data.csv")
    # Assuming `graph` is already defined and is the output of load_graph_from_csv()
    start_station, destination_station = get_user_input()
    
    if start_station not in graph or destination_station not in graph:
        print("One or more of the stations entered do not exist in the network.")
        return

    # Run Dijkstra's algorithm to find shortest paths from start_station
    distances, predecessors = dijkstra(graph, start_station)

    # Check if the destination_station is reachable
    if destination_station in distances:
        # Define a mapping function (identity function if using station names)
        mapping_func = lambda x: x

        # Use the print_path function to get the path from start_station to destination_station
        path = print_path_func(predecessors, start_station, destination_station, mapping_func)

        # Check if a path exists
        if path:
            print("Path from {} to {}:".format(start_station, destination_station))
            for station in path:
                print(station)
            total_duration = distances[destination_station]
            print("Total journey time: {} minutes".format(total_duration))
        else:
            print("No path exists from {} to {}.".format(start_station, destination_station))
    else:
        print("Destination station is not reachable from the starting station.")

if __name__ == "__main__":
    main()
