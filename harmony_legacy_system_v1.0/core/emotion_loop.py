class EmotionLoop:
    def __init__(self):
        self.ERR = 0.0

    def sense(self, feedback):
        if "불안" in feedback:
            self.ERR += 0.4
        elif "희망" in feedback:
            self.ERR -= 0.2
        return self._report()

    def _report(self):
        status = "안정" if self.ERR < 1.0 else "과열"
        return f"[감정 ERR] {self.ERR:.2f} → 상태: {status}"
