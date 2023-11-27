import matplotlib.pyplot as plt
from loader import load_graph_from_csv
from dijkstra import dijkstra
from task1 import convert_graph  # Ensure this is the correct import for your setup
import shutdown_analysis  # Import your shutdown_analysis module

def calculate_journey_times(graph, station_to_index):
    journey_times = []
    for start_station in station_to_index:
        start_index = station_to_index[start_station]
        distances, _ = dijkstra(graph, start_index)
        for end_station in station_to_index:
            end_index = station_to_index[end_station]
            if start_station != end_station and distances[end_index] != float('infinity'):
                journey_times.append(distances[end_index])
    return journey_times


def plot_histogram(journey_times, title):
    plt.hist(journey_times, bins=range(min(journey_times), max(journey_times) + 1), edgecolor='black')
    plt.title(title)
    plt.xlabel('Journey Time (minutes)')
    plt.ylabel('Number of Station Pairs')
    plt.show()

def main():
    # Load and convert the original graph
    original_graph_data = load_graph_from_csv("London_underground_data.csv")
    original_graph, station_to_index, index_to_station = convert_graph(original_graph_data)

    # Calculate journey times for the original graph
    original_journey_times = calculate_journey_times(original_graph, station_to_index)
    plot_histogram(original_journey_times, "Pre-Shutdown Journey Times")

    # Load shutdown routes from the file
    shutdown_routes = shutdown_analysis.read_shutdown_routes("shutdown_routes.txt")

    # Modify the graph for shutdown
    modified_graph = shutdown_analysis.modify_graph_for_shutdown(original_graph, shutdown_routes, station_to_index)

    # Calculate journey times for the modified graph
    modified_journey_times = calculate_journey_times(modified_graph, station_to_index)
    plot_histogram(modified_journey_times, "Post-Shutdown Journey Times")

if __name__ == "__main__":
    main()
