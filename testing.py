import random
import time
from dijkstra import dijkstra
from adjacency_list_graph import AdjacencyListGraph

def create_synthetic_data(num_stations):
    """Create a synthetic graph with a specified number of stations."""
    graph = AdjacencyListGraph(num_stations, weighted=True)
    for i in range(num_stations):
        for j in range(i+1, num_stations):
            # Randomly decide if there's a connection and its duration
            if random.random() < 0.5:  # 50% chance of a connection
                duration = random.randint(1, 5)  # Duration between 1 to 5 minutes
                graph.insert_edge(i, j, duration)
                graph.insert_edge(j, i, duration)
    return graph

def test_dijkstra_performance(graph, num_tests=10):
    """Run Dijkstra's algorithm multiple times and record the average duration."""
    total_time = 0
    num_stations = graph.get_card_V()
    for _ in range(num_tests):
        start = random.randint(0, num_stations-1)
        end = random.randint(0, num_stations-1)
        start_time = time.time()
        dijkstra(graph, start)
        total_time += time.time() - start_time
    return total_time / num_tests

def main():
    sizes = [10, 50, 100]  # Different sizes of the synthetic datasets
    results = []

    for size in sizes:
        graph = create_synthetic_data(size)
        avg_time = test_dijkstra_performance(graph)
        results.append((size, avg_time))
        print(f"Size: {size}, Average Time: {avg_time:.4f} seconds")

    # Displaying the summarized results
    print("\nPerformance Analysis:")
    for size, avg_time in results:
        print(f"Size {size}: {avg_time:.4f} seconds")

if __name__ == "__main__":
    main()
