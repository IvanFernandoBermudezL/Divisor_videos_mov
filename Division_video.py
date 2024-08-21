from moviepy.video.io.VideoFileClip import VideoFileClip
import os

# Ruta al video original
input_video = r'C:\Users\ivanf\Downloads\IMG_5884.mov'

# Directorio de salida
output_dir = r'C:\Users\ivanf\Downloads\salida.mov'

# Asegúrate de que el directorio de salida exista
os.makedirs(output_dir, exist_ok=True)

# Carga el video
video = VideoFileClip(input_video)

# Duración total del video en segundos
video_duration = video.duration

# Duración de cada parte
part_duration = video_duration / 12

# Crear y guardar los clips
for i in range(12):
    start_time = i * part_duration
    end_time = (i + 1) * part_duration
    subclip = video.subclip(start_time, end_time)
    
    # Define el nombre del archivo de salida
    output_filename = os.path.join(output_dir, f'video_part_{i+1}.mov')
    
    # Escribe el subclip al archivo
    subclip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

# Liberar recursos
video.close()