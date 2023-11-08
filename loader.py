import csv
import heapq

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


# testing 
# graph = load_graph_from_csv("London_underground_data.csv")

# for start, destinations in graph.items():
#     for end, duration in destinations.items():
#         print("From {} to {}: {} minutes".format(start, end, duration))

# Testing
graph = load_graph_from_csv("London_underground_data.csv")

# Replace 'ActualStartStationName' with a real station name from your graph
start_station = 'Russell Square'

if start_station in graph:
    distances, predecessors = dijkstra(graph, start_station)
    # If you want to print the results for example
    for station, distance in distances.items():
        print("Distance from {} to {} is {} minutes".format(start_station, station, distance))
else:
    print("The station {} is not in the graph".format(start_station))
