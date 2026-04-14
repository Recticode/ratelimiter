import json
import os

class Repository:
    def __init__(self):
        self.file_name = "../data.json"
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.file_name):
            return {}
        try:
            with open(self.file_name, "r") as file:
                content = file.read().strip()
                if not content:
                    return {}
                return json.loads(content)
        except json.JSONDecodeError:
            return {}

    def add(self, user_id, window: list[int]):
        self.data[user_id] = window

        with open(self.file_name, "w") as file:
            json.dump(self.data, file)