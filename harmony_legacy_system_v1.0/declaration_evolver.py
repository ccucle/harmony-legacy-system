
# declaration_evolver.py

class DeclarationEvolver:
    def __init__(self):
        self.base_declarations = []

    def add(self, declaration):
        self.base_declarations.append(declaration)

    def evolve(self):
        if not self.base_declarations:
            return "선언 없음"
        merged = " · ".join(self.base_declarations[-3:])
        return f"이 선언들은 하나의 흐름으로 진화됩니다: {merged}"
