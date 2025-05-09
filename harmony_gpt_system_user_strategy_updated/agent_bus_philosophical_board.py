
from agents.lucia_philosophical_agent import LuciaPhilosophicalAgent
from agents.logi_reflective_agent import LogiReflectiveAgent
from agents.reve_gpt_agent import ReveGPTAgent
from agents.ehr_agent import EhrAgent
from memory.memory_engine import MemoryEngine
from memory.shared_declaration_board import SharedDeclarationBoard
import os

class AgentBusPhilosophicalBoard:
    def __init__(self):
        self.memory = MemoryEngine()
        self.board = SharedDeclarationBoard()

        self.lucia = LuciaPhilosophicalAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.logi = LogiReflectiveAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.reve = ReveGPTAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.ehr = EhrAgent()

        self.declarations = []
        self.evaluations = []
        self.questions = []

    def run_cycle(self, input_keywords):
        history = self.board.latest()
        repeated = self.memory.check_repeated_keywords()

        declaration = self.lucia.generate_declaration(input_keywords, history)
        self.memory.add_memory(declaration)
        self.board.post(declaration)
        self.declarations.append(declaration)

        evaluation = self.logi.evaluate_declaration(declaration, history, repeated)
        self.memory.add_memory(evaluation)
        self.board.post(evaluation)
        self.evaluations.append(evaluation)

        question = self.reve.generate_question(declaration, history)
        self.memory.add_memory(question)
        self.board.post(question)
        self.questions.append(question)

        resonance = self.ehr.analyze_resonance(self.declarations, self.questions, self.evaluations)
        self.memory.add_memory(resonance)
        self.board.post(resonance)

        return {
            "Lucia": declaration,
            "Logi": evaluation,
            "Reve": question,
            "Ehr": resonance,
            "Board": self.board.latest()
        }
