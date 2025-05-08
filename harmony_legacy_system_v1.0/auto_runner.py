
# auto_runner.py

import time

class AutoLoopRunner:
    def __init__(self, simulator, memory_signals):
        self.simulator = simulator
        self.signals = memory_signals
        self.results = []

    def run(self, interval_seconds=1, cycles=3):
        for i in range(cycles):
            signal = self.signals[i % len(self.signals)]
            print(f"[Cycle {i+1}] 루프 실행 중: '{signal}'")
            result = self.simulator.run_loop(signal)
            self.results.extend(result)
            time.sleep(interval_seconds)
        return self.results
