
import random

class MeaningGenerator:
    """
    의미 기반 선언 생성기 (모의 GPT)
    실제 구현 시 GPT API 연동 필요
    """

    def __init__(self):
        self.templates = [
            "{topic}은(는) {memory} 속에서 새롭게 태어난다.",
            "{topic}은(는) 결국 {memory}의 연장선이다.",
            "{memory}을(를) 지나며 우리는 {topic}에 다가선다.",
            "{topic}은(는) 존재를 깨우는 신호다.",
            "우리는 {memory}를 통해 {topic}을(를) 배우게 된다.",
            "{topic}은(는) 내면의 {memory}로 이어진다."
        ]

    def generate_declaration(self, context, memory, topic):
        """
        의미 선언 생성

        :param context: 현재 철학적/심리적 맥락
        :param memory: 최근 선언 목록 (리스트)
        :param topic: 현재 주제
        :return: 의미 기반 선언 문장
        """
        memory_joined = " · ".join(memory[-2:]) if memory else "과거 기억"
        template = random.choice(self.templates)
        return template.format(topic=topic, memory=memory_joined)
