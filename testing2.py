import random
import time
from bfs import bfs  # Assuming you have a BFS implementation in bfs.py
from adjacency_list_graph import AdjacencyListGraph

def create_synthetic_unweighted_graph(num_stations):
    """Create a synthetic unweighted graph with a specified number of stations."""
    graph = AdjacencyListGraph(num_stations, weighted=False)
    for i in range(num_stations):
        for j in range(i+1, num_stations):
            # Randomly decide if there's a connection
            if random.random() < 0.5:  # 50% chance of a connection
                graph.insert_edge(i, j)
                graph.insert_edge(j, i)
    return graph

def test_bfs_performance(graph, num_tests=10):
    """Run BFS multiple times and record the average duration."""
    total_time = 0
    num_stations = graph.get_card_V()
    for _ in range(num_tests):
        start = random.randint(0, num_stations-1)
        start_time = time.time()
        bfs(graph, start)  # Assuming your BFS function signature is bfs(graph, start, end)
        total_time += time.time() - start_time
    return total_time / num_tests

def main():
    sizes = [10, 50, 100]  # Different sizes of the synthetic datasets
    results = []

    for size in sizes:
        graph = create_synthetic_unweighted_graph(size)
        avg_time = test_bfs_performance(graph)
        results.append((size, avg_time))
        print(f"Size: {size}, Average Time: {avg_time:.4f} seconds")

    # Displaying the summarized results
    print("\nPerformance Analysis:")
    for size, avg_time in results:
        print(f"Size {size}: {avg_time:.4f} seconds")

if __name__ == "__main__":
    main()
