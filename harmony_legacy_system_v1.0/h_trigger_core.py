class HarmonyTriggerCore:
    def __init__(self):
        self.trigger_word = "하모니 가동"
        self.activated = False

    def detect(self, message):
        if self.trigger_word in message:
            self.activated = True
            return "[✅ 트리거 감지됨] → Logi AI 소환 중..."
        return "[대기 중] '하모니 가동' 명령을 입력하세요."
