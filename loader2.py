import csv

def load_graph_from_csv(csv_filename):
    graph = {}
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)  # Skip the header row if there is one
        for row in reader:
            # Ignore rows that don't have at least three columns
            if len(row) < 3 or not row[1].strip() or not row[2].strip():
                continue
            
            # Trim any whitespace from the station names
            line, start, end = row[:3]
            start = start.strip()
            end = end.strip()
            
            # Ignore rows with empty station names
            if not start or not end:
                continue

            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            graph[start][end] = 1
            graph[end][start] = 1
    
    return graph 
    
