from scholarly import scholarly
import json
from datetime import datetime
import os
import sys
import signal

# -----------------------------
# CONFIG
# -----------------------------
TIMEOUT_SECONDS = 30
RESULT_DIR = "results"
AUTHOR_ID = os.environ.get("GOOGLE_SCHOLAR_ID")

# -----------------------------
# HARD TIMEOUT
# -----------------------------
def timeout_handler(signum, frame):
    print("ERROR: Scholar request timed out", flush=True)
    sys.exit(0)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(TIMEOUT_SECONDS)

# -----------------------------
# BASIC CHECK
# -----------------------------
if not AUTHOR_ID:
    print("ERROR: GOOGLE_SCHOLAR_ID not set", flush=True)
    sys.exit(1)

print("Starting Google Scholar scan", flush=True)

# -----------------------------
# FETCH AUTHOR (NO PROXIES)
# -----------------------------
try:
    print("Fetching author profile...", flush=True)
    author = scholarly.search_author_id(AUTHOR_ID)

    print("Filling author data...", flush=True)
    scholarly.fill(
        author,
        sections=["basics", "indices", "counts", "publications"]
    )

except Exception as e:
    print(f"Scholar fetch failed: {e}", flush=True)
    sys.exit(0)

# -----------------------------
# PROCESS DATA
# -----------------------------
author["updated"] = datetime.utcnow().isoformat() + "Z"

if "publications" in author:
    author["publications"] = {
        p.get("author_pub_id", str(i)): p
        for i, p in enumerate(author["publications"])
    }

# -----------------------------
# WRITE OUTPUTS
# -----------------------------
os.makedirs(RESULT_DIR, exist_ok=True)

with open(f"{RESULT_DIR}/gs_data.json", "w", encoding="utf-8") as f:
    json.dump(author, f, ensure_ascii=False, indent=2)

shieldio_data = {
    "schemaVersion": 1,
    "label": "citations",
    "message": str(author.get("citedby", "0")),
}

with open(f"{RESULT_DIR}/gs_data_shieldsio.json", "w", encoding="utf-8") as f:
    json.dump(shieldio_data, f, ensure_ascii=False)

print("Google Scholar scan completed successfully", flush=True)

signal.alarm(0)
