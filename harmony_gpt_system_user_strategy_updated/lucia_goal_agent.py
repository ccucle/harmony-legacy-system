
from agents.lucia_gpt_agent import LuciaGPTAgent
from philosophical_response_generator import generate_philosophical_response
from self_goal_agent import generate_goal

class LuciaGoalAgent(LuciaGPTAgent):
    def __init__(self, openai_api_key: str, user_name="Lucia", style="철학적"):
        super().__init__(openai_api_key)
        self.user_name = user_name
        self.style = style
        self.goal = generate_goal()  # 자기 목표 생성

    def generate_declaration(self, keywords, history):
        base = super().generate_declaration(keywords, history)
        extension = generate_philosophical_response(base)
        declaration = f"[{self.user_name}의 선언 - 목표: {self.goal}, 스타일: {self.style}]\n{base}\n→ 사유 확장: {extension}"
        return declaration
