
class LoopStrategyDecider:
    def __init__(self):
        self.current_strategy = "기본"

    def decide(self, keyword, resonance_score):
        if "불안" in keyword or resonance_score < 0.5:
            self.current_strategy = "성찰 강화 루프"
        elif "사랑" in keyword and resonance_score > 0.8:
            self.current_strategy = "확장 선언 루프"
        else:
            self.current_strategy = "기본 흐름 유지"
        return self.current_strategy
