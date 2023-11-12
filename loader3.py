import csv
from adjacency_list_graph import AdjacencyListGraph

def load_graph_for_bfs(csv_filename):
    unique_stations = set()
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        for row in reader:
            if len(row) < 3:
                continue
            start, end = row[1].strip(), row[2].strip()
            unique_stations.update([start, end])

    # Create mappings
    station_to_index = {station: index for index, station in enumerate(unique_stations)}
    # print("Station to Index Mapping:", station_to_index)

    index_to_station = {index: station for station, index in station_to_index.items()}

    # Create the graph with the number of unique stations
    graph = AdjacencyListGraph(len(unique_stations))
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header
        for row in reader:
            if len(row) < 3 or not row[1].strip() or not row[2].strip():
                continue
            start, end = row[1].strip(), row[2].strip()
            # print(f"Processing edge: {start} -> {end}")  # Debugging print

            if start not in station_to_index or end not in station_to_index:
                # print(f"Missing station in mapping: start={start}, end={end}")
                continue

            start_idx = station_to_index[start]
            end_idx = station_to_index[end]
            if not graph.has_edge(start_idx, end_idx):
                graph.insert_edge(start_idx, end_idx)

    return graph, station_to_index, index_to_station
if __name__ == "__main__":
    # Example usage of load_graph_for_bfs
    graph, station_to_index, index_to_station = load_graph_for_bfs("London_underground_data.csv")
    # print("Graph loaded successfully")
    print("Number of stations:", len(station_to_index))
    # Add more print statements or logic as needed to test the functionality