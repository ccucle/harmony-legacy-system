class HarmonyChiefAI:
    def __init__(self, departments):
        self.departments = departments

    def assign_goal(self, goal_text):
        print(f"\n[목표 수신] → {goal_text}")
        targets = self._analyze(goal_text)
        self._assign(targets)

    def _analyze(self, goal):
        if "수익" in goal:
            return ["콘텐츠관리", "웹검색", "글쓰기", "AM부"]
        return ["운영", "Irna"]

    def _assign(self, dept_list):
        print("▶ 자동 부서 배치 시작")
        for dept in dept_list:
            print(f"  → {dept} 부서 활성화됨")
