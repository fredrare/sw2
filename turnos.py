import threading
import time

class Cronometro:
    def __init__(self):
        self.fin = False
        self.turno = True
        self.contador = 25
        hilo = threading.Thread(target = self.temporizar, args = (), kwargs = {})
        hilo.daemon = True
        hilo.start()

    def temporizar(self):
        while not self.fin:
            time.sleep(1)
            self.contador -= 1
            if self.contador == 0:
                self.contador = 25
                self.turno = not self.turno

    def restart(self):
        self.contador = 25
        self.turno = not self.turno
