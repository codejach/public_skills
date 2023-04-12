import os
from dontenv import load_dotenv

load_dotenv()

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    class Config(metaclass=Singleton):
        def __init__(self):
            self.config = {}

        def set(self, key, value):
            self.config[key] = value

        def get(self, key):
            return self.config[key]

        def get_all(self):
            return self.config
