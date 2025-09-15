# scripts/ingest.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fishnet.parser import parse_email
from fishnet.graph import build_graph


def main():
    if len(sys.argv) != 2:
        print("Usage: python ingest.py <email_file.eml>")
        return

    file_path = sys.argv[1]
    email_data = parse_email(file_path)
    graph = build_graph(email_data)

    print("\n=== FishNet Graph ===")
    for edge in graph.edges(data=True):
        print(f"{edge[0]} --{edge[2]['relation']}--> {edge[1]}")

if __name__ == "__main__":
    main()
