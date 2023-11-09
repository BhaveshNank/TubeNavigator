import heapq

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # The priority queue stores entries as (distance, vertex)
    priority_queue = [(0, start)]
    predecessors = {vertex: None for vertex in graph}

    # Set to keep track of visited nodes to prevent processing a node more than once
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        # Iterate over the neighbors of the current node
        for neighbor in graph[current_vertex]:
            distance = current_distance + 1  # Since each edge represents 1 stop

            # Only consider this new path if it's better than any path we've
            # already found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors


def get_user_input():
    start_station = input("Please enter your starting station: ")
    destination_station = input("Please enter your destination station: ")
    return start_station, destination_station
