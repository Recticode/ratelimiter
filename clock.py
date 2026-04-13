import time

class Clock:
    def now(self) -> int:
        return int(time.time())

class FakeClock:
    def __init__(self, start_time: int=0):
       self.time = start_time

    def now(self) -> int:
        return self.time

    def set(self, new_time: int):
        self.time = new_time

    def advance(self, seconds: int):
        self.time += seconds