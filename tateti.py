from tablero import Tablero, PosOcupadaException

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
        self.ganador = None
        self.empate = False

    def ocupar_una_de_las_casillas(self, fil, col):
        if self.ganador or self.empate:
            raise Exception("El juego ya terminó")

        self.tablero.poner_la_ficha(fil, col, self.turno)

        
        if self.tablero.hay_ganador(self.turno):
            self.ganador = self.turno
            return

      
        if self.tablero.esta_lleno():
            self.empate = True
            return

        self.turno = "0" if self.turno == "X" else "X"

    def reiniciar(self):
        self.tablero.limpiar()
        self.turno = "X"
        self.ganador = None
        self.empate = False
