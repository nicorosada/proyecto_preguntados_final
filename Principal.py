import pygame
from Constantes import *
from Menu import *
from Juego import *
from Configuracion import *
from Rankings import *
from Terminado import *
# from moviepy.editor import VideoFileClip

#Configuraciones Basicas
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MI PRIMER JUEGO 114")
icono = pygame.image.load("icono-10.png")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100,"aciertos_consecutivos":0}
ventana_actual = "menu"
bandera_musica = False

# Ruta al video
# VIDEO_PATH = "intro_mundial2.mp4"

# # Crear la ventana de Pygame según el tamaño del video
# clip = VideoFileClip(VIDEO_PATH)
# video_width, video_height = clip.size  # Obtener las dimensiones del video
# pantalla = pygame.display.set_mode((video_width, video_height))  # Ajustar el tamaño de la ventana
# pygame.display.set_caption("Presentación del Juego")

# Función para reproducir el video con sonido
# def reproducir_video(video_path):
#     """Reproduce un video con sonido en la ventana de Pygame."""
#     clip = VideoFileClip(video_path)  # Cargar el video con MoviePy
#     fps = clip.fps  # Obtener los FPS del video
#     audio = clip.audio  # Obtener la pista de audio del video

#     # Guardar el audio del video como un archivo temporal y cargarlo con pygame
#     audio.write_audiofile("temp_audio.mp3")  # Guardar como archivo de audio
#     pygame.mixer.music.load("temp_audio.mp3")  # Cargar el audio con pygame.mixer
#     pygame.mixer.music.play()  # Reproducir el audio del video

#     for frame in clip.iter_frames(fps=fps, with_times=False):
#         # Convertir el frame a un formato compatible con Pygame
#         frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
#         pantalla.blit(frame_surface, (0, 0))  # Dibujar el frame en la pantalla
#         pygame.display.update()  # Actualizar la pantalla

#         # Manejo de eventos para permitir cerrar la ventana durante la reproducción
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 clip.close()
#                 pygame.quit()
#                 return

#         reloj.tick(fps)  # Mantener los FPS del video

#     clip.close()  # Cerrar el video al terminar
#     pygame.mixer.music.stop()  # Detener la música al finalizar el video

# # Reproducir el video de introducción
# reproducir_video(VIDEO_PATH)





#Ciclo de vida
while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    
    if ventana_actual == "menu":
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        # if bandera_musica == False:
        #     porcentaje_volumen = datos_juego["volumen_musica"] / 300
        #     pygame.mixer.music.load("musicaa.mp3")
        #     pygame.mixer.music.set_volume(porcentaje_volumen)
        #     pygame.mixer.music.play(-1)
        #     bandera_musica = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuraciones":
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "salir":
        corriendo = False
    

    #Actualizar cambios
    pygame.display.flip()

pygame.quit()
    