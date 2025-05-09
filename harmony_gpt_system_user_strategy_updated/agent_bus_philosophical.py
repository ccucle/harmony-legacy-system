
from agents.lucia_philosophical_agent import LuciaPhilosophicalAgent
from agents.logi_reflective_agent import LogiReflectiveAgent
from agents.reve_gpt_agent import ReveGPTAgent
from agents.ehr_agent import EhrAgent
from memory.memory_engine import MemoryEngine
import os

class AgentBusPhilosophical:
    def __init__(self):
        self.memory = MemoryEngine()
        self.lucia = LuciaPhilosophicalAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.logi = LogiReflectiveAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.reve = ReveGPTAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.ehr = EhrAgent()

        self.declarations = []
        self.evaluations = []
        self.questions = []

    def run_cycle(self, input_keywords):
        history = self.memory.recent_history()
        repeated = self.memory.check_repeated_keywords()

        declaration = self.lucia.generate_declaration(input_keywords, history)
        self.memory.add_memory(declaration)
        self.declarations.append(declaration)

        evaluation = self.logi.evaluate_declaration(declaration, history, repeated)
        self.memory.add_memory(evaluation)
        self.evaluations.append(evaluation)

        question = self.reve.generate_question(declaration, history)
        self.memory.add_memory(question)
        self.questions.append(question)

        resonance = self.ehr.analyze_resonance(self.declarations, self.questions, self.evaluations)
        self.memory.add_memory(resonance)

        return {
            "Lucia": declaration,
            "Logi": evaluation,
            "Reve": question,
            "Ehr": resonance
        }
