from loader2 import load_graph_from_csv
from task2 import dijkstra, get_user_input

def main():
    graph = load_graph_from_csv("London_underground_data.csv")
    # print(graph)
    start_station, destination_station = get_user_input()
    
    if start_station not in graph or destination_station not in graph:
        print("One or more of the stations entered do not exist in the network.")
        return

    distances, _ = dijkstra(graph, start_station)

    if destination_station in distances:
        print("The number of stops from {} to {} is: {}".format(start_station, destination_station, distances[destination_station]))
    else:
        print("Destination station is not reachable from the starting station.")


if __name__ == "__main__":
    main()
    
