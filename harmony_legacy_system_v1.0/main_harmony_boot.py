from h_trigger_core import HarmonyTriggerCore
from core.logi_core import LogiAI

def run_harmony_system():
    print("🧭 하모니 시스템 초기 대기 중...")
    trigger = HarmonyTriggerCore()

    while True:
        cmd = input("\n[입력] ▶ ")
        result = trigger.detect(cmd)
        print(result)

        if trigger.activated:
            break

    logi = LogiAI()
    print(logi.initiate_loop())

if __name__ == "__main__":
    run_harmony_system()
