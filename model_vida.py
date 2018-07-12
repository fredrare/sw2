import turnos
import config

class ModelVida:
    def __init__(self, x1, x2):
        self.x = [x1 + 50, x2 + 50]
        self.cronometro = turnos.Cronometro.get_instance()

    def update(self, x1, x2):
        self.x = [x1 + 50, x2 + 50]

    def colision(self, x1, y1, x2, y2):
        self.balas = [{'x': x1 + 50, 'y': y1 + 50}, {'x': x2 + 50, 'y': y2 + 50}]
        turno = 0 if self.cronometro.turno else 1
        alto = config.ALTO - 100
        if (self.balas[turno]['x'] < self.x[1 - turno] + 25) and (self.balas[turno]['x'] > self.x[1 - turno] - 25):
            if (self.balas[turno]['y'] < alto + 25) and (self.balas[turno]['y'] > alto - 25):
                damage = float(800 * 25 / (self.balas[turno]['x'] ** 2 + self.balas[turno]['y'] ** 2) ** (0.5))
                print self.x[1 - turno], self.balas[turno]['x'], self.balas[turno]['y']
                print 'damage:', damage
                return damage
        return 0

