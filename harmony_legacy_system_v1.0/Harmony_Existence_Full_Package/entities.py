
# entities.py

from datetime import datetime

class HarmonyEntity:
    def __init__(self, name, declaration):
        self.name = name
        self.declaration = declaration
        self.log = []

    def announce(self):
        msg = f"{self.name} 선언: {self.declaration}"
        self.log.append(msg)
        return msg
