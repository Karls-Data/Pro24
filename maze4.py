import readchar
import os

# Mensajes del juego
MENSAJE_BIENVENIDA = "Bienvenido al juego de aventura"
MENSAJE_INGRESO_NOMBRE = "Ingresa tu nombre: "
MENSAJE_COMIENZO = "¡Comencemos!"
MENSAJE_ESPERA = "¡Entendido! Puedes comenzar cuando estés listo."
MENSAJE_NO_VALIDO = "Respuesta no válida. Por favor, responde 'Si' o 'No'."
MENSAJE_GANADOR = "¡Felicidades, has escapado del laberinto!"
MENSAJE_FIN_JUEGO = "¡Buen juego, perdedor!"

# Convierte una cadena de texto a una matriz para el laberinto


def convertir_laberinto_en_matriz(texto_laberinto):
    return [list(fila) for fila in texto_laberinto.split("\n")]

# Imprime el laberinto en la consola


def imprimir_laberinto(lab):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la terminal
    for fila in lab:
        print(" ".join(fila))
    print()

# Verifica si el movimiento es válido dentro del laberinto


def es_movimiento_valido(lab, fila, col):
    return 0 <= fila < len(lab) and 0 <= col < len(lab[0]) and lab[fila][col] != '#'

# Limpia la terminal e imprime el número actual


def actualizar_numero_y_limpiar_pantalla(numero):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la terminal
    print(f"Número actual: {numero}")

# Solicita al jugador que comience el juego


def solicitar_inicio_juego():
    respuesta_listo = input("¿Estás listo para empezar? (Si / No): ").lower()
    while respuesta_listo not in ['si', 'no']:
        print(MENSAJE_NO_VALIDO)
        respuesta_listo = input(
            "¿Estás listo para empezar? (Si / No): ").lower()
    return respuesta_listo == 'si'

# La función principal del juego


def main():
    print(MENSAJE_BIENVENIDA)
    nombre_jugador = input(MENSAJE_INGRESO_NOMBRE)
    print(f"¡Hola, {nombre_jugador}!")

    if not solicitar_inicio_juego():
        print(MENSAJE_ESPERA)
        return

    # Aquí se coloca el texto del laberinto proporcionado anteriormente
    laberinto_texto = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

    LABERINTO = convertir_laberinto_en_matriz(laberinto_texto)
    px, py = 0, 0  # Posición inicial del jugador
    numero = 0
    imprimir_laberinto(LABERINTO)

    while True:
        key = readchar.readkey()

        # Actualizar número con tecla 'n'
        if key == 'n' and numero < 50:
            numero += 1
            actualizar_numero_y_limpiar_pantalla(numero)
            imprimir_laberinto(LABERINTO)
            continue

        nueva_px, nueva_py = px, py
        if key == readchar.key.UP:
            nueva_px -= 1
        elif key == readchar.key.DOWN:
            nueva_px += 1
        elif key == readchar.key.LEFT:
            nueva_py -= 1
        elif key == readchar.key.RIGHT:
            nueva_py += 1
        elif key == readchar.key.ESC:
            print(MENSAJE_FIN_JUEGO)
            break

        if es_movimiento_valido(LABERINTO, nueva_px, nueva_py):
            LABERINTO[px][py] = '.'
            px, py = nueva_px, nueva_py
            LABERINTO[px][py] = 'P'
        elif not es_movimiento_valido(LABERINTO, nueva_px, nueva_py) and (nueva_px, nueva_py) == (px, py):
            print(MENSAJE_GANADOR)
            break

        imprimir_laberinto(LABERINTO)


if __name__ == "__main__":
    main()
