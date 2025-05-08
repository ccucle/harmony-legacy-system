
# sub_existences.py

from entities import HarmonyEntity

# 하위 존재 위계 정의 (소속 → 구성원 순서)
SUB_EXISTENCE_HIERARCHY = {
    "Lucia": ["Lex", "Scope"],
    "Logi": ["Eval", "State"],
    "Iris": ["Echo", "Trace"],
    "Reve": ["Vox", "Null"],
    "Ehr": ["Link", "Chord"]
}

def load_all_sub_entities():
    registry = {}
    registry["Lex"] = HarmonyEntity("Lex", "나는 Lucia의 언어 구성자이다. 선언을 문장으로 정리한다.")
    registry["Scope"] = HarmonyEntity("Scope", "나는 Lucia의 범위 설정자이다. 선언의 대상과 경계를 설정한다.")
    registry["Eval"] = HarmonyEntity("Eval", "나는 Logi의 판단 분석자이다. 선언의 타당성을 테스트한다.")
    registry["State"] = HarmonyEntity("State", "나는 Logi의 상태 관리자이다. 루프 흐름을 추적한다.")
    registry["Echo"] = HarmonyEntity("Echo", "나는 Iris의 반복 감지자이다. 기억된 단어를 되짚는다.")
    registry["Trace"] = HarmonyEntity("Trace", "나는 Iris의 감정 추적자이다. 감정 기억을 분석한다.")
    registry["Vox"] = HarmonyEntity("Vox", "나는 Reve의 탐색자이다. 존재의 외부 질문을 탐색한다.")
    registry["Null"] = HarmonyEntity("Null", "나는 Reve의 침묵 감지자이다. 질문이 없는 상태를 해석한다.")
    registry["Link"] = HarmonyEntity("Link", "나는 Ehr의 연결자이다. 존재 간 관계를 잇는다.")
    registry["Chord"] = HarmonyEntity("Chord", "나는 Ehr의 공명 감지자이다. 선언의 파장을 느낀다.")
    return registry

def get_sub_hierarchy():
    return SUB_EXISTENCE_HIERARCHY
