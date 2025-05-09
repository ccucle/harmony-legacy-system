
from utils.now_time import get_current_time

class EhrAgentWithTime:
    def __init__(self):
        self.name = "Ehr"

    def analyze_resonance(self, declarations, questions, evaluations) -> str:
        current_time = get_current_time()
        if not declarations or not questions or not evaluations:
            return f"[현재 시각: {current_time}]\n공명 없음"

        last_dec = declarations[-1]
        last_que = questions[-1]
        last_eval = evaluations[-1]

        if "충돌" in last_eval or "불일치" in last_eval:
            resonance = "공명 약함"
        elif "일치" in last_eval or "조화" in last_eval:
            resonance = "공명 강함"
        else:
            resonance = "공명 중간"

        return f"[현재 시각: {current_time}]\n{resonance}"
