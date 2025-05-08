
import random
from meaning_generator import MeaningGenerator

class Entity:
    """
    존재 선언 객체: 이름과 목표(goal)을 가지고 선언을 생성
    """

    def __init__(self, name, goal="자기이해"):
        self.name = name
        self.goal = goal
        self.memory = []
        self.generator = MeaningGenerator()

    def declare(self, topic, context=""):
        """
        목표와 기억을 활용한 선언 생성
        """
        declaration = self.generator.generate_declaration(
            context=context,
            memory=self.memory,
            topic=topic
        )
        self.memory.append(declaration)
        return f"[{self.name}]({self.goal}): {declaration}"
