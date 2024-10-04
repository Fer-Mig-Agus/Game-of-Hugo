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

# Cargar fondo de la pantalla de juego
fondo_juego_original = pygame.image.load("screenPlay.png")  # Asegúrate de que la imagen esté en el mismo directorio
fondo_juego = pygame.transform.scale(fondo_juego_original, (ancho, alto))

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (200, 200, 200)
gris_claro = (150, 150, 150)

# Array de preguntas
preguntas = [
    {"pregunta": "¿Cuál es la capital de Francia?", "opciones": ["Berlín", "Madrid", "París", "Lisboa"], "respuesta_correcta": 2},
    {"pregunta": "¿Qué es Pygame?", "opciones": ["Una librería de Python", "Un juego", "Un sistema operativo", "Ninguna de las anteriores"], "respuesta_correcta": 0},
    # Agrega más preguntas aquí
]

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

# Función para dibujar la pantalla de juego
def dibujar_juego():
    pantalla.blit(fondo_juego, (0, 0))  # Dibujar fondo de juego

    # Mostrar estadísticas
    fuente = pygame.font.Font(None, 54)
    preguntas_label = fuente.render("Preguntas (1/20)", True, negro)
    errores_label = fuente.render("Errores (0)", True, negro)
    acertados_label = fuente.render("Acertados (1)", True, negro)

    pantalla.blit(preguntas_label, (50, 50))
    pantalla.blit(errores_label, (50, 120))
    pantalla.blit(acertados_label, (50, 190))

    # Dibujar botón de inicio
    dibujar_boton("Start", ancho // 2 - 100, 300, 200, 50)

    pygame.display.flip()  # Actualizar pantalla

# Bucle principal del juego
en_juego = False  # Variable para controlar si estamos en la pantalla de juego

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Verificar si se hizo clic con el botón izquierdo del ratón
                mouse_pos = pygame.mouse.get_pos()
                
                if not en_juego:
                    # Comprobar si se presionó el botón "Inicio"
                    if pygame.Rect(ancho // 2 - 100, 200, 200, 50).collidepoint(mouse_pos):
                        en_juego = True  # Cambiar a la pantalla de juego

    # Redimensionar la imagen de fondo si la ventana cambia de tamaño
    fondo = pygame.transform.scale(fondo_original, (pantalla.get_width(), pantalla.get_height()))
    fondo_juego = pygame.transform.scale(fondo_juego_original, (pantalla.get_width(), pantalla.get_height()))

    if en_juego:
        dibujar_juego()  # Dibujar la pantalla de juego
    else:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_menu(mouse_pos)  # Dibujar el menú
