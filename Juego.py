import pygame
from Constantes import *
from Preguntas import *
from Funciones import *
pygame.init()

#fondo
fondo = pygame.image.load("fondo_juego.jpg")
fondo = pygame.transform.scale(fondo, VENTANA)

# Carga de imagenes para las preguntas
IMAGEN_PREGUNTA = pygame.image.load("imagen_pregunta2.png")
IMAGEN_PREGUNTA = pygame.transform.scale(IMAGEN_PREGUNTA, TAMAÑO_PREGUNTA)

# Carga de imágenes para las respuestas
IMAGEN_BLANCA = pygame.image.load("boton_respuesta.png")
IMAGEN_VERDE = pygame.image.load("boton_correcta.png")
IMAGEN_ROJA = pygame.image.load("boton_incorrecta.png")

#Carga de imagen para el fondo de el tiempo y puntuacion
fondo_tiempo = pygame.image.load("fondo_tiempo.png")


#Carga de imagen para comodines
imagen_comodin_puntos_x2 = pygame.image.load("boton_x2.png")
boton_comodin_puntos_x2 = {
    "superficie": imagen_comodin_puntos_x2,
    "rectangulo": imagen_comodin_puntos_x2.get_rect(),
}
imagen_comodin_pasar_pregunta = pygame.image.load("boton_pasar.png")
boton_comodin_pasar_pregunta = {
    "superficie": imagen_comodin_pasar_pregunta,
    "rectangulo": imagen_comodin_pasar_pregunta.get_rect(),
}

# Escalado de las imágenes al tamaño de las respuestas
IMAGEN_BLANCA = pygame.transform.scale(IMAGEN_BLANCA, TAMAÑO_RESPUESTA)
IMAGEN_VERDE = pygame.transform.scale(IMAGEN_VERDE, TAMAÑO_RESPUESTA)
IMAGEN_ROJA = pygame.transform.scale(IMAGEN_ROJA, TAMAÑO_RESPUESTA)

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = IMAGEN_PREGUNTA.copy()
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

cartas_respuestas = []
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = IMAGEN_BLANCA.copy()  # Usa la imagen blanca como fondo inicial
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

fuente_pregunta = pygame.font.SysFont("qatar-2022-book", 30)
fuente_respuesta = pygame.font.SysFont("qatar-2022-book", 23)
fuente_texto = pygame.font.SysFont("Roboto-Bold", 35)
mezclar_lista(lista_preguntas)
indice = 0  # INMUTABLE -> En la funcion las declaro como global
bandera_respuesta = False  # INMUTABLE -> En la funcion las declaro como global

# Tiempo
cuenta_regresiva = 10
tiempo_inicial = None


def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict, comodines: dict, disponibilidad_comodines: dict) -> str:
    global indice
    global bandera_respuesta
    global tiempo_inicial
    global cuenta_regresiva

    retorno = "juego"

    cuadro_pregunta["superficie"].blit(IMAGEN_PREGUNTA, (0, 0))

    #Tiempo
    tiempo_inicial = inicializar_tiempo(tiempo_inicial)
    tiempo_restante = calcular_tiempo_restante(tiempo_inicial,cuenta_regresiva)
    if tiempo_restante == 0:
        # Tiempo agotado, pasa a la siguiente pregunta
        datos_juego["vidas"] -= 1
        indice += 1
        if indice >= len(lista_preguntas):  # Si se llega al final, reinicia el índice
            indice = 0
            mezclar_lista(lista_preguntas)
        tiempo_inicial = None  # Reinicia el tiempo para la siguiente pregunta
        bandera_respuesta = True  # Marca para que la pantalla se actualice
        if datos_juego ["vidas"] == 0:
            bandera_respuesta = False
            retorno = "terminado"
        # Tiempo
    color_tiempo = avisar_poco_tiempo(tiempo_restante)

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
            verificar_comodines(evento, comodines, disponibilidad_comodines, boton_comodin_puntos_x2, boton_comodin_pasar_pregunta)
            indice = pasar_pregunta_comodin(comodines, indice, lista_preguntas, bandera_respuesta)
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    if verificar_respuesta(datos_juego, pregunta_actual, respuesta_usuario, comodines):
                        # Cambia el fondo a verde si la respuesta es correcta
                        ACIERTO_SONIDO.play()
                        cartas_respuestas[i]['superficie'] = IMAGEN_VERDE.copy()
                        print("RESPUESTA CORRECTA")
                    else:
                        # Cambia el fondo a rojo si la respuesta es incorrecta
                        ERROR_SONIDO.play()
                        cartas_respuestas[i]['superficie'] = IMAGEN_ROJA.copy()
                        print("RESPUESTA INCORRECTA")
                    print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
                    bandera_respuesta = True
                    tiempo_inicial = None
                
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1

                    if datos_juego["vidas"] == 0:
                        retorno = "terminado"


    # Muestra el texto de la nueva pregunta y respuestas
    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), fuente_pregunta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    mostrar_texto(cartas_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_4']}", (20, 20), fuente_respuesta, COLOR_NEGRO)
    
    

    # Dibuja el fondo
    pantalla.blit(fondo, (0, 0))

    #Dibuja el cuadro de tiempo
    pantalla.blit(fondo_tiempo,(0, 0))

    #Dibuja el cuadro de preguntas
    pantalla.blit(cuadro_pregunta["superficie"], (80, 180))

    # Dibuja las respuestas en la pantalla
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'], (600, 100))
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'], (600, 200))
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'], (600, 300))
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'], (600, 400))

    # Dibuja y muestra los comodines
    dibujar_comodines(pantalla, disponibilidad_comodines, boton_comodin_puntos_x2, boton_comodin_pasar_pregunta)

    # Muestra puntuación y vidas
    mostrar_texto(pantalla, f"PUNTOS: {datos_juego['puntuacion']}", (10, 10), fuente_texto, COLOR_NEGRO)
    mostrar_texto(pantalla, f"VIDAS: {datos_juego['vidas']}", (10, 40), fuente_texto, COLOR_NEGRO)
    mostrar_texto(pantalla, f"TIEMPO: {max(0, tiempo_restante)}", (10, 70), fuente_texto, color_tiempo)

    mostrar_texto(pantalla, f"{pregunta_actual['respuesta_correcta']}", (900,550), fuente_respuesta, COLOR_NEGRO)

    return retorno
