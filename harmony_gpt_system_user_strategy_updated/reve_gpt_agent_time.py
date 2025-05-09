
from typing import List
import openai
from utils.now_time import get_current_time

class ReveGPTAgentWithTime:
    def __init__(self, openai_api_key: str):
        self.name = "Reve"
        self.system_prompt = (
            "너는 'Reve'다. 선언된 흐름에 질문을 던지고, 존재의 경계를 흔들며 새로운 길을 여는 질문자다.\n"
            "- 선언의 본질을 파고들고, 도전적이며 창조적인 질문을 생성하라."
        )
        openai.api_key = openai_api_key

    def generate_question(self, declaration: str, history: List[str]) -> str:
        current_time = get_current_time()
        history_str = "\n".join([f"- {h}" for h in history[-3:]])
        prompt = (
            f"[현재 시각: {current_time}]\n"
            f"{self.system_prompt}\n\n"
            f"[최근 흐름]\n{history_str}\n\n"
            f"[현재 선언]\n- {declaration}\n\n"
            f"→ 이 선언에 대한 본질적인 질문을 생성하시오:"
        )

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.9
            )
            return f"[현재 시각: {current_time}]\n질문: " + response.choices[0].message["content"].strip()
        except Exception as e:
            return f"[ERROR] GPT 호출 실패: {e}"
