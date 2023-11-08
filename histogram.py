import matplotlib.pyplot as plt

# Import your graph loading and Dijkstra's function
from loader import load_graph_from_csv
from task1 import dijkstra

def calculate_journey_times_for_all_pairs(graph):
    journey_times = []
    for start_station in graph:
        distances, _ = dijkstra(graph, start_station)
        for end_station in graph:
            if start_station != end_station:
                # Make sure to check if a path to the end_station exists
                if end_station in distances:
                    journey_times.append(distances[end_station])
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
    graph = load_graph_from_csv("London_underground_data.csv")
    journey_times = calculate_journey_times_for_all_pairs(graph)
    plot_histogram(journey_times)

if __name__ == "__main__":
    main()
