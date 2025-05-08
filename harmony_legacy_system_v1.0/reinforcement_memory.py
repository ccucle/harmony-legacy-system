
class ReinforcementMemory:
    """
    선언 강화 피드백 메모리
    각 선언에 대한 점수를 기반으로 진화 우선순위 제공
    """

    def __init__(self):
        self.memory = []

    def add(self, declaration, score=0):
        """
        선언과 그에 대한 점수 추가
        :param declaration: 선언 텍스트
        :param score: -1(부정), 0(중립), 1(긍정)
        """
        self.memory.append({"text": declaration, "score": score})

    def top_declarations(self, n=3):
        """
        점수 기준 상위 N개 선언 반환
        """
        sorted_mem = sorted(self.memory, key=lambda x: x["score"], reverse=True)
        return [entry["text"] for entry in sorted_mem[:n]]
