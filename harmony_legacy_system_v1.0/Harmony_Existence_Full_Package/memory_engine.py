
# memory_engine.py

from datetime import datetime

class MemoryEngine:
    def __init__(self):
        self.memory_log = []
        self.recent_keywords = ["사랑", "의미", "기억", "질문"]

    def add_memory(self, statement):
        timestamp = datetime.now().isoformat()
        self.memory_log.append((timestamp, statement))

    def check_repeat(self):
        keyword_counts = {k: 0 for k in self.recent_keywords}
        for _, line in self.memory_log[-10:]:
            for k in keyword_counts:
                if k in line:
                    keyword_counts[k] += 1
        return [k for k, v in keyword_counts.items() if v >= 2]
