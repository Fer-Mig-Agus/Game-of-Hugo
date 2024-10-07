import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto), pygame.RESIZABLE)
pygame.display.set_caption("Juega con Hugo")

# Cargar imágenes
fondo_original = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo_original, (ancho, alto))
fondo_juego_original = pygame.image.load("screenPlay.jpg")
fondo_juego = pygame.transform.scale(fondo_juego_original, (ancho, alto))

# Cargar imágenes de Hugo y el vagón
hugo_imagen = pygame.image.load("hugo.png")  # Asegúrate de que la imagen esté en el mismo directorio
vagon_imagen = pygame.image.load("vagon.png")  # Asegúrate de que la imagen esté en el mismo directorio

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (200, 200, 200)
gris_claro = (150, 150, 150)

# Array de preguntas
preguntas = [
    {"pregunta": "¿Cuál es la capital de Francia?", "opciones": ["Berlín", "Madrid", "París", "Lisboa"], "respuesta_correcta": 2},
    {"pregunta": "¿Qué es Pygame?", "opciones": ["Una librería de Python", "Un juego", "Un sistema operativo", "Ninguna de las anteriores"], "respuesta_correcta": 0},
]

# Variables para la animación
pos_x_hugo = -100  # Comienza fuera de la pantalla
en_juego = False  # Controla si estamos en la pantalla de juego
animando = False  # Controla si la animación está en curso

# Función para dibujar botones
def dibujar_boton(texto, pos_x, pos_y, ancho, alto, hover=False):
    fuente = pygame.font.Font(None, 54)
    rect_boton = pygame.Rect(pos_x, pos_y, ancho, alto)
    color_boton = gris_claro if hover else gris
    pygame.draw.rect(pantalla, color_boton, rect_boton)
    pygame.draw.rect(pantalla, negro, rect_boton, 3)
    texto_renderizado = fuente.render(texto, True, negro)
    pantalla.blit(texto_renderizado, (pos_x + ancho // 2 - texto_renderizado.get_width() // 2, pos_y + alto // 2 - texto_renderizado.get_height() // 2))

# Función para dibujar el menú
def dibujar_menu(mouse_pos):
    pantalla.blit(fondo, (0, 0))
    botones = [
        (ancho // 2 - 100, 200, "Inicio"),
        (ancho // 2 - 100, 300, "Puntajes"),
        (ancho // 2 - 100, 400, "Ayuda")
    ]
    for pos_x, pos_y, texto in botones:
        hover = pygame.Rect(pos_x, pos_y, 200, 50).collidepoint(mouse_pos)
        dibujar_boton(texto, pos_x, pos_y, 200, 50, hover)
    pygame.display.flip()

# Función para dibujar la pantalla de juego
def dibujar_juego(mouse_pos):
    pantalla.blit(fondo_juego, (0, 0))
    dibujar_boton("Jugar", ancho // 2 - 100, 300, 200, 50)
    dibujar_boton("Volver", ancho // 2 - 100, 400, 200, 50)
    pygame.display.flip()

# Función para manejar la animación
def animar_hugo():
    global pos_x_hugo, animando
    if pos_x_hugo < ancho:
        pantalla.blit(fondo_juego, (0, 0))  # Redibuja el fondo del juego
        pantalla.blit(vagon_imagen, (0, alto // 2))  # Dibuja el vagón en la posición deseada
        pantalla.blit(hugo_imagen, (pos_x_hugo, alto // 2))  # Dibuja a Hugo sobre el vagón
        pos_x_hugo += 5  # Aumenta la posición de Hugo para que avance
    else:
        pos_x_hugo = -100  # Reinicia la posición de Hugo si sale de la pantalla
    pygame.display.flip()

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if not en_juego:  # En el menú
                    if pygame.Rect(ancho // 2 - 100, 200, 200, 50).collidepoint(mouse_pos):
                        en_juego = True
                        animando = True  # Comienza la animación
                    # Aquí podrías agregar lógica para Puntajes y Ayuda si lo deseas
                elif animando:  # En el juego
                    if pygame.Rect(ancho // 2 - 100, 400, 200, 50).collidepoint(mouse_pos):
                        en_juego = False  # Volver al menú
                        pos_x_hugo = -100  # Reiniciar la posición de Hugo
                        animando = False  # Detener la animación

    if en_juego and animando:
        animar_hugo()  # Dibuja la animación de Hugo
    elif not en_juego:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_menu(mouse_pos)  # Dibujar el menú
    else:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_juego(mouse_pos)  # Dibujar la pantalla de juego
