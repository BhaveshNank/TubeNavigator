from adjacency_list_graph import AdjacencyListGraph
from task4a import kruskals_algorithm  # Replace with your actual Kruskal's algorithm import
import random
import time

def create_synthetic_network(num_stations, density=0.5):
    """ Creates a synthetic network with a given number of stations and connection density. """
    graph = AdjacencyListGraph(num_stations, weighted=True)
    for i in range(num_stations):
        for j in range(i + 1, num_stations):
            if random.random() < density:
                weight = random.randint(1, 10)
                graph.insert_edge(i, j, weight)
                graph.insert_edge(j, i, weight)
    return graph

def test_kruskals_performance(graph):
    """ Measures the performance of Kruskal's algorithm on the given graph. """
    start_time = time.time()
    kruskals_algorithm(graph)
    end_time = time.time()
    return end_time - start_time

# Example usage
sizes = [10, 50, 100, 200]  # Different sizes of the synthetic datasets
for size in sizes:
    synthetic_network = create_synthetic_network(size)
    time_taken = test_kruskals_performance(synthetic_network)
    print(f"Size: {size}, Time taken by Kruskal's algorithm: {time_taken:.4f} seconds")
