import csv

def load_graph_from_csv(csv_filename):
    graph = {}
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) < 3:  # Check for at least three entries
                continue
            line, start, end = row[:3]
            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            # Here we assume the weight to be '1' for each stop.
            graph[start][end] = 1
            graph[end][start] = 1  # Assuming the graph is undirected
    
    return graph
