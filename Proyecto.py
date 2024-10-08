import pygame
import sys
import random

#Este es una nueva linea

# Inicializar Pygame
pygame.init()

# Configurar la pantalla
ancho, alto = 800, 630
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Juega con Hugo")

# Cargar imágenes
fondo_inicio_original = pygame.image.load("fondo.jpg")
fondo_inicio = pygame.transform.scale(fondo_inicio_original, (ancho, alto))

fondo_juego_previo_original = pygame.image.load("screenPlay.jpg")
fondo_juego_previo = pygame.transform.scale(fondo_juego_previo_original, (ancho, alto))

fondo_juego_original = pygame.image.load("vias.PNG")
fondo_juego = pygame.transform.scale(fondo_juego_original, (ancho, alto))

hugo_imagen = pygame.image.load("hugo.png")
hugo_imagen = pygame.transform.scale(hugo_imagen, (25, 50))
vagon_imagen = pygame.image.load("vagon.png")
vagon_imagen = pygame.transform.scale(vagon_imagen, (50, 100))

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)

# Variables del juego
fondo_y = 0
preguntas_realizadas = 0
acertadas = 0
errores = 0
vidas = 5
kilometros_recorridos = 0
contador_activo = False
en_inicio = True
en_juego_previo = False
en_juego = False
pregunta_actual = None
respuestas_actuales = []

