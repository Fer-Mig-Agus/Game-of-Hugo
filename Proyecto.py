import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto), pygame.RESIZABLE)  # Hacer la ventana ajustable
pygame.display.set_caption("Juega con Hugo")

# Cargar imagen de fondo y redimensionar
fondo_original = pygame.image.load("fondo.jpg")  # Asegúrate de que la imagen esté en el mismo directorio
fondo = pygame.transform.scale(fondo_original, (ancho, alto))  # Redimensionar imagen al tamaño de la pantalla

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (200, 200, 200)
gris_claro = (150, 150, 150)

# Función para dibujar botones
def dibujar_boton(texto, pos_x, pos_y, ancho, alto, hover=False):
    fuente = pygame.font.Font(None, 54)
    rect_boton = pygame.Rect(pos_x, pos_y, ancho, alto)
    
    # Cambiar color del botón si está en hover
    color_boton = gris_claro if hover else gris
    
    # Dibujar el botón
    pygame.draw.rect(pantalla, color_boton, rect_boton)  # Botón
    pygame.draw.rect(pantalla, negro, rect_boton, 3)  # Bordes en negro

    # Dibujar texto en el botón
    texto_renderizado = fuente.render(texto, True, negro)
    pantalla.blit(texto_renderizado, (pos_x + ancho // 2 - texto_renderizado.get_width() // 2, pos_y + alto // 2 - texto_renderizado.get_height() // 2))

# Función para dibujar el menú
def dibujar_menu(mouse_pos):
    global fondo  # Usar la imagen de fondo redimensionada
    pantalla.blit(fondo, (0, 0))  # Dibujar fondo

    # Definir posiciones de los botones
    botones = [
        (ancho // 2 - 100, 200, "Inicio"),
        (ancho // 2 - 100, 300, "Puntajes"),
        (ancho // 2 - 100, 400, "Ayuda")
    ]

    # Dibujar botones con efecto hover
    for pos_x, pos_y, texto in botones:
        hover = pygame.Rect(pos_x, pos_y, 200, 50).collidepoint(mouse_pos)  # Verificar si el mouse está sobre el botón
        dibujar_boton(texto, pos_x, pos_y, 200, 50, hover)

    pygame.display.flip()  # Actualizar pantalla

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Redimensionar la imagen de fondo si la ventana cambia de tamaño
    fondo = pygame.transform.scale(fondo_original, (pantalla.get_width(), pantalla.get_height()))

    # Obtener la posición del mouse
    mouse_pos = pygame.mouse.get_pos()

    dibujar_menu(mouse_pos)
