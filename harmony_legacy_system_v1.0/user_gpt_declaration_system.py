
class UserGPTDeclarationSystem:
    """
    사용자 전용 선언 흐름 시스템
    - 사용자의 이름, 철학, 주제 흐름, 기억, 목표 등을 반영하여
      완전 맞춤형 선언 생성 흐름을 구성
    """

    def __init__(self, user_name="User", goal="진정한 자기표현", style="철학적"):
        self.user_name = user_name
        self.goal = goal
        self.style = style
        self.memory = []

    def build_prompt(self, topic, context):
        memory_text = " · ".join(self.memory[-3:]) if self.memory else "없음"
        return (
            f"[{self.user_name} 선언 생성 요청]
"
            f"- 목표: {self.goal}
"
            f"- 스타일: {self.style}
"
            f"- 문맥: {context}
"
            f"- 기억: {memory_text}
"
            f"- 주제: {topic}
"
            f"→ 이 기준에 맞는 선언을 한 문장으로 생성하세요."
        )

    def generate_declaration(self, topic, context=""):
        prompt = self.build_prompt(topic, context)
        print("=== 사용자 맞춤 프롬프트 ===")
        print(prompt)
        print("==========================")
        last_memory = self.memory[-1] if self.memory else "내면의 침묵"
        declaration = f"{topic}은(는) {last_memory}에 닿는 울림이다."
        self.memory.append(declaration)
        return declaration
