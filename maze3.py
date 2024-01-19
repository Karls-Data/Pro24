import readchar
import os

LABERINTO = [
    "###############################.......P.#######",
    "#............................#####..###########",
    "#.##......#######..####...###.........#########",
    "#.#......####.....####...##...######.......####",
    "#.##..###.....................########........#",
    "#.....######.......#.#########.........###..###",
    "#..#####......#################.........####.##",
    "#.....#..###...#########......#############.###",
    "#######.....#...############.......############",
    "##########..##...################.......#######",
    "################..........*####################"
]

MENSAJE_BIENVENIDA = "Bienvenido al juego de aventura"
MENSAJE_INGRESO_NOMBRE = "Ingresa tu nombre: "
MENSAJE_COMIENZO = "¡Comencemos!"
MENSAJE_ESPERA = "¡Entendido! Puedes comenzar cuando estés listo."
MENSAJE_NO_VALIDO = "Respuesta no válida. Por favor, responde 'Si' o 'No'."
MENSAJE_GANADOR = "¡Felicidades, has ganado el juego!"
MENSAJE_FIN_JUEGO = "¡Buen juego, perdedor!"


def imprimir_laberinto(lab):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la terminal
    for fila in lab:
        print(" ".join(fila))
    print()


def encontrar_posicion_inicial(lab):
    for i, fila in enumerate(lab):
        for j, celda in enumerate(fila):
            if celda == "P":
                return i, j
    return None


def mover_jugador(lab, fila, col, direccion):
    nueva_fila, nueva_col = fila, col
    if direccion == "arriba":
        nueva_fila -= 1
    elif direccion == "abajo":
        nueva_fila += 1
    elif direccion == "izquierda":
        nueva_col -= 1
    elif direccion == "derecha":
        nueva_col += 1

    if 0 <= nueva_fila < len(lab) and 0 <= nueva_col < len(lab[0]):
        if lab[nueva_fila][nueva_col] == "*":
            print(MENSAJE_GANADOR)
            exit()
        elif lab[nueva_fila][nueva_col] != "#":
            nuevo_laberinto = [list(fila) for fila in lab]
            nuevo_laberinto[fila][col] = "."
            nuevo_laberinto[nueva_fila][nueva_col] = "P"
            return ["".join(fila) for fila in nuevo_laberinto], nueva_fila, nueva_col
    return lab, fila, col


def solicitar_confirmacion():
    while True:
        ready = input("¿Estás listo para empezar? (Si / No): ").lower()
        if ready == "si":
            return True
        elif ready == "no":
            print(MENSAJE_ESPERA)
            return False
        else:
            print(MENSAJE_NO_VALIDO)


def actualizar_numero_y_limpiar_pantalla(numero):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la terminal
    print(f"Número actual: {numero}")


def main():
    global LABERINTO
    numero = 0

    print(MENSAJE_BIENVENIDA)
    nombre_jugador = input(MENSAJE_INGRESO_NOMBRE)
    print(f"¡Bienvenido, disfruta de esta gran aventura, {nombre_jugador}!")

    if not solicitar_confirmacion():
        return

    print(MENSAJE_COMIENZO)
    posicion_jugador = encontrar_posicion_inicial(LABERINTO)
    if posicion_jugador is None:
        print("No se pudo encontrar la posición inicial del jugador.")
        return

    fila_jugador, col_jugador = posicion_jugador
    imprimir_laberinto(LABERINTO)

    while True:
        key = readchar.readkey()

        if key == readchar.key.UP:
            direccion = "arriba"
        elif key == readchar.key.DOWN:
            direccion = "abajo"
        elif key == readchar.key.LEFT:
            direccion = "izquierda"
        elif key == readchar.key.RIGHT:
            direccion = "derecha"
        elif key == readchar.key.ESC:
            print(MENSAJE_FIN_JUEGO)
            break
        elif key == 'n':
            if numero < 50:
                numero += 1
            actualizar_numero_y_limpiar_pantalla(numero)
            continue

        LABERINTO, fila_jugador, col_jugador = mover_jugador(
            LABERINTO, fila_jugador, col_jugador, direccion)
        imprimir_laberinto(LABERINTO)


if __name__ == "__main__":
    main()
