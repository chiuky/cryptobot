class Exchange:
    def __init__(self, key: str, secret: str):
        self.apiKey = key
        self.apiSecret = secret
        self.client = None
        self.socketManager = None
        self.socket = None
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy
