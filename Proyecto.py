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

# Cargar imágenes de Hugo y el vagón y redimensionar
hugo_imagen = pygame.image.load("hugo.png")
hugo_imagen = pygame.transform.scale(hugo_imagen, (25, 50))  # Redimensionar a 25px x 50px
vagon_imagen = pygame.image.load("vagon.png")
vagon_imagen = pygame.transform.scale(vagon_imagen, (50, 100))  # Redimensionar a 50px x 100px

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
fondo_y = 0  # Posición inicial del fondo
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
        (ancho // 2 - 100, 400, "Ayuda"),
        (ancho // 2 - 100, 500, "Salir")
    ]
    for pos_x, pos_y, texto in botones:
        hover = pygame.Rect(pos_x, pos_y, 200, 50).collidepoint(mouse_pos)
        dibujar_boton(texto, pos_x, pos_y, 200, 50, hover)
    pygame.display.flip()

# Función para dibujar la pantalla de juego
def dibujar_juego(mouse_pos):
    # Dibujar el fondo del juego
    pantalla.fill(blanco)  # Limpiar pantalla con color blanco
    dibujar_boton("Jugar", ancho // 2 - 100, 300, 200, 50)
    dibujar_boton("Volver", ancho // 2 - 100, 400, 200, 50)
    pygame.display.flip()

# Función para manejar la animación
def animar_fondo():
    global fondo_y, animando
    fondo_y += 5  # Mueve el fondo hacia arriba
    if fondo_y >= alto:  # Si el fondo se ha movido completamente
        fondo_y = 0  # Reinicia la posición

    # Dibujar el fondo desplazándose
    pantalla.blit(fondo, (0, fondo_y - alto))  # Parte superior
    pantalla.blit(fondo, (0, fondo_y))  # Parte inferior

    # Dibujar el vagón y a Hugo en el centro
    pantalla.blit(vagon_imagen, (ancho // 2 - 25, alto // 2 + 25))  # Dibujar el vagón en el medio
    pantalla.blit(hugo_imagen, (ancho // 2 - 12.5, alto // 2 - 25))  # Dibujar a Hugo en el medio
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
                    elif pygame.Rect(ancho // 2 - 100, 500, 200, 50).collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()  # Cierra el juego
                elif animando:  # En el juego
                    if pygame.Rect(ancho // 2 - 100, 400, 200, 50).collidepoint(mouse_pos):
                        en_juego = False  # Volver al menú
                        fondo_y = 0  # Reiniciar la posición del fondo
                        animando = False  # Detener la animación

    if en_juego and animando:
        animar_fondo()  # Dibuja la animación del fondo
    elif not en_juego:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_menu(mouse_pos)  # Dibujar el menú
    else:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_juego(mouse_pos)  # Dibujar la pantalla de juego

