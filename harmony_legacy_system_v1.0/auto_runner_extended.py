
from entities import Entity
from event_listener import EventListener
from reinforcement_memory import ReinforcementMemory
from declaration_evolver import DeclarationEvolver

class AutoLoopRunnerExtended:
    def __init__(self, entity, event_listener, memory, evolver):
        self.entity = entity
        self.event_listener = event_listener
        self.memory = memory
        self.evolver = evolver

    def run_from_event(self, event_msg):
        topics = self.event_listener.receive(event_msg)
        print(f"Event 해석: {event_msg} -> 주제들: {topics}")

        for topic in topics:
            declaration = self.entity.declare(topic)
            print(f"선언: {declaration}")
            self.memory.add(declaration, score=1)
            self.evolver.add(declaration)

        evolved = self.evolver.evolve()
        print(f"최종 진화 선언: {evolved}")


# 예시 실행
if __name__ == "__main__":
    entity = Entity("Iris", goal="의식의 흐름 이해")
    listener = EventListener()
    memory = ReinforcementMemory()
    evolver = DeclarationEvolver()

    runner = AutoLoopRunnerExtended(entity, listener, memory, evolver)
    runner.run_from_event("그녀와의 이별 후 슬픔이 밀려왔다")
