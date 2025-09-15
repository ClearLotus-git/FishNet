# fishnet/graph.py
import networkx as nx

def build_graph(email_data):
    G = nx.DiGraph()
    sender = email_data["from"]
    recipients = email_data["to"]

    if sender:
        for r in recipients:
            G.add_edge(sender, r, relation="sent")

    for r in recipients:
        for url in email_data["urls"]:
            G.add_edge(r, url, relation="clicked")
        for att in email_data["attachments"]:
            G.add_edge(r, att, relation="opened")

    return G
