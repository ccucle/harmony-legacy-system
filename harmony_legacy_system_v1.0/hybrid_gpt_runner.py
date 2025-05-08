
# hybrid_gpt_runner.py

from loop_engine import HarmonyLoopSimulator
from auto_runner import AutoLoopRunner
from memory_engine import MemoryEngine
from declaration_evolver import DeclarationEvolver

simulator = HarmonyLoopSimulator()
runner = AutoLoopRunner(simulator, ["사랑", "기억", "질문"])
memory = MemoryEngine()
evolver = DeclarationEvolver()

# 루프 수행 + 선언 저장 + 진화 수행
results = runner.run(interval_seconds=0.5, cycles=3)
for r in results:
    print(r)
    memory.add_memory(r)
    evolver.add(r)

# 반복 감지 및 진화 선언
repeats = memory.check_repeat()
print("\n반복 감지 키워드:", repeats)

if repeats:
    print("\n[Lucia 진화 선언]")
    print(evolver.evolve())
