import pygame
from Constantes import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *
from Funciones import *
from moviepy.editor import VideoFileClip

#Configuraciones Basicas
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MI PRIMER JUEGO 114")
icono = pygame.image.load("icono-10.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"vidas":3,"nombre":"","volumen_musica":100,"aciertos_consecutivos":0}
comodines = {"comodin_pasar":False,"comodin_x2":False}
disponibilidad_comodines = {"comodin_pasar":True, "comodin_x2": True}
ventana_actual = "menu"
bandera_musica = False

# # Ruta al video
VIDEO_PATH = "intro_mundial2.mp4"

# Función para reproducir el video con sonido
def reproducir_video(video_path, pantalla):
    """Reproduce un video con sonido en la ventana de Pygame y se pausa en el último frame."""
    clip = VideoFileClip(video_path)  # Cargar el video con MoviePy
    fps = clip.fps  # Obtener los FPS del video
    audio = clip.audio  # Obtener la pista de audio del video

    # Guardar el audio del video como un archivo temporal y cargarlo con pygame
    audio.write_audiofile("temp_audio.mp3")  # Guardar como archivo de audio
    pygame.mixer.music.load("temp_audio.mp3")  # Cargar el audio con pygame.mixer
    pygame.mixer.music.play()  # Reproducir el audio del video

    # Reproducir el video frame por frame
    for frame in clip.iter_frames(fps=fps, with_times=False):
        # Convertir el frame a un formato compatible con Pygame
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
        pantalla.blit(frame_surface, (0, 0))  # Dibujar el frame en la pantalla
        pygame.display.update()  # Actualizar la pantalla

        # Manejo de eventos para permitir cerrar la ventana durante la reproducción
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                clip.close()
                pygame.quit()
                return

        reloj.tick(fps)  # Mantener los FPS del video

    # Al final del video, mostrar el último frame con el mensaje
    frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
    pantalla.blit(frame_surface, (0, 0))  # Dibujar el último frame en la pantalla

    # Dibujar el mensaje "Pulse una tecla para empezar"
    fuente_txt = pygame.font.SysFont("Roboto-Bold", 50)  # Fuente por defecto, tamaño 50
    texto = fuente_txt.render("Pulse una tecla para empezar", True, (255, 255, 255))
    texto_rect = texto.get_rect(center=(pantalla.get_width() // 2, pantalla.get_height() - 50))
    # Variable para controlar el parpadeo
    parpadeando = True
    ultima_actualizacion = pygame.time.get_ticks()  # Tiempo inicial
    intervalo_parpadeo = 500  # Intervalo de parpadeo en milisegundos (500ms)

    # Esperar a que el usuario presione una tecla
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                clip.close()
                pygame.quit()
                return
            if evento.type == pygame.KEYDOWN:  # Detectar cualquier tecla
                esperando = False

        # Alternar visibilidad del texto cada cierto tiempo (parpadeo)
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - ultima_actualizacion > intervalo_parpadeo:
            parpadeando = not parpadeando  # Cambiar el estado de visibilidad
            ultima_actualizacion = tiempo_actual  # Actualizar el tiempo

        # Dibujar el último frame
        pantalla.blit(frame_surface, (0, 0))

        # Dibujar el texto si está "visible"
        if parpadeando:
            pantalla.blit(texto, texto_rect)

        pygame.display.update()  # Actualizar la pantalla
        reloj.tick(30)  # Mantener FPS

    clip.close()  # Cerrar el video al terminar
    pygame.mixer.music.stop()  # Detener la música al finalizar el video

# Reproducir el video de introducción
reproducir_video(VIDEO_PATH, pantalla)

#Ciclo de vida
while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        if bandera_musica == False:
            porcentaje_volumen = datos_juego["volumen_musica"] / 300
            pygame.mixer.music.load("musicaa.mp3")
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_musica = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego,comodines,disponibilidad_comodines)
    elif ventana_actual == "configuraciones":
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego,disponibilidad_comodines)
    elif ventana_actual == "salir":
        corriendo = False
    

    #Actualizar cambios
    pygame.display.flip()

pygame.quit()
    