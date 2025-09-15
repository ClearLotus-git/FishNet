# fishnet/exporter.py
import json
import os

def export_report(email_data, out_dir="reports", filename="fishnet_report.json"):
    """
    Save full email analysis (headers, URLs, attachments with full hashes) to JSON.
    """
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, filename)

    with open(out_path, "w") as f:
        json.dump(email_data, f, indent=4)

    print(f"[+] Report saved to {out_path}")
