# Juega con Hugo - Edición Pygame

Este es un juego en Python basado en el juego infantil "Juega con Hugo", desarrollado utilizando la biblioteca Pygame. El juego incluye un menú principal con botones, una pantalla jugable, y un sistema de preguntas y respuestas.

## Características

- **Ventana Redimensionable:** La ventana del juego se puede ajustar, manteniendo el diseño y los gráficos.
- **Menú:** Un menú principal con opciones para iniciar el juego, consultar puntajes (en futuras versiones) y obtener ayuda (en futuras versiones).
- **Modo de Juego:** El juego incluye una modalidad de preguntas y respuestas con estadísticas de respuestas correctas, errores y preguntas totales respondidas.
- **Opciones para Regresar:** El jugador puede volver al menú principal en cualquier momento desde la pantalla de juego.

## Instalación

1. Instalar Python 3.x desde [python.org](https://www.python.org/).
2. Instalar Pygame usando pip:

    ```bash
    pip install pygame
    ```

3. Clonar este repositorio y asegurarse de que las imágenes (`fondo.jpg` y `screenPlay.jpg`) estén en el mismo directorio que el script de Python.

## Cómo Jugar

1. Ejecuta el juego:

    ```bash
    python main.py
    ```

2. Aparecerá el menú principal, donde puedes:
   - Hacer clic en **Inicio** para comenzar el juego.
   - En futuras versiones, revisar los **Puntajes** o acceder a la **Ayuda**.

3. Durante el juego, verás una pantalla con una serie de preguntas.
   - Se registran las respuestas correctas e incorrectas, y puedes ver tu progreso.
   - Puedes volver al menú en cualquier momento haciendo clic en **Volver**.

## Resumen del Código

- **`main.py`**: El script principal del juego que maneja el bucle del juego, el menú y la mecánica dentro del juego.
- **Imágenes**: 
  - `fondo.jpg`: Imagen de fondo para la pantalla del menú.
  - `screenPlay.jpg`: Imagen de fondo para la pantalla del juego.
- **Preguntas**: Se incluye un pequeño conjunto de preguntas con opciones múltiples, y se pueden agregar más preguntas al array.

## Personalización

- Agrega más preguntas al array `preguntas`.
- Modifica o añade nuevo
