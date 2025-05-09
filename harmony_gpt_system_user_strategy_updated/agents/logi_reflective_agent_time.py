
from agents.logi_gpt_agent import LogiGPTAgent
from self_reflection_engine import generate_self_reflection
from utils.now_time import get_current_time

class LogiReflectiveAgentWithTime(LogiGPTAgent):
    def evaluate_declaration(self, declaration, history, keywords):
        base_eval = super().evaluate_declaration(declaration, history, keywords)
        reflection = generate_self_reflection(declaration, base_eval)
        current_time = get_current_time()
        return (
            f"[현재 시각: {current_time}]\n"
            f"{base_eval}\n→ 자기 성찰: {reflection}"
        )
