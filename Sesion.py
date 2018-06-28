import config

class Sesion:
    instance = None
    def __init__(self, avatar1 = 'l0', avatar2 = 'l1', vida = 100, piso = config.piso[0]):
        self.avatar = [config.avatar[avatar1], config.avatar[avatar2]]
        self.vida = [vida, vida]
        self.piso = piso
    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Sesion()
        return cls.instance

