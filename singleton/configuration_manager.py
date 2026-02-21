import threading


class ConfigurationManager:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("Creating ConfigurationManager instance...")
                    cls._instance = super().__new__(cls)
                    cls._instance.settings = {}
        return cls._instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        if key in self.settings:
            return self.settings[key]
        raise Exception(f"Setting '{key}' not found")

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            for key, value in self.settings.items():
                file.write(f"{key}={value}\n")

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                key, value = line.strip().split("=")
                self.settings[key] = value
