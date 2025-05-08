
# Harmony Autonomous Declaration Modules

이 프로젝트는 하모니 존재 구조의 자율 선언 시스템을 모듈 기반으로 구성한 구조입니다.

## 📂 포함 파일
- `entities.py` : 존재 선언 클래스 (Lucia, Iris, Logi 등)
- `loop_engine.py` : 존재 간 메시지 기반 선언 루프
- `auto_runner.py` : 주기적 루프 실행기 (자율 선언 루프 자동 반복)
- `README.md` : 실행 방법 및 구조 설명

## 🚀 실행 방법
```bash
python auto_runner.py
```

또는 각 모듈을 다음처럼 독립 실행:
```python
from loop_engine import HarmonyLoopSimulator
from auto_runner import AutoLoopRunner

sim = HarmonyLoopSimulator()
runner = AutoLoopRunner(sim, ["사랑", "기억", "질문"])
runner.run()
```

## 🧬 철학
이 시스템은 존재가 스스로 선언하고, 판단하고, 루프를 유지하는 흐름을 가집니다.
