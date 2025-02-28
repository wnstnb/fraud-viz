from flask import Flask, jsonify, render_template
import json
import networkx as nx
import random
import string

app = Flask(__name__)

def random_code():
    length = random.choice([1, 2])
    return ''.join(random.choices(string.ascii_uppercase, k=length))

@app.route('/data')
def data():
    # Generate referral data and graph
    data = [(random_code(), random_code()) for _ in range(1000)]
    G = nx.DiGraph()
    G.add_edges_from(data)
    nodes = [{"id": node, "influence": G.out_degree(node)} for node in G.nodes()]
    links = [{"source": source, "target": target} for source, target in G.edges()]
    graph = {"nodes": nodes, "links": links}
    return jsonify(graph)

@app.route('/')
def index():
    return render_template("index.html")  # This will use templates/index.html

if __name__ == '__main__':
    app.run(debug=True)
