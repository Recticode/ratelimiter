import time

class Clock:
    def __init__(self, actual: bool):
        self.actual = actual

    def current_time(self):
        if self.actual:
            return time.time()
        else:
            return 0