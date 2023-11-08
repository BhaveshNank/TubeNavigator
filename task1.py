import heapq

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