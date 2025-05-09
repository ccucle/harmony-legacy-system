
from agents.lucia_goal_agent_time import LuciaGoalAgentWithTime
from agents.logi_reflective_agent_time import LogiReflectiveAgentWithTime
from agents.reve_gpt_agent_time import ReveGPTAgentWithTime
from agents.ehr_agent_time import EhrAgentWithTime
from memory.memory_engine import MemoryEngine
from memory.shared_declaration_board import SharedDeclarationBoard
from loop.loop_strategy_decider import LoopStrategyDecider

class UserStrategicAgentBus:
    def __init__(self):
        self.memory = MemoryEngine()
        self.board = SharedDeclarationBoard()

        self.lucia = LuciaGoalAgentWithTime(openai_api_key="your-api-key-here")
        self.logi = LogiReflectiveAgentWithTime(openai_api_key="your-api-key-here")
        self.reve = ReveGPTAgentWithTime(openai_api_key="your-api-key-here")
        self.ehr = EhrAgentWithTime()
        self.strategy = LoopStrategyDecider()

        self.declarations = []
        self.evaluations = []
        self.questions = []

    def run_user_query(self, user_input: str):
        keywords = [user_input]
        history = self.board.latest()
        repeated = self.memory.check_repeated_keywords()

        declaration = self.lucia.generate_declaration(keywords, history)
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

        strategy = self.strategy.decide(user_input, evaluation, resonance)

        return {
            "UserInput": user_input,
            "Lucia": declaration,
            "Logi": evaluation,
            "Reve": question,
            "Ehr": resonance,
            "Strategy": strategy,
            "Board": self.board.latest()
        }
