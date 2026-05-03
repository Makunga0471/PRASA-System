class Database:
    _instance = None
    data = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)