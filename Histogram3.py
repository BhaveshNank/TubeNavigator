import matplotlib.pyplot as plt

# Import your graph loading and Dijkstra's function
from loader3 import load_graph_for_bfs
from task3 import load_graph_for_bfs
from bfs import bfs

def calculate_stops_between_stations(graph, station_to_index, index_to_station):
    num_stations = len(station_to_index)
    journey_times = []

    for start in range(num_stations):
        distances, _ = bfs(graph, start)
        for end in range(num_stations):
            if start != end and distances[end] < float('inf'):
                journey_times.append(distances[end])

    return journey_times



def plot_histogram(journey_times):
    plt.hist(journey_times, bins=range(max(journey_times)+1), edgecolor='black')
    plt.title('Histogram of Journey Times (Number of Stops)')
    plt.xlabel('Number of Stops')
    plt.ylabel('Frequency')
    plt.show()

# Main Function
def main():
    graph, station_to_index, index_to_station = load_graph_for_bfs("London_underground_data.csv")
    journey_times = calculate_stops_between_stations(graph, station_to_index, index_to_station)
    plot_histogram(journey_times)

if __name__ == "__main__":
    main()
