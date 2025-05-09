
import json
from datetime import datetime

class TimelineLogger:
    def __init__(self, file_path="declaration_timeline.json"):
        self.file_path = file_path
        self.logs = []

    def log(self, role, content):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "role": role,
            "content": content
        }
        self.logs.append(entry)

    def save(self):
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(self.logs, f, ensure_ascii=False, indent=2)
