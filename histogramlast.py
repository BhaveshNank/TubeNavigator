import matplotlib.pyplot as plt
import random
from dijkstra import dijkstra
from adjacency_list_graph import AdjacencyListGraph

def create_synthetic_network(num_stations):
    """ Create a synthetic network with specified number of stations. """
    graph = AdjacencyListGraph(num_stations, weighted=True)
    for i in range(num_stations):
        for j in range(i+1, num_stations):
            if random.random() < 0.5:  # 50% chance of a connection
                duration = random.randint(1, 10)  # Random duration between stations
                graph.insert_edge(i, j, duration)
                graph.insert_edge(j, i, duration)
    return graph

def calculate_journey_time(graph, start_index, end_index):
    """ Calculate journey time between two stations. """
    distances, _ = dijkstra(graph, start_index)
    return distances[end_index]

def simulate_closure(graph, closed_stations_indices):
    """ Simulate closure of stations in the graph. """
    for i in closed_stations_indices:
        for j in range(graph.get_card_V()):
            graph.delete_edge(i, j, delete_undirected=True)
            graph.delete_edge(j, i, delete_undirected=True)

def generate_histogram(journey_times, title):
    plt.hist(journey_times, bins=range(min(journey_times), max(journey_times) + 1, 1), color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel('Journey Time')
    plt.ylabel('Frequency')
    plt.show()

def main():
    num_stations = 20  # Example number of stations
    graph = create_synthetic_network(num_stations)

    # Indices for Station A and Station B
    station_a_index = 0  # Replace with actual index
    station_b_index = 1  # Replace with actual index

    # Calculate journey times before closure
    journey_times_before = [calculate_journey_time(graph, station_a_index, station_b_index) for _ in range(100)]

    # Simulate closure
    simulate_closure(graph, [2, 3])  # Example: Close stations 2 and 3

    # Calculate journey times after closure
    journey_times_after = [calculate_journey_time(graph, station_a_index, station_b_index) for _ in range(100)]

    # Generate histograms
    generate_histogram(journey_times_before, 'Journey Time Before Closure')
    generate_histogram(journey_times_after, 'Journey Time After Closure')

if __name__ == "__main__":
    main()
