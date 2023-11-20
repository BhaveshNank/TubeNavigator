import matplotlib.pyplot as plt
from itertools import combinations
from loader2 import load_graph_from_csv
from dijkstra import dijkstra
from task2 import convert_graph
import time 

start = time.time()
def calculate_all_pairs_stops(graph):
    all_stops = []
    for start_index, destination_index in combinations(range(graph.get_card_V()), 2):
        distances, _ = dijkstra(graph, start_index)
        if distances[destination_index] < float('infinity'):
            all_stops.append(distances[destination_index])
    return all_stops


def plot_histogram(stops_counts):
    plt.hist(stops_counts, bins=range(1, max(stops_counts) + 2), edgecolor='black')
    plt.title('Histogram of Stops Count between Station Pairs')
    plt.xlabel('Number of Stops')
    plt.ylabel('Frequency')
    plt.show()

def main():
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    graph, _, _ = convert_graph(dictionary_graph)
    stops_counts = calculate_all_pairs_stops(graph)
    plot_histogram(stops_counts)

if __name__ == "__main__":
    main()
end = time.time()
total_time = end-start
print(total_time)
