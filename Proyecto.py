import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto), pygame.RESIZABLE)
pygame.display.set_caption("Juega con Hugo")

# Cargar imágenes
fondo_inicio = pygame.image.load("fondo.jpg")
fondo_juego_original = pygame.image.load("vias.PNG")
fondo_juego = pygame.transform.scale(fondo_juego_original, (ancho, alto))

# Cargar imágenes de Hugo y el vagón y redimensionar
hugo_imagen = pygame.image.load("hugo.png")
hugo_imagen = pygame.transform.scale(hugo_imagen, (25, 50))
vagon_imagen = pygame.image.load("vagon.png")
vagon_imagen = pygame.transform.scale(vagon_imagen, (50, 100))

# Colores
negro = (0, 0, 0)

# Variables para la animación
fondo_y = 0
en_inicio = True
en_juego_previo = False
en_juego = False
animando = False

# Función para dibujar botones
def dibujar_boton(texto, pos_x, pos_y, ancho, alto, hover=False):
    fuente = pygame.font.Font(None, 30)
    rect_boton = pygame.Rect(pos_x, pos_y, ancho, alto)
    color_boton = (200, 200, 200) if hover else (150, 150, 150)
    pygame.draw.rect(pantalla, color_boton, rect_boton)
    pygame.draw.rect(pantalla, negro, rect_boton, 3)
    texto_renderizado = fuente.render(texto, True, negro)
    pantalla.blit(texto_renderizado, (pos_x + ancho // 2 - texto_renderizado.get_width() // 2, pos_y + alto // 2 - texto_renderizado.get_height() // 2))

# Función para dibujar la pantalla de inicio
def dibujar_menu(mouse_pos):
    pantalla.blit(fondo_inicio, (0, 0))
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

# Función para dibujar la pantalla de juego previo
def dibujar_juego_previo(mouse_pos):
    pantalla.fill((255, 255, 255))  # Limpiar pantalla con color blanco
    dibujar_boton("Jugar", ancho // 2 - 100, 300, 200, 50)
    dibujar_boton("Volver", ancho // 2 - 100, 400, 200, 50)
    pygame.display.flip()

# Función para manejar la animación
def animar_fondo():
    global fondo_y, animando
    fondo_y += 2.5
    if fondo_y >= alto:
        fondo_y = 0

    pantalla.blit(fondo_juego, (0, fondo_y - alto))
    pantalla.blit(fondo_juego, (0, fondo_y))
    pantalla.blit(vagon_imagen, (ancho // 2 - 25, alto // 2 + 25))
    pantalla.blit(hugo_imagen, (ancho // 2 - 12.5, alto // 2 - 25))
    pygame.display.flip()

# Función para dibujar la pantalla de juego
def dibujar_juego(mouse_pos):
    animar_fondo()  # Dibuja la animación
    fuente = pygame.font.Font(None, 15)
    
    # Labels
    label = fuente.render("Estadísticas: (0/0)", True, negro)
    pantalla.blit(label, (10, 10))
    
    # Botón de volver
    dibujar_boton("Volver", ancho - 100, 10, 80, 30)
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
                if en_inicio:
                    if pygame.Rect(ancho // 2 - 100, 200, 200, 50).collidepoint(mouse_pos):
                        en_inicio = False
                        en_juego_previo = True
                    elif pygame.Rect(ancho // 2 - 100, 500, 200, 50).collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                elif en_juego_previo:
                    if pygame.Rect(ancho // 2 - 100, 300, 200, 50).collidepoint(mouse_pos):
                        en_juego_previo = False
                        en_juego = True
                        animando = True
                    elif pygame.Rect(ancho // 2 - 100, 400, 200, 50).collidepoint(mouse_pos):
                        en_inicio = True  # Regresa al menú
                elif en_juego:
                    if pygame.Rect(ancho - 100, 10, 80, 30).collidepoint(mouse_pos):
                        en_juego = False  # Volver a la pantalla de juego previo
                        animando = False  # Detener la animación

    if en_inicio:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_menu(mouse_pos)
    elif en_juego_previo:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_juego_previo(mouse_pos)
    elif en_juego and animando:
        dibujar_juego(mouse_pos)
