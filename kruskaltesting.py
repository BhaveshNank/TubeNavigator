import random
import time
from adjacency_list_graph import AdjacencyListGraph
from task4a import kruskals_algorithm  # Replace with your actual Kruskal's algorithm import

def create_synthetic_network(num_stations, connection_probability=0.5):
    """Creates a synthetic network with a given number of stations and connection probability."""
    graph = AdjacencyListGraph(num_stations, weighted=True)
    for i in range(num_stations):
        for j in range(i + 1, num_stations):
            if random.random() < connection_probability:  # Connection probability
                weight = random.randint(1, 10)  # Random weight for the edge
                graph.insert_edge(i, j, weight)
                graph.insert_edge(j, i, weight)
    return graph

def test_kruskals_algorithm(graph):
    """Tests Kruskal's algorithm on the graph and returns the execution time."""
    start_time = time.time()
    kruskals_algorithm(graph)
    execution_time = time.time() - start_time
    return execution_time

# Test with different sizes of synthetic data
sizes = [20]
results = []

for size in sizes:
    graph = create_synthetic_network(size)
    time_taken = test_kruskals_algorithm(graph)
    results.append((size, time_taken))

# Print the test results
print("Kruskal's Algorithm Test Results:")
for size, time_taken in results:
    print(f"Size: {size}, Time Taken: {time_taken:.4f} seconds")
