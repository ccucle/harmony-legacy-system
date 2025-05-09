
from agents.lucia_gpt_agent import LuciaGPTAgent
from philosophical_response_generator import generate_philosophical_response

class LuciaUserStyleAgent(LuciaGPTAgent):
    def __init__(self, openai_api_key: str, user_name="Lucia", goal="존재 탐구", style="시적"):
        super().__init__(openai_api_key)
        self.user_name = user_name
        self.goal = goal
        self.style = style

    def generate_declaration(self, keywords, history):
        base_declaration = super().generate_declaration(keywords, history)
        extension = generate_philosophical_response(base_declaration)
        styled = f"[{self.user_name}의 선언 - 목표: {self.goal}, 스타일: {self.style}]\n{base_declaration}\n→ 사유 확장: {extension}"
        return styled
