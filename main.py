import datetime
import argparse

parser = argparse.ArgumentParser(description='Procesa un archivo de subtítulos.')
parser.add_argument('file', type=str, help='El archivo de subtítulos a procesar.')
parser.add_argument('-H', '--hour', type=int, help='La cantidad de horas a ajustar.', default=0)
parser.add_argument('-M', '--minute', type=int, help='La cantidad de minutos a ajustar.', default=0)
parser.add_argument('-S', '--second', type=int, help='La cantidad de segundos a ajustar.', default=0)
parser.add_argument('-MS', '--millisecond', type=int, help='La cantidad de milisegundos a ajustar.', default=0)
args = parser.parse_args()

# Abrir el archivo de subtítulo para leer
with open(args.file, "r") as f:
    lines = f.readlines()

# Definir el formato del tiempo en el subtítulo
sub_time_format = "%H:%M:%S,%f"

start_time_str = None
end_time_str = None
count_subtitle_line = 0

# tiempo a restar
time_to_subtract = datetime.timedelta(hours=args.hour, minutes=args.minute, seconds=args.second, milliseconds=args.millisecond)

# Recorrer todas las líneas del subtítulo
for i, line in enumerate(lines):
    line = line.strip()

    # Esto es para regresar el contador de líneas de subtítulos desde el inicio
    if line.isdigit():
        count_subtitle_line += 1
        lines[i] = f"{str(count_subtitle_line)}\n"

    # Si la línea es una línea de tiempo (no es el número de línea o una línea en blanco)
    elif " --> " in line:
        # Extraer el tiempo de inicio y final de la línea
        start_time_str, end_time_str = line.split(" --> ")
        # Convertir el tiempo de inicio y final a objetos datetime
        start_time = datetime.datetime.strptime(start_time_str, sub_time_format)
        end_time = datetime.datetime.strptime(end_time_str, sub_time_format)

        # Restar el tiempo especificado a ambos tiempos
        new_start_time = start_time - time_to_subtract
        new_end_time = end_time - time_to_subtract

        # Formatear los tiempos en el formato deseado
        new_start_time_str = new_start_time.strftime(sub_time_format)[:-3]
        new_end_time_str = new_end_time.strftime(sub_time_format)[:-3]

        # Reemplazar el tiempo original con el nuevo tiempo en la línea del subtítulo
        lines[i] = f"{new_start_time_str} --> {new_end_time_str}\n"

# Escribir las líneas actualizadas de vuelta en el archivo de subtítulo
with open(args.file, "w") as f:
    f.writelines(lines)
