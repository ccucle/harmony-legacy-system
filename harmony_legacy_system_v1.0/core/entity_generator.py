class Entity:
    def __init__(self, name, role, traits):
        self.name = name
        self.role = role
        self.traits = traits
        print(f"[🧬 인재 창조] {self.name} ({self.role}) → {self.traits}")

class EntityGenerator:
    def create(self, goal):
        templates = {
            "감정": ("EmpathDesigner", ["공감형", "감정해석"]),
            "수익": ("FlowSeeker_SEO", ["전환", "키워드"]),
            "글쓰기": ("StoryCrafter", ["감성", "문장"]),
        }
        for k, (name, traits) in templates.items():
            if k in goal:
                yield Entity(name + "_1", k + " 담당", traits)
