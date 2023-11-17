import matplotlib.pyplot as plt
from loader import load_graph_from_csv
from dijkstra import dijkstra
from task1 import convert_graph

def calculate_journey_times_for_all_pairs(graph, station_to_index):
    journey_times = []
    for start_station in station_to_index.keys():
        start_index = station_to_index[start_station]
        distances, _ = dijkstra(graph, start_index)
        for end_station in station_to_index.keys():
            if start_station != end_station:
                end_index = station_to_index[end_station]
                # Make sure to check if a path to the end_station exists
                if distances[end_index] != float('infinity'):
                    journey_times.append(distances[end_index])
    return journey_times


def plot_histogram(journey_times):
    # Dynamically create bins based on the journey times
    min_time = min(journey_times)
    max_time = max(journey_times)
    bin_size = 1  # You can change the size of the bin depending on your data
    bins = range(int(min_time), int(max_time) + bin_size, bin_size)
    
    # Plot the histogram
    plt.hist(journey_times, bins=bins, edgecolor='black')
    plt.title('Histogram of Journey Times')
    plt.xlabel('Journey Time (minutes)')
    plt.ylabel('Number of Station Pairs')
    plt.show()

def main():
    dictionary_graph = load_graph_from_csv("London_underground_data.csv")
    graph, station_to_index, _ = convert_graph(dictionary_graph)
    journey_times = calculate_journey_times_for_all_pairs(graph, station_to_index)
    plot_histogram(journey_times)

if __name__ == "__main__":
    main()
