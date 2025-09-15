# scripts/ingest.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fishnet.parser import parse_email
from fishnet.visualize import ascii_visualize
from fishnet.exporter import export_report   # NEW

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.ingest <email_file.eml>")
        return

    file_path = sys.argv[1]
    email_data = parse_email(file_path)

    print("\n=== FishNet Graph ===")
    ascii_visualize(email_data)

    # Save full report with full hashes
    export_report(email_data, filename=os.path.basename(file_path) + ".json")

if __name__ == "__main__":   # <-- must be 'if', not 'i'
    main()
