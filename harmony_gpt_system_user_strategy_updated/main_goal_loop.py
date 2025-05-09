
from agents.lucia_goal_agent import LuciaGoalAgent
from agents.logi_reflective_agent import LogiReflectiveAgent
from agents.reve_gpt_agent import ReveGPTAgent
from agents.ehr_agent import EhrAgent
from evolver.reinforced_evolver_eval import ReinforcedEvolverWithEvaluation
from memory.memory_engine import MemoryEngine

def run_goal_loop():
    lucia = LuciaGoalAgent(openai_api_key="your-api-key-here")
    logi = LogiReflectiveAgent(openai_api_key="your-api-key-here")
    reve = ReveGPTAgent(openai_api_key="your-api-key-here")
    ehr = EhrAgent()
    memory = MemoryEngine()
    evolver = ReinforcedEvolverWithEvaluation()

    signals = ["질문", "불안", "침묵", "사랑"]
    for i, k in enumerate(signals):
        history = memory.recent_history()
        repeated = memory.check_repeated_keywords()

        print(f"\n[루프 {i+1}] 키워드: {k}")
        declaration = lucia.generate_declaration([k], history)
        print("Lucia 선언:", declaration)
        memory.add_memory(declaration)
        evolver.add(declaration)

        evaluation = logi.evaluate_declaration(declaration, history, repeated)
        print("Logi 판단:", evaluation)
        memory.add_memory(evaluation)

        question = reve.generate_question(declaration, history)
        print("Reve 질문:", question)
        memory.add_memory(question)

        resonance = ehr.analyze_resonance([declaration], [question], [evaluation])
        print("Ehr 공명:", resonance)
        memory.add_memory(resonance)

    print("\n🌿 자기 목표 기반 진화 선언:")
    print(evolver.evolve())

if __name__ == "__main__":
    run_goal_loop()
