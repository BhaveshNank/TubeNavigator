import csv
from adjacency_list_graph import AdjacencyListGraph

def load_graph_for_bfs(csv_filename):
    graph = AdjacencyListGraph()
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row if there is one
        for row in reader:
            if len(row) < 3 or not row[1].strip() or not row[2].strip():
                continue
            start, end = row[1].strip(), row[2].strip()
            graph.insert_edge(start, end)
    return graph
