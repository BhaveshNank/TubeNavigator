import csv
import heapq
from print_path import print_path as print_path_func


def load_graph_from_csv(csv_filename):
    graph = {}
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 4 or not row[3].strip().isdigit():  # Check for empty string or non-digit duration
                continue
            line, start, end, duration = row
            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            graph[start][end] = int(duration)
            # Assuming the graph is undirected and travel time is the same in both directions
            graph[end][start] = int(duration)
    
    return graph

def dijkstra(graph, start):
    """Compute shortest paths and distances in a graph from a starting point using Dijkstra's algorithm."""
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    priority_queue = [(0, start)]
    predecessors = {vertex: None for vertex in graph}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances, predecessors

def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station

def main():
    # Assuming `graph` is already defined and is the output of load_graph_from_csv()
    start_station, destination_station = get_user_input()
    
    if start_station not in graph or destination_station not in graph:
        print("One or more of the stations entered do not exist in the network.")
        return
# testing 
# graph = load_graph_from_csv("London_underground_data.csv")

# for start, destinations in graph.items():
#     for end, duration in destinations.items():
#         print("From {} to {}: {} minutes".format(start, end, duration))

# Testing
graph = load_graph_from_csv("London_underground_data.csv")


# Check if both stations are in the graph
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






