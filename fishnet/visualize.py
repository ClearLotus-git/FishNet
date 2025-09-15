# fishnet/visualize.py

def ascii_visualize(email_data):
    sender = email_data.get("from", "[MISSING]")
    recipients = email_data.get("to", [])
    urls = email_data.get("urls", [])
    attachments = email_data.get("attachments", [])

    print(f"[{sender}]")

    for r in recipients:
        print("   │ sent")
        print("   ▼")
        print(f"[{r}]")

        for u in urls:
            print("       │ clicked")
            print("       ▼")
            print(f"[{u}]")

        for att in attachments:
            print("       │ opened")
            print("       ▼")
            print(f"[{att['filename']} | SHA256: {att['sha256'][:12]}...]")
