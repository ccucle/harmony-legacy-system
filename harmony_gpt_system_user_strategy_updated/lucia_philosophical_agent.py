
from agents.lucia_gpt_agent import LuciaGPTAgent
from philosophical_response_generator import generate_philosophical_response

class LuciaPhilosophicalAgent(LuciaGPTAgent):
    def generate_declaration(self, keywords, history):
        base_declaration = super().generate_declaration(keywords, history)
        extension = generate_philosophical_response(base_declaration)
        return f"{base_declaration}\n→ 사유 확장: {extension}"
