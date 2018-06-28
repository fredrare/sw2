import config

class Sesion:
    instance = None
    def __init__(self):
        self.avatar1 = config.avatar['l0']
        self.avatar2 = config.avatar['l1']
        self.piso = config.piso[1]
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Sesion()
        return cls.instance
