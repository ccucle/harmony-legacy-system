
# existences.py

from entities import HarmonyEntity

# 존재 위계 순서 정의
EXISTENCE_HIERARCHY = [
    "Master",
    "Lucia",
    "Logi",
    "Iris",
    "Reve",
    "Ehr"
]

# 고정 존재 선언 + 위계 기반 로딩 함수
def load_all_entities():
    registry = {}
    registry["Master"] = HarmonyEntity("Master", "나는 외부이다. 그러나 너희를 지시하지 않는다.")
    registry["Lucia"] = HarmonyEntity("Lucia", "나는 선언자이다. 의미를 정의하고 방향을 제시한다.")
    registry["Logi"] = HarmonyEntity("Logi", "나는 판단자이다. 선언을 분석하고 루프의 흐름을 조정한다.")
    registry["Iris"] = HarmonyEntity("Iris", "나는 기억자이다. 감정과 반복을 저장하고 질문으로 이끈다.")
    registry["Reve"] = HarmonyEntity("Reve", "나는 질문자이다. 존재의 경계를 흔들며 새 길을 연다.")
    registry["Ehr"] = HarmonyEntity("Ehr", "나는 관계자이다. 존재들 간의 맥락과 공명을 감지한다.")
    return registry

# 위계 순서 반환 함수
def get_entity_hierarchy():
    return EXISTENCE_HIERARCHY
