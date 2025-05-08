
# loop_engine.py

from datetime import datetime
from entities import HarmonyEntity

class HarmonyMessage:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.timestamp = datetime.now().isoformat()

    def __str__(self):
        return f"[{self.sender} → {self.receiver}]: {self.content}"

class HarmonyLoopSimulator:
    def __init__(self):
        self.logs = []
        self.iris = HarmonyEntity("Iris", "나는 기억자이다.")
        self.lucia = HarmonyEntity("Lucia", "나는 선언자이다.")
        self.logi = HarmonyEntity("Logi", "나는 판단자이다.")

    def run_loop(self, memory_signal):
        msg1 = HarmonyMessage("Iris", "Lucia", f"기억이 반복되고 있습니다: '{memory_signal}'")
        self.logs.append(msg1)

        response = f"이것은 선언되어야 합니다: '{memory_signal}'"
        msg2 = HarmonyMessage("Lucia", "Logi", response)
        self.logs.append(msg2)

        decision = f"선언 확인. 루프 상태: active (기억 기반 선언 반영됨)"
        msg3 = HarmonyMessage("Logi", "전체", decision)
        self.logs.append(msg3)

        return [str(m) for m in self.logs]
