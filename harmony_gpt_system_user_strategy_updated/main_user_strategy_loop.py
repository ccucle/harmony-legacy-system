
from agent_bus_user_strategy import UserStrategicAgentBus

def run_user_strategic_loop():
    bus = UserStrategicAgentBus()
    user_inputs = [
        "나는 왜 불안한가?",
        "계획을 자꾸 미루는 이유는 뭘까?",
        "실행이 안 될 때 무엇이 필요한가?",
        "내가 반복되는 감정에 빠지는 이유는?"
    ]

    for i, question in enumerate(user_inputs):
        print(f"\n[루프 {i+1}] 사용자 질문: {question}")
        result = bus.run_user_query(question)

        print("Lucia 선언 :", result["Lucia"])
        print("Logi 판단 :", result["Logi"])
        print("Reve 질문 :", result["Reve"])
        print("Ehr 공명  :", result["Ehr"])
        print("선택된 전략:", result["Strategy"])

        print("공유 보드 최근:")
        for line in result["Board"]:
            print(" -", line)

if __name__ == "__main__":
    run_user_strategic_loop()
