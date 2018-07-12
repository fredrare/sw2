import threading
import time
import obtener_datos

class Cronometro:
    instance = None
    def __init__(self):
        self.fin = False
        self.turno = True
        self.tiempo = int(obtener_datos.obtener_tiempo_actual())
        print(self.tiempo)
        self.contador = self.tiempo
        hilo = threading.Thread(target = self.temporizar, args = (), kwargs = {})
        hilo.daemon = True
        hilo.start()

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Cronometro()
        return cls.instance

    def temporizar(self):
        while not self.fin:
            time.sleep(1)
            self.contador -= 1
            if self.contador == 0:
                self.restart()

    def restart(self):
        self.contador = self.tiempo
        self.turno = not self.turno
