
import random

class GPTDeclarationAgent:
    """
    GPT 기반 선언 생성 에이전트 (모의 버전)
    실제 사용 시 OpenAI API로 연결
    """

    def __init__(self, name="GPT"):
        self.name = name

    def generate(self, topic, context="", memory=None):
        """
        의미 기반 프롬프트 구성 후 선언 생성
        """
        memory = memory or []
        prompt = f"{self.name}는 다음 주제에 대한 선언을 생성합니다.\n" \
                 f"주제: {topic}\n" \
                 f"문맥: {context}\n" \
                 f"기억: {' · '.join(memory[-3:]) if memory else '없음'}"

        # 모의 응답
        return f"{topic}은(는) {random.choice(['존재의 울림이다.', '내면으로 흐른다.', '새로운 시작이다.', '끝없는 여정이다.'])}"
