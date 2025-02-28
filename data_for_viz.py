import json
import networkx as nx
import random
import string
from datetime import date, timedelta

def random_code():
    # Randomly choose a code length of 1 or 2 characters.
    length = random.choice([1, 2])
    return ''.join(random.choices(string.ascii_uppercase, k=length))

def random_date(start_date, end_date):
    """
    Returns a random date between start_date and end_date.
    """
    delta = end_date - start_date
    random_days = random.randrange(delta.days)  # random day offset
    return start_date + timedelta(days=random_days)

# Define the date range for node creation
start_date = date(2020, 1, 1)
end_date = date(2023, 1, 1)

# Generate some referral data
data = [(random_code(), random_code()) for _ in range(500)]

# Create a directed graph
G = nx.DiGraph()
G.add_edges_from(data)

# Assign each node a random date in the specified range
node_dates = {}
for node in G.nodes():
    node_dates[node] = random_date(start_date, end_date)

# Convert graph data into a format suitable for D3
# Include the "date_account_opened" for each node
nodes = []
for node in G.nodes():
    nodes.append({
        "id": node,
        "influence": G.out_degree(node),
        "date_account_opened": node_dates[node].isoformat()  # e.g. "2021-07-15"
    })

links = []
for source, target in G.edges():
    links.append({
        "source": source,
        "target": target
    })

graph = {"nodes": nodes, "links": links}

# Save the graph to a JSON file
with open("graph_data.json", "w") as f:
    json.dump(graph, f, indent=2)
