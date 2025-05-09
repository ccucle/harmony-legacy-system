
def generate_self_reflection(declaration: str, evaluation: str) -> str:
    if "충돌" in evaluation:
        return "나는 왜 선언이 흐름과 충돌했는지 성찰한다."
    elif "일치" in evaluation or "조화" in evaluation:
        return "나는 선언이 흐름과 일치한 이유를 되새긴다."
    elif "불확실" in evaluation:
        return "나는 선언이 명확하지 않은 이유를 되묻는다."
    else:
        return "나는 이 선언의 근원을 다시 바라본다."
