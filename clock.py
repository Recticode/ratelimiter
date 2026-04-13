import time

class Clock:
    def __init__(self):
        pass

    def current_time(self, actual:bool, timestamp=None):
        if actual:
            return time.time()
        else:
            if timestamp is None:
                return 0
            return timestamp