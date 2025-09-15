# scripts/ingest_folder.py
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fishnet.parser import parse_email
from fishnet.visualize import ascii_visualize
from fishnet.exporter import export_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python -m scripts.ingest_folder <folder_path>")
        return

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"[!] Not a valid folder: {folder_path}")
        return

    eml_files = [f for f in os.listdir(folder_path) if f.endswith(".eml")]
    if not eml_files:
        print("[!] No .eml files found in folder")
        return

    for file_name in eml_files:
        file_path = os.path.join(folder_path, file_name)
        print(f"\n=== Processing {file_name} ===")
        email_data = parse_email(file_path)
        ascii_visualize(email_data)

        # Save full JSON report per file
        export_report(email_data, filename=file_name + ".json")

if __name__ == "__main__":
    main()
