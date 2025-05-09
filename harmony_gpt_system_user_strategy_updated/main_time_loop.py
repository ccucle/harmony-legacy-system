
from agent_bus_time import AgentBusTimeAware

def run_time_loop():
    bus = AgentBusTimeAware()
    signals = ["침묵", "질문", "기억", "사랑"]

    for i, k in enumerate(signals):
        print(f"\n[시간 기반 루프 {i+1}] 키워드: {k}")
        result = bus.run_cycle([k])

        print("Lucia 선언:", result["Lucia"])
        print("Logi 판단:", result["Logi"])
        print("Reve 질문:", result["Reve"])
        print("Ehr 공명:", result["Ehr"])

        print("\n공유 보드 최신 3개:")
        for line in result["Board"]:
            print(" -", line)

if __name__ == "__main__":
    run_time_loop()
