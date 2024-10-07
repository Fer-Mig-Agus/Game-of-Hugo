import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 630  # Aumentar 30px en la altura
pantalla = pygame.display.set_mode((ancho, alto))  # No se permite redimensionar
pygame.display.set_caption("Juega con Hugo")

# Cargar imágenes
fondo_inicio_original = pygame.image.load("fondo.jpg")
fondo_inicio = pygame.transform.scale(fondo_inicio_original, (ancho, alto))

fondo_juego_previo_original = pygame.image.load("screenPlay.jpg")
fondo_juego_previo = pygame.transform.scale(fondo_juego_previo_original, (ancho, alto))

fondo_juego_original = pygame.image.load("vias.PNG")
fondo_juego = pygame.transform.scale(fondo_juego_original, (ancho, alto))

# Cargar imágenes de Hugo y el vagón y redimensionar
hugo_imagen = pygame.image.load("hugo.png")
hugo_imagen = pygame.transform.scale(hugo_imagen, (25, 50))
vagon_imagen = pygame.image.load("vagon.png")
vagon_imagen = pygame.transform.scale(vagon_imagen, (50, 100))

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)

# Variables para la animación y el juego
fondo_y = 0
preguntas_realizadas = 0  # Estado inicial
acertadas = 0  # Estado inicial
errores = 0  # Estado inicial
vidas = 5  # Estado inicial
kilometros_recorridos = 0  # Estado inicial
contador_activo = False  # Para controlar el inicio del conteo de kilómetros
en_inicio = True
en_juego_previo = False
en_juego = False

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
    pantalla.blit(fondo_juego_previo, (0, 0))
    dibujar_boton("Jugar", ancho // 2 - 100, 300, 200, 50)
    dibujar_boton("Volver", ancho // 2 - 100, 400, 200, 50)
    pygame.display.flip()

# Función para manejar la animación
def animar_fondo():
    global fondo_y
    fondo_y += 2.5
    if fondo_y >= alto:
        fondo_y = 0

    pantalla.blit(fondo_juego, (0, fondo_y - alto))
    pantalla.blit(fondo_juego, (0, fondo_y))
    pantalla.blit(vagon_imagen, (ancho // 2 - 25, alto // 2 + 25))
    pantalla.blit(hugo_imagen, (ancho // 2 - 12.5, alto // 2 - 25))

# Función para dibujar la pantalla de juego
def dibujar_juego():
    global kilometros_recorridos
    animar_fondo()  # Dibuja la animación
    fuente = pygame.font.Font(None, 20)

    # Labels
    label_preguntas = fuente.render(f"Preguntas: {preguntas_realizadas}/20", True, negro)
    label_acertadas = fuente.render(f"Acertadas: {acertadas}", True, negro)
    label_errores = fuente.render(f"Erradas: {errores}", True, negro)
    label_vidas = fuente.render(f"Vidas: {'♥' * vidas}", True, negro)
    label_kilometros = fuente.render(f"Kilómetros: {kilometros_recorridos:.2f}", True, negro)

    # Dibujar los labels en la pantalla
    pantalla.blit(label_preguntas, (10, 10))
    pantalla.blit(label_acertadas, (10, 40))
    pantalla.blit(label_errores, (10, 70))
    pantalla.blit(label_vidas, (10, 100))
    pantalla.blit(label_kilometros, (10, 130))

    # Navbar
    dibujar_boton("Volver", ancho - 100, 10, 80, 30)  # Botón Volver en la navbar
    pygame.display.flip()

# Bucle principal del juego
clock = pygame.time.Clock()  # Para controlar el tiempo
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
                        #global contador_activo
                        contador_activo = True  # Activar el contador de kilómetros
                    elif pygame.Rect(ancho // 2 - 100, 400, 200, 50).collidepoint(mouse_pos):
                        en_inicio = True  # Regresa al menú
                        en_juego_previo = False  # Asegúrate de que no estemos en juego previo
                elif en_juego:
                    if pygame.Rect(ancho - 100, 10, 80, 30).collidepoint(mouse_pos):
                        en_juego = False  # Volver a la pantalla de juego previo
                        en_juego_previo = True  # Asegurarse de que estamos en la pantalla previa
                        fondo_y = 0  # Reiniciar la posición del fondo

    if en_inicio:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_menu(mouse_pos)
    elif en_juego_previo:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_juego_previo(mouse_pos)
    elif en_juego:
        if contador_activo:  # Solo actualizar kilómetros si el contador está activo
            kilometros_recorridos += 0.01  # Incrementar kilómetros por cada segundo
        dibujar_juego()
    
    # Controlar el tiempo
    clock.tick(60)  # Limitar a 60 FPS
