import pygame
from Constantes import *
from Preguntas import *
from Funciones import *

pygame.init()

#fondo
fondo = pygame.image.load("fondo_juego.jpg")
fondo = pygame.transform.scale(fondo, VENTANA)

# Carga de imagenes para las preguntas
IMAGEN_PREGUNTA = pygame.image.load("imagen_pregunta.png")
IMAGEN_PREGUNTA = pygame.transform.scale(IMAGEN_PREGUNTA, TAMAÑO_PREGUNTA)

# Carga de imágenes para las respuestas
IMAGEN_BLANCA = pygame.image.load("boton_respuesta.png")
IMAGEN_VERDE = pygame.image.load("boton_correcta.png")
IMAGEN_ROJA = pygame.image.load("boton_incorrecta.png")

# Escalado de las imágenes al tamaño de las respuestas
IMAGEN_BLANCA = pygame.transform.scale(IMAGEN_BLANCA, TAMAÑO_RESPUESTA)
IMAGEN_VERDE = pygame.transform.scale(IMAGEN_VERDE, TAMAÑO_RESPUESTA)
IMAGEN_ROJA = pygame.transform.scale(IMAGEN_ROJA, TAMAÑO_RESPUESTA)

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

cartas_respuestas = []
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = IMAGEN_BLANCA.copy()  # Usa la imagen blanca como fondo inicial
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

fuente_pregunta = pygame.font.SysFont("qatar-2022-book", 30)
fuente_respuesta = pygame.font.SysFont("qatar-2022-book", 23)
fuente_texto = pygame.font.SysFont("qatar-2022-book", 25)
mezclar_lista(lista_preguntas)
indice = 0  # INMUTABLE -> En la funcion las declaro como global
bandera_respuesta = False  # INMUTABLE -> En la funcion las declaro como global


def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice
    global bandera_respuesta

    retorno = "juego"

    cuadro_pregunta["superficie"].blit(IMAGEN_PREGUNTA, (0, 0))


    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False

    pregunta_actual = lista_preguntas[indice]

    # Reinicia las superficies de las respuestas a su estado inicial (blanco)
    for carta in cartas_respuestas:
        carta["superficie"] = IMAGEN_BLANCA.copy()

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    contador_bonus=0
                    print(f"contador bonus: {contador_bonus}")
                    if verificar_respuesta(datos_juego, pregunta_actual, respuesta_usuario):
                        # Cambia el fondo a verde si la respuesta es correcta
                        CLICK_SONIDO.play()
                        cartas_respuestas[i]['superficie'] = IMAGEN_VERDE.copy()
                        print("RESPUESTA CORRECTA")
                        if datos_juego["aciertos_consecutivos"] == 5:
                            datos_juego["vidas"] += 1
                            datos_juego["aciertos_consecutivos"] = 0
                    else:
                        # Cambia el fondo a rojo si la respuesta es incorrecta
                        # ERROR_SONIDO.play()
                        cartas_respuestas[i]['superficie'] = IMAGEN_ROJA.copy()
                        # retorno = "terminado"
                        print("RESPUESTA INCORRECTA")

                    print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
                    bandera_respuesta = True
                
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1

    # Muestra el texto de la nueva pregunta y respuestas
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), fuente_pregunta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_correcta']}", (20, 20), fuente_respuesta, COLOR_NEGRO)

    # pantalla.fill(COLOR_AZUL)
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(cuadro_pregunta["superficie"], (80, 80))

    # Dibuja las respuestas en la pantalla
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'], (600, 100))
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'], (600, 200))
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'], (600, 300))
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'], (600, 400))

    # Muestra puntuación y vidas
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (10, 10), fuente_texto, COLOR_NEGRO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['vidas']}", (10, 40), fuente_texto, COLOR_NEGRO)

    return retorno
