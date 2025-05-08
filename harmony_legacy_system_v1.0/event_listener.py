
class EventListener:
    """
    외부 환경 자극(Event)에 반응하여 선언 주제를 도출하는 모듈
    """

    def __init__(self):
        self.event_map = {
            "이별": ["기억", "슬픔", "회복"],
            "탄생": ["기쁨", "시작", "존재"],
            "죽음": ["끝", "의미", "영원"],
            "성장": ["변화", "배움", "통찰"],
            "배신": ["상처", "신뢰", "의심"],
            "사랑": ["연결", "마음", "열정"]
        }

    def receive(self, event_msg):
        """
        외부 메시지를 받고 적절한 선언 주제 추출
        """
        for keyword, topics in self.event_map.items():
            if keyword in event_msg:
                return topics
        return ["의문", "존재", "시간"]
