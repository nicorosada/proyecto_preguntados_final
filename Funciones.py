import random
from Constantes import *
import pygame

def mostrar_texto(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def mezclar_lista(lista_preguntas:list) -> None:
    random.shuffle(lista_preguntas)
    
def verificar_respuesta(datos_juego: dict, pregunta_actual: dict, respuesta: int, comodines: dict) -> bool:
    if respuesta == int(pregunta_actual["respuesta_correcta"]):
        datos_juego["aciertos_consecutivos"] += 1
        datos_juego["puntuacion"] += PUNTUACION_ACIERTO
        retorno = True
        if datos_juego["aciertos_consecutivos"] == 5:
            datos_juego["vidas"] += 1
            datos_juego["aciertos_consecutivos"] = 0
        if comodines["comodin_x2"]: # Si se activa suma otros 100 puntos a la puntuacion
            datos_juego["puntuacion"] += PUNTUACION_ACIERTO
            comodines["comodin_x2"] = False
    else:
        if datos_juego["puntuacion"] > PUNTUACION_ERROR:
            datos_juego["puntuacion"] -= PUNTUACION_ERROR
        datos_juego["aciertos_consecutivos"] = 0
        datos_juego["vidas"] -= 1
        retorno = False
    
    return retorno

def verificar_comodines(evento, comodines: dict, disponibilidad_comodines: dict, boton_comodin_puntos_x2: dict, boton_comodin_pasar_pregunta: dict) -> int:
    if disponibilidad_comodines["comodin_x2"] and boton_comodin_puntos_x2['rectangulo'].collidepoint(evento.pos):
        comodines["comodin_x2"] = True
        disponibilidad_comodines["comodin_x2"] = False
        print("COMODIN X2 ACTIVADO")
        COMODIN_SONIDO.play()
    elif disponibilidad_comodines["comodin_pasar"] and boton_comodin_pasar_pregunta["rectangulo"].collidepoint(evento.pos):
        comodines["comodin_pasar"] = True
        disponibilidad_comodines["comodin_pasar"] = False
        print("COMODIN PASAR ACTIVADO")
        COMODIN_SONIDO.play()
    
def pasar_pregunta_comodin(comodines:dict, indice: int, lista_preguntas: list, bandera_respuesta: bool):
    if comodines["comodin_pasar"] == True:
        indice += 1
        comodines["comodin_pasar"] = False
    if indice >= len(lista_preguntas):  # Si se llega al final, reinicia el índice
        indice = 0
        mezclar_lista(lista_preguntas)
        bandera_respuesta = True  # Marca la bandera para que la pantalla se actualice
        comodines["comodin_pasar"] = False  # Reinicia el estado del comodín
    return indice

    
def reiniciar_datos_juego_y_comodines(datos_juego: dict, disponibilidad_comodines: dict) -> None:
    datos_juego ["puntuacion"] = 0
    datos_juego ["vidas"] = CANTIDAD_VIDAS
    datos_juego ["aciertos_consecutivos"] = 0
    datos_juego ["nombre"] = ""
    disponibilidad_comodines["comodin_x2"] = True
    disponibilidad_comodines["comodin_pasar"] = True
    
def dibujar_comodines(pantalla, disponibilidad_comodines: dict, boton_comodin_puntos_x2: dict, boton_comodin_pasar_pregunta: dict):
    """
    """
    if disponibilidad_comodines["comodin_x2"]:
        boton_comodin_puntos_x2["rectangulo"] = pantalla.blit(boton_comodin_puntos_x2["superficie"], (340, 430))
    if disponibilidad_comodines["comodin_pasar"]:
        boton_comodin_pasar_pregunta["rectangulo"] = pantalla.blit(boton_comodin_pasar_pregunta["superficie"], (120, 430))

def calcular_tiempo_restante(tiempo_inicial, cuenta_regresiva):
    tiempo_actual = pygame.time.get_ticks()
    tiempo_transcurrido = (tiempo_actual - tiempo_inicial) // 1000
    return cuenta_regresiva - tiempo_transcurrido

def inicializar_tiempo(tiempo_inicial):
    if tiempo_inicial is None:
        tiempo_inicial = pygame.time.get_ticks()
    return tiempo_inicial

def avisar_poco_tiempo(tiempo_restante:int):
    if tiempo_restante <= 3:  # Cuando quedan 3 segundos o menos
    # Alternar entre rojo y blanco basado en el tiempo (parpadeo)
        if (pygame.time.get_ticks() // 500) % 2 == 0:  # Cambia cada 0.5 segundos
            color_tiempo = COLOR_ROJO
        else:
            color_tiempo = COLOR_BLANCO
    else:
        color_tiempo = COLOR_NEGRO
    return color_tiempo
