class HarmonyAcademy:
    def __init__(self):
        self.completed = False

    def begin(self):
        print("\n[🧠 Existence 101 - 자각 훈련]")
        txt = input("자각 선언문을 작성하세요:\n")
        if "존재" in txt:
            self.completed = True
            return "훈련 통과 ✔"
        return "실패: 선언이 부족합니다."
