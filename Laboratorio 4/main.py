from islands import init_bar_and_islands_dict
from functions import *
from threading import Thread

total_pirates = 500

# Diccionario que describe los piratas en cola a la isla y en la isla, junto a los semaforos
pirates_on_islands_and_on_queue = init_bar_and_islands_dict()

threads = []

# Crea un diccionario de archivos txt necesarios y los abre con formato 'a' para append
txt_files_dict = init_txt_files()

print("El programa main.py se está ejecutando y se crearon los archivos .txt.")

# Entran al bar del oráculo y reciben las instrucciones
for thread_num in range(1, total_pirates + 1):
  thread = Thread(target = threading_function, args = (str(thread_num), pirates_on_islands_and_on_queue, txt_files_dict))
  threads.append(thread)
  threads[thread_num - 1].start()

for i in range(0, total_pirates):
  threads[i].join()

close_files(txt_files = txt_files_dict) # Cierra todos los archivos

print("\nEl programa main.py finalizó, se han completado los registros en los archivos .txt")