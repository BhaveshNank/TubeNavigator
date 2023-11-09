import matplotlib.pyplot as plt
from itertools import combinations
from loader2 import load_graph_from_csv
from task2 import dijkstra

def calculate_all_pairs_stops(graph):
    all_stops = []
    for start_station, destination_station in combinations(graph.keys(), 2):
        distances, _ = dijkstra(graph, start_station)
        if destination_station in distances:
            all_stops.append(distances[destination_station])
    return all_stops

def plot_histogram(stops_counts):
    plt.hist(stops_counts, bins=range(1, max(stops_counts) + 2), edgecolor='black')
    plt.title('Histogram of Stops Count between Station Pairs')
    plt.xlabel('Number of Stops')
    plt.ylabel('Frequency')
    plt.show()

def main():
    graph = load_graph_from_csv("London_underground_data.csv")
    stops_counts = calculate_all_pairs_stops(graph)
    plot_histogram(stops_counts)

if __name__ == "__main__":
    main()
