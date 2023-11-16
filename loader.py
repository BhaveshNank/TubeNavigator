import csv

def load_graph_from_csv(csv_filename):
    graph = {}
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 4 or not row[3].strip().isdigit():  # Check for empty string or non-digit duration
                continue
            line, start, end, duration = row
            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            graph[start][end] = int(duration)
            # Assuming the graph is undirected and travel time is the same in both directions
            graph[end][start] = int(duration)
    
    return graph