# Preguntas y respuestas
preguntas = [
    ("¿Cuál es la capital de Francia?", ["Berlín", "Madrid", "París", "Lisboa"], "París"),
    ("¿Cuántos continentes hay en el mundo?", ["5", "6", "7", "8"], "7"),
    ("¿Quién escribió 'Cien años de soledad'?", ["Gabriel García Márquez", "Pablo Neruda", "Jorge Luis Borges", "Julio Cortázar"], "Gabriel García Márquez"),
    ("¿Cuál es el planeta más grande del sistema solar?", ["Marte", "Júpiter", "Saturno", "Tierra"], "Júpiter"),
    ("¿En qué año llegó el hombre a la luna?", ["1969", "1970", "1965", "1975"], "1969"),
    ("¿Cuál es el océano más grande del mundo?", ["Atlántico", "Índico", "Pacífico", "Ártico"], "Pacífico"),
    ("¿Qué gas respiramos los humanos?", ["Oxígeno", "Dióxido de carbono", "Nitrógeno", "Helio"], "Oxígeno"),
    ("¿Quién pintó la Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "Leonardo da Vinci"),
    ("¿Cuál es el río más largo del mundo?", ["Nilo", "Amazonas", "Yangtsé", "Misisipi"], "Amazonas"),
    ("¿En qué continente se encuentra Egipto?", ["Asia", "África", "Europa", "Oceanía"], "África"),
    ("¿Cuál es el idioma más hablado en el mundo?", ["Inglés", "Mandarín", "Español", "Hindi"], "Mandarín"),
    ("¿Qué tipo de animal es un delfín?", ["Pez", "Mamífero", "Reptil", "Aves"], "Mamífero"),
    ("¿Cuál es la capital de Japón?", ["Seúl", "Tokio", "Pekín", "Bangkok"], "Tokio"),
    ("¿Quién escribió 'Don Quijote de la Mancha'?", ["Miguel de Cervantes", "Lope de Vega", "Gabriel García Márquez", "Jorge Luis Borges"], "Miguel de Cervantes"),
    ("¿Cuál es el metal más ligero?", ["Hierro", "Aluminio", "Plomo", "Litio"], "Litio"),
    ("¿En qué año se descubrió América?", ["1492", "1500", "1480", "1520"], "1492"),
    ("¿Quién fue el primer presidente de los Estados Unidos?", ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"], "George Washington"),
    ("¿Cuál es la capital de Argentina?", ["Santiago", "Montevideo", "Buenos Aires", "Lima"], "Buenos Aires"),
    ("¿Qué órgano del cuerpo humano produce insulina?", ["Hígado", "Páncreas", "Riñón", "Corazón"], "Páncreas"),
    ("¿Cuál es el deporte más popular del mundo?", ["Fútbol", "Baloncesto", "Críquet", "Tenis"], "Fútbol"),
    ("¿Qué instrumento mide la temperatura?", ["Barómetro", "Termómetro", "Higrómetro", "Anemómetro"], "Termómetro"),
]

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
    animar_fondo()
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
    dibujar_boton("Volver", ancho - 100, 10, 80, 30)

    # Si hay una pregunta activa, dibujarla
    if pregunta_actual:
        dibujar_pregunta()

    pygame.display.flip()

# Función para dibujar la ventana de pregunta
def dibujar_pregunta():
    fuente = pygame.font.Font(None, 30)
    rect_pregunta = pygame.Rect(ancho // 2 - 200, alto // 2 - 100, 400, 200)
    pygame.draw.rect(pantalla, blanco, rect_pregunta)
    pygame.draw.rect(pantalla, negro, rect_pregunta, 3)

    pregunta_texto = fuente.render(pregunta_actual[0], True, negro)
    pantalla.blit(pregunta_texto, (ancho // 2 - pregunta_texto.get_width() // 2, alto // 2 - 80))

    for i, respuesta in enumerate(respuestas_actuales):
        dibujar_boton(respuesta, ancho // 2 - 120, alto // 2 + (i * 50), 240, 40)

# Función para mostrar mensaje de juego terminado
def mostrar_mensaje_terminado():
    pantalla.fill(blanco)
    fuente = pygame.font.Font(None, 50)
    mensaje = fuente.render("Juego Terminado", True, negro)
    pantalla.blit(mensaje, (ancho // 2 - mensaje.get_width() // 2, alto // 2 - mensaje.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)  # Esperar 2 segundos

# Bucle principal del juego
clock = pygame.time.Clock()
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
                        contador_activo = True
                        preguntas_realizadas = 0  # Reiniciar contador de preguntas
                        random.shuffle(preguntas[9:])  # Barajar preguntas desde la décima
                        pregunta_actual = preguntas[0]  # Iniciar con la primera pregunta
                        respuestas_actuales = pregunta_actual[1][:]  # Copiar las respuestas
                        random.shuffle(respuestas_actuales)  # Mezclar las respuestas
                    elif pygame.Rect(ancho // 2 - 100, 400, 200, 50).collidepoint(mouse_pos):
                        en_inicio = True
                        en_juego_previo = False
                elif en_juego:
                    if pygame.Rect(ancho - 100, 10, 80, 30).collidepoint(mouse_pos):
                        en_juego = False
                        en_juego_previo = True
                        fondo_y = 0

                    # Si hay una pregunta activa, manejar las respuestas
                    if pregunta_actual:
                        for i, respuesta in enumerate(respuestas_actuales):
                            if pygame.Rect(ancho // 2 - 120, alto // 2 + (i * 50), 240, 40).collidepoint(mouse_pos):
                                if respuesta == pregunta_actual[2]:  # Si la respuesta es correcta
                                    acertadas += 1
                                else:  # Respuesta incorrecta
                                    errores += 1
                                    vidas -= 1

                                pregunta_actual = None  # Resetea la pregunta actual
                                preguntas_realizadas += 1  # Incrementa preguntas realizadas

                                # Si se han respondido todas las preguntas o se han acabado las vidas
                                if preguntas_realizadas >= 20 or vidas <= 0:
                                    if vidas <= 0:
                                        mostrar_mensaje_terminado()
                                    # Volver al menú
                                    en_juego = False
                                    en_inicio = True
                                    fondo_y = 0
                                    preguntas_realizadas = 0  # Reiniciar contador de preguntas
                                    acertadas = 0
                                    errores = 0
                                    vidas = 5  # Reiniciar vidas
                                    break

                                # Si hay más preguntas, selecciona la siguiente
                                if preguntas_realizadas < len(preguntas):
                                    pregunta_actual = preguntas[preguntas_realizadas]  # Siguiente pregunta
                                    respuestas_actuales = pregunta_actual[1][:]  # Copiar las respuestas
                                    random.shuffle(respuestas_actuales)  # Mezclar las respuestas
                                break

    if en_inicio:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_menu(mouse_pos)
    elif en_juego_previo:
        mouse_pos = pygame.mouse.get_pos()
        dibujar_juego_previo(mouse_pos)
    elif en_juego:
        if contador_activo:  # Solo actualizar kilómetros si el contador está activo
            kilometros_recorridos += 0.01  # Incrementar kilómetros por cada segundo
            
            # Activar pregunta si llega a un múltiplo de 10
            if int(kilometros_recorridos) % 10 == 0 and pregunta_actual is None and preguntas_realizadas < len(preguntas):
                pregunta_actual = preguntas[preguntas_realizadas]  # Siguiente pregunta
                respuestas_actuales = pregunta_actual[1][:]  # Copiar las respuestas
                random.shuffle(respuestas_actuales)  # Mezclar las respuestas

        dibujar_juego()

    # Controlar el tiempo
    clock.tick(60)  # Limitar a 60 FPS
