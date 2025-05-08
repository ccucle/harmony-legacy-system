import json

class Department:
    def __init__(self, name, subunits):
        self.name = name
        self.subunits = subunits

    def activate(self):
        print(f"[{self.name}] 부서 가동 중...")
        for sub in self.subunits:
            print(f"   └─ {sub} 활성화")

class HarmonyDepartmentSystem:
    def __init__(self, path="data/structure_map.json"):
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        self.departments = [
            Department(name, subs)
            for name, subs in data["부서"].items()
        ]

    def activate_all(self):
        for d in self.departments:
            d.activate()
