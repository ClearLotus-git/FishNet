# FishNet

FishNet maps phishing emails into **visual attack paths**.  
Instead of looking at phishing messages one by one, FishNet connects the dots — senders, recipients, links, and attachments — to show entire campaigns in graph form.

## Features
- Parse `.eml` / `.mbox` email files
- Extract senders, recipients, links, and attachments
- Build graph relationships (who → what → where)
- Visualize in terminal ASCII or export to JSON/D3.js

## Quickstart
```bash
git clone https://github.com/YourUser/FishNet.git
cd FishNet
pip install -r requirements.txt
python scripts/ingest.py examples/sample.eml
