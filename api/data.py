import json
from typing import Any, Dict, List

try:
    with open("loads_DB.json", "r") as f:
        LOADS: List[Dict[str, Any]] = json.load(f)
except FileNotFoundError:
    print("Warning: loads_DB.json not found. The app will run with no load data.")
    LOADS = []
