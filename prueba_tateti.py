import unittest
from tateti import Tateti, PosOcupadaException

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti()

    def test_poner_ficha_posicion_libre(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.tablero.contenedor[0][0], "X")

    def test_posicion_ocupada_lanza_excepcion(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        with self.assertRaises(PosOcupadaException):
            self.juego.ocupar_una_de_las_casillas(0, 0)

    def test_cambio_de_turno(self):
        self.assertEqual(self.juego.turno, "X")
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "0")
        self.juego.ocupar_una_de_las_casillas(0, 1)
        self.assertEqual(self.juego.turno, "X")

    def test_ganar_fila(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  
        self.assertEqual(self.juego.ganador, "X")
    
    
    def test_empate(self):
        jugadas = [
            (0,0), (0,1),
            (0,2), (1,1),
            (1,0), (1,2),
            (2,1), (2,0),
            (2,2)
        ]  
        for f, c in jugadas:
            self.juego.ocupar_una_de_las_casillas(f, c)
     
        self.assertTrue(self.juego.empate)
        self.assertIsNone(self.juego.ganador)

    def test_no_se_puede_jugar_terminado(self):
        # Gana X
        self.juego.ocupar_una_de_las_casillas(0, 0)  
        self.juego.ocupar_una_de_las_casillas(1, 0)  
        self.juego.ocupar_una_de_las_casillas(0, 1)  
        self.juego.ocupar_una_de_las_casillas(1, 1)  
        self.juego.ocupar_una_de_las_casillas(0, 2)  

        with self.assertRaises(Exception) as e:
            self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertIn("terminó", str(e.exception))


if __name__ == '__main__':
    unittest.main()
