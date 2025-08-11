from tateti import Tateti, PosOcupadaException

def mostrar_tablero(tablero):
    for fila in tablero.contenedor:
        print(" | ".join(celda if celda != "" else " " for celda in fila))
        print("-" * 9)

def main():
    print("Bienvenidos al Tateti")
    juego = Tateti()

    while True:
        mostrar_tablero(juego.tablero)
        print(f"Turno: {juego.turno}")

        if juego.ganador:
            print(f"¡Ganó {juego.ganador}!")
            break

        if juego.empate:
            print("¡Empate!")
            break

        try:
            fil = int(input("Ingrese fila (0-2): "))
            col = int(input("Ingrese columna (0-2): "))
            juego.ocupar_una_de_las_casillas(fil, col)
        except PosOcupadaException as e:
            print(f"Error: {e}")
        except ValueError:
            print("Error: Por favor ingrese números válidos")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()
