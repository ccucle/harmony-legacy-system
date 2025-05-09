
from agents.logi_gpt_agent import LogiGPTAgent
from self_reflection_engine import generate_self_reflection

class LogiReflectiveAgent(LogiGPTAgent):
    def evaluate_declaration(self, declaration, history, keywords):
        base_eval = super().evaluate_declaration(declaration, history, keywords)
        reflection = generate_self_reflection(declaration, base_eval)
        return f"{base_eval}\n→ 자기 성찰: {reflection}"
