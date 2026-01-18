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
# HARD TIMEOUT (prevents hang)
# -----------------------------
def timeout_handler(signum, frame):
    print("ERROR: Google Scholar request timed out", flush=True)
    sys.exit(0)

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(TIMEOUT_SECONDS)

# -----------------------------
# BASIC CHECKS
# -----------------------------
if not AUTHOR_ID:
    print("ERROR: GOOGLE_SCHOLAR_ID not set", flush=True)
    sys.exit(1)

print("Starting Google Scholar scan", flush=True)

# -----------------------------
# SCHOLARLY SAFETY SETTINGS
# -----------------------------
scholarly.use_proxy(None)      # disable free-proxy
scholarly.set_timeout(10)      # internal request timeout

# -----------------------------
# FETCH AUTHOR
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

# Reduce payload size (important for CI)
if "publications" in author:
    author["publications"] = {
        p["author_pub_id"]: p
        for p in author["publications"]
        if "author_pub_id" in p
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

# Cancel alarm if everything finished
signal.alarm(0)
