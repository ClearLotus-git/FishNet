# fishnet/parser.py
import email
from email import policy
from email.parser import BytesParser
import re

def parse_email(file_path):
    try:
        with open(file_path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)
    except Exception as e:
        print(f"[!] Error parsing email: {e}")
        return {
            "from": None,
            "to": [],
            "subject": None,
            "urls": [],
            "attachments": []
        }

    # From / To
    sender = msg["From"] if msg["From"] else "Unknown"
    recipients = msg.get_all("To", []) or []

    # Subject
    subject = msg["Subject"] if msg["Subject"] else "No Subject"

    # Extract body
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() in ["text/plain", "text/html"]:
                try:
                    body += part.get_payload(decode=True).decode(errors="ignore")
                except:
                    pass
    else:
        try:
            body = msg.get_payload(decode=True).decode(errors="ignore")
        except:
            pass

    # URLs
    urls = re.findall(r'http[s]?://\S+', body)

    # Attachments
    attachments = []
    for part in msg.iter_attachments():
        attachments.append(part.get_filename())

    return {
        "from": sender,
        "to": recipients,
        "subject": subject,
        "urls": urls,
        "attachments": attachments,
    }
