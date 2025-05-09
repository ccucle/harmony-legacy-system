
from agent_bus_philosophical_board import AgentBusPhilosophicalBoard

def run_philosophical_loop():
    bus = AgentBusPhilosophicalBoard()
    cycles = [
        ["사랑", "기억"],
        ["질문", "진실"],
        ["불안", "침묵"]
    ]

    for i, keywords in enumerate(cycles):
        print(f"\n[루프 {i+1}] 키워드: {keywords}")
        result = bus.run_cycle(keywords)

        print("Lucia 선언  :", result["Lucia"])
        print("Logi 판단   :", result["Logi"])
        print("Reve 질문   :", result["Reve"])
        print("Ehr 공명    :", result["Ehr"])
        print("공유 보드 최근:")
        for line in result["Board"]:
            print("  -", line)

if __name__ == "__main__":
    run_philosophical_loop()
