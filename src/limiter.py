from repository import Repository
from src.clock import Clock, FakeClock

class Limiter:
    def __init__(self, N: int, T: int, clock: Clock | FakeClock):
        self.repository = Repository()
        self.N = N
        self.T = T
        self.clock = clock

    # a request is allowed if the number of requests in the last T seconds is < N
    # “last T seconds” means: now - T < timestamp <= now

    def allow(self, user_id: int) -> bool:
        # check if the request is valid (using sliding window)
        user_data = self.repository.data.get(user_id, [])
        now = self.clock.now()
        window = []
        for timestamp in user_data:
            if now - self.T < timestamp <= now:
                window.append(timestamp)
        valid = len(window) < self.N
        if valid:
            window.append(now)
            self.repository.add(user_id, window)
        return valid