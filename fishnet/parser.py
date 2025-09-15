# fishnet/parser.py
import email
from email import policy
from email.parser import BytesParser
import re
import hashlib

def parse_email(file_path):
    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    sender = msg["From"] if msg["From"] else "Unknown"
    recipients = msg.get_all("To", []) or []
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

    # Extract URLs
    urls = re.findall(r'http[s]?://[^\s"\'>]+', body)

    # Extract attachments with SHA256 hash
    attachments = []
    for part in msg.iter_attachments():
        filename = part.get_filename()
        payload = part.get_payload(decode=True)
        if filename and payload:
            sha256 = hashlib.sha256(payload).hexdigest()
            attachments.append({"filename": filename, "sha256": sha256})

    return {
        "from": sender,
        "to": recipients,
        "subject": subject,
        "urls": urls,
        "attachments": attachments,
    }
