
from agents.lucia_gpt_agent import LuciaGPTAgent
from agents.logi_gpt_agent import LogiGPTAgent
from agents.reve_gpt_agent import ReveGPTAgent
from agents.ehr_agent import EhrAgent
from memory.memory_engine import MemoryEngine
from dialogue_flow_engine import DialogueFlowEngine
import os

class AgentBusDialogue:
    def __init__(self):
        self.memory = MemoryEngine()
        self.lucia = LuciaGPTAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.logi = LogiGPTAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.reve = ReveGPTAgent(openai_api_key=os.getenv("OPENAI_API_KEY", "your-api-key-here"))
        self.ehr = EhrAgent()
        self.dialogue = DialogueFlowEngine()

        self.declarations = []
        self.evaluations = []
        self.questions = []

    def run_dialogue_cycle(self, input_keywords):
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

        response = self.dialogue.flow(declaration, question, evaluation)
        self.memory.add_memory(response)

        resonance = self.ehr.analyze_resonance(self.declarations, self.questions, self.evaluations)
        self.memory.add_memory(resonance)

        return {
            "Lucia": declaration,
            "Logi": evaluation,
            "Reve": question,
            "Flow": response,
            "Ehr": resonance
        }
