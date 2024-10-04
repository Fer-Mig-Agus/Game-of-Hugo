import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 600
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juega con Hugo")

# Cargar imagen de fondo y redimensionar
fondo_original = pygame.image.load("fondo.jpg")  # Asegúrate de que la imagen esté en el mismo directorio
fondo = pygame.transform.scale(fondo_original, (ancho, alto))  # Redimensionar imagen al tamaño de la pantalla

# Colores
blanco = (255, 255, 255)

# Función para dibujar el menú
def dibujar_menu():
    fuente = pygame.font.Font(None, 74)
    texto_inicio = fuente.render("Inicio", True, (0, 0, 0))
    texto_puntajes = fuente.render("Puntajes", True, (0, 0, 0))
    texto_ayuda = fuente.render("Ayuda", True, (0, 0, 0))

    pantalla.blit(fondo, (0, 0))  # Dibujar fondo
    pantalla.blit(texto_inicio, (ancho // 2 - texto_inicio.get_width() // 2, 200))
    pantalla.blit(texto_puntajes, (ancho // 2 - texto_puntajes.get_width() // 2, 300))
    pantalla.blit(texto_ayuda, (ancho // 2 - texto_ayuda.get_width() // 2, 400))
    
    pygame.display.flip()  # Actualizar pantalla

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dibujar_menu()
