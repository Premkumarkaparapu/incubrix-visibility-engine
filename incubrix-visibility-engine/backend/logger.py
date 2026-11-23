import json
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

class EngineLogger:
    def __init__(self, run_name: str = "engine"):
        self.log_file = os.path.join(LOG_DIR, f"{run_name}.log")
        
    def log(self, level: str, message: str, context: dict = None):
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": level.upper(),
            "message": message,
            "context": context or {}
        }
        with open(self.log_file, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        print(f"[{entry['level']}] {entry['message']}")

    def info(self, msg: str, ctx: dict = None):
        self.log("INFO", msg, ctx)

    def warning(self, msg: str, ctx: dict = None):
        self.log("WARNING", msg, ctx)

    def error(self, msg: str, ctx: dict = None):
        self.log("ERROR", msg, ctx)
