# Juego de Laberinto ASCII - Documentación Completa

Autor: Karl Melendez
Fecha de Inicio: 11/02/2023
Fecha de Finalización: 11/09/2023

Introducción
El "Juego de Laberinto con Teclado" es un proyecto Python diseñado para navegar un personaje a través de un laberinto utilizando las teclas de flecha. Este juego es interactivo y basado en la terminal, empleando caracteres ASCII para la representación visual.

Características del Proyecto
Parte 2 (11/02/2023): Inicialmente, el juego consistía en un bucle infinito que leía e imprimía las teclas presionadas, terminando sólo al presionar la tecla de flecha hacia arriba.

Parte 3 (12/16/2023): Se incorporó la funcionalidad de iniciar con un contador en 0, incrementándolo con cada presión de la tecla 'n'. Se implementó la limpieza de la terminal para actualizar la visualización del contador.

Parte 4 (1/09/2024): Se transformó el juego en un laberinto navegable. Se introdujo una función para convertir una cadena de texto en una matriz que representa el laberinto. El jugador comienza en la posición (0,0) y el objetivo es llegar a la posición (len(mapa)-1, len(mapa[0])-1).

Instalación y Uso
Requisitos
Python 3.x
Librería readchar
Instalación de readchar
bash
Copy code
pip install readchar
Ejecución del Juego
Para jugar, ejecuta python maze_game.py en tu terminal. Navega en el laberinto con las teclas de flecha y utiliza 'n' para incrementar un contador.

Estructura y Funciones del Juego
Laberinto ASCII: Representado con '#', '.', y 'P' para paredes, espacios y el jugador, respectivamente.

Funciones Clave:

convertir_laberinto_en_matriz(texto_laberinto): Convierte una cadena de texto en una matriz de laberinto.
imprimir_laberinto(lab): Imprime el laberinto en la terminal.
es_movimiento_valido(lab, fila, col): Verifica si un movimiento es válido dentro del laberinto.
actualizar_numero_y_limpiar_pantalla(numero): Limpia la pantalla y muestra el número actualizado.
Juego Principal (main):

Inicia con la bienvenida y la posición inicial del jugador.
El bucle principal controla la navegación y el contador.
Pruebas y Control de Versión
Se implementaron pruebas unitarias para asegurar la funcionalidad del juego.
Se utilizó Git para el control de versiones, facilitando el seguimiento de cambios y colaboraciones.
Conclusiones y Aprendizaje
A lo largo del desarrollo de este juego, se aprendió sobre la manipulación de la terminal, la lectura de entradas del teclado, y la lógica de programación en Python para crear un juego interactivo. Este proyecto demuestra habilidades en programación Python y manejo de control de versiones con Git.
# Pro24
