
from reinforcement_memory import ReinforcementMemory
from declaration_self_evaluator import evaluate_declaration

class ReinforcedEvolverWithEvaluation:
    def __init__(self):
        self.memory = ReinforcementMemory()

    def add(self, declaration: str):
        score = evaluate_declaration(declaration)
        self.memory.add(declaration, score)

    def evolve(self) -> str:
        top_declarations = self.memory.top_n(3)
        if not top_declarations:
            return "진화 불가: 선언 부족"
        merged = " · ".join(top_declarations)
        return f"자기 평가 기반 진화 선언: {merged}"
