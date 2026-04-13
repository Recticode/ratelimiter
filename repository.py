import json
import os
from models import Request

class Repository:
    def __init__(self):
        self.file_name = "data.json"
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

    def add(self, request: Request):
        # add to self.data
        # save self.data onto json file
        pass