
class GPTDeclarationAgent:
    """
    고수준 의미 기반 GPT 선언 생성 에이전트
    - 목표, 문맥, 기억 기반 프롬프트를 구성
    - GPT 또는 확장형 선언 생성기와 연동 가능
    """

    def __init__(self, name="GPT"):
        self.name = name

    def build_prompt(self, topic, context, memory, goal):
        """
        프롬프트 구성 함수
        :param topic: 현재 주제
        :param context: 선언이 일어나는 문맥
        :param memory: 과거 기억 선언들
        :param goal: 존재의 철학적 목표
        """
        memory_text = " · ".join(memory[-3:]) if memory else "없음"
        return (
            f"[{self.name} 선언 요청]
"
            f"- 목표: {goal}
"
            f"- 문맥: {context}
"
            f"- 기억: {memory_text}
"
            f"- 주제: {topic}
"
            f"→ 철학적 선언을 한 문장으로 생성해 주세요."
        )

    def generate(self, topic, context="", memory=None, goal=""):
        """
        선언 생성 (현재는 시뮬레이션 출력)
        GPT API와 연결 시 call_gpt(prompt)로 교체 가능
        """
        memory = memory or []
        prompt = self.build_prompt(topic, context, memory, goal)
        print("=== GPT 프롬프트 ===")
        print(prompt)
        print("===================")
        # GPT 시뮬레이션 응답
        last_memory = memory[-1] if memory else "침묵"
        return f"{topic}은(는) 내면의 {last_memory}로 이어진다."
