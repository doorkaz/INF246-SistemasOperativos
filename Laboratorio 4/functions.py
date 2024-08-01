from islands import islands_properties
from random import sample
from time import sleep
from datetime import datetime

def generate_rand_values_from_dict(dict, quantity_of_rand_values = 2):
  """
  Genera valores aleatorios a partir de las keys de un diccionario,
  por default genera 2 valores.

  params:
    dict: Diccionario
    quantity_of_rand_values(No requerido): Por defecto, calcula 2 valores aleatorios, pero es modificable.

  return:
    Lista de valores aleatorios
  """
  lst = list(dict.keys())

  return sample(lst, quantity_of_rand_values)

def init_txt_files(settings = {'mode': 'w', 'encoding': 'UTF-8'}):
  """
  Inicializa todos los archivos .txt necesarios para resolver el problema.

  return:
    txt_files: Diccionario que contiene los nombres de los 
    archivos con su value que es el archivo para manipular.
  """

  txt_files = {
    'BarOraculo': open('BarOraculo.txt', settings['mode'], encoding = settings['encoding'])
  }
  
  for island in islands_properties:
    txt_files[island] = open(island + '.txt', settings['mode'], encoding = settings['encoding'])
  
  txt_files['Salida'] = open('Salida.txt', settings['mode'], encoding = settings['encoding'])

  for _, file_content in txt_files.items():
    file_content.flush() # Libera el buffer interno

  return txt_files

def close_files(txt_files):
  """
  Cierra todos los archivos de un diccionario de la forma par
  key, value => nombre del archivo, archivo

  params:
    txt_files: Diccionario de archivos .txt que se deben cerrar.

  return:
    void
  """
  for file in txt_files.values():
    file.close()

def get_str_datetime_now():
  """
  Devuelve la hora actual en string
  
  return:
    hora(string)
  """
  return str(datetime.now().time())

def write_on_txt_file(file, text):
  """
  Escribe 'text' en el archivo 'file', luego limpia el buffer interno.
  
  params:
    file: Archivo donde se debe escribir el texto
    text: Texto que se debe escribir en el archivo
  return:
  """
  file.write(text)
  file.flush()

def enter_bar(thread_num, lock_bar):
  """
  Función auxiliar que resuelve la entrada al bar por primera vez,
  calcula el tiempo de entrada al bar y
  entrega las dos islas aleatorias que debe visitar.
  
  params:
    thread_num: Número del thread o número del pirata
    lock_bar: Lock que protege el orden de llegada al bar de uno en uno

  return:
    join_to_bar (string): Texto que debe escribir en BarOraculo.txt
    islands_to_visit (list): Lista de dos valores aleatorios

  """
  with lock_bar:
    # Pasa al bar por primera vez y de uno en uno (lock)
    time_join_bar = get_str_datetime_now()

    # El oraculo le da al pirata 2 islas para visitar.
    islands_to_visit = generate_rand_values_from_dict(islands_properties)

    join_to_bar = f"Pirata{thread_num}, {time_join_bar}, "
  
  return join_to_bar, islands_to_visit

def visit_island(thread_num, island, number_of_island, info, files_dict, join_to_bar, join_island_bridges):
  """
  Función auxiliar que resuelve el problema de visitar la isla, junto a sus complicaciones.
  Se preocupa de que los piratas hagan la búsqueda del tesoro de manera sincronizada,
  se espera a que todos los piratas entren a la isla por orden de llegada
  y puedan esperar a los demás piratas para que empiecen la búsqueda.

  params:
    thread_num: Número del thread o del pirata.
    island: Nombre de la isla visitada.
    number_of_island: Mencionada si la isla visita es la primera o la segunda.
    info: Diccionario que guarda todos los semáforos y locks necesarios, junto a la condición de la isla.
    files_dict: Diccionario que almacena las referencias a los archivos .txt del bar, islas y salida.
    join_to_bar: Texto que guarda la información del pirata y el tiempo de llegada al bar.
    join_island_bridges: Lista que contiene la lista de ambos textos que guardan el tiempo de llegada a los puentes de las islas

  return: void
  """
  lock_queue = info[island]["lock_queue"]
  lock_island = info[island]["lock_island"]
  semaphore_queue = info[island]["queue_semaphore"]
  semaphore_pirates_on_island = info[island]["island_semaphore"]
  island_condition = info[island]["island_condition"]
  duration_treasure_hunt = islands_properties[island]["duration"]

  # Protege que entren de a uno y en orden.
  with lock_queue:
    semaphore_queue.acquire() # Entra al puente de la isla
    time_join_queue = get_str_datetime_now()
    join_island_bridges.append(f"{island}, {time_join_queue}")

    # Si está en su segunda isla, debe escribir en el bar del oraculo
    if number_of_island == 2:
      oracleBarText = join_to_bar + join_island_bridges[0] + ", " + join_island_bridges[1] + "\n"
      write_on_txt_file(file = files_dict['BarOraculo'], text = oracleBarText)

  semaphore_pirates_on_island.acquire() # Usa un cupo en la isla
  semaphore_queue.release() # Libera 1 cupo en el puente ya que se ocupa uno en la isla

  island_condition.acquire()

  # Espera que todos los piratas puedan entrar a la isla
  if (semaphore_pirates_on_island._value == 0):
    # Invoca a todos los piratas a la isla
    island_condition.notify_all()
  else:
    # Deja esperando hasta que todos estén listos para entrar a la isla
    island_condition.wait(timeout = 20)

  island_condition.release()

  # Gracias a la condition pueden entrar los piratas a la isla al mismo tiempo
  with lock_island: # Protege que escriba primero pero en orden de llegada
    time_join_island = get_str_datetime_now() # Entra a la isla
    join_to_island = f"Pirata{thread_num}, {str(time_join_queue)}, {str(time_join_island)}, {number_of_island}\n"
    write_on_txt_file(file = files_dict[island], text = join_to_island)

  sleep(duration_treasure_hunt) # Realiza la búsqueda del tesoro
  semaphore_pirates_on_island.release() # Libera 1 cupo en la isla

def leave_bar(thread_num, files_dict, lock_write_leaving_bar):
  """
  Función auxiliar que resuelve la salida del pirata del bar,
  también escribe en el texto de Salida.txt el tiempo en que sale del bar.

  params:
    thread_num: Número del thread o del pirata.
    files_dict: Diccionario que almacena las referencias a los archivos .txt del bar, islas y salida.
    lock_write_leaving_bar: Lock que protege que la escritura en Salida.txt sea por orden de llegada.

  return: void
  """
  # En esta parte el pirata sale del bar
  time_leaving_bar = get_str_datetime_now()

  # Protege que se imprima en orden de llegada en Salida.txt
  with lock_write_leaving_bar:
    write_on_txt_file(file = files_dict['Salida'], text = f"Pirata{thread_num}, {time_leaving_bar}\n")

def threading_function(thread_num, info, txt_files_dict):
  """
  Función especial para trabajar con multithreading, en ella el pirata
  resuelve su acceso a cada isla, de forma que se va registrando en cada 
  archivo .txt sus tiempos y movimientos de forma sincronizada con otros threads.

  params:
    thread_num: Número del thread o del pirata.
    info: Diccionario que guarda todos los semáforos y locks necesarios, junto a la condición de la isla.
    txt_files_dict: Diccionario que almacena las referencias a los archivos .txt del bar, islas y salida.

  return: void
  """
  join_island_bridges = []

  # Resuelve la entrada al bar en orden de llegada
  text_join_to_bar, islands_to_visit = enter_bar(thread_num = thread_num, lock_bar = info["BarOraculo"]["lock_bar"])

  for number_of_island, island in enumerate(iterable = islands_to_visit, start = 1):
    # Visita cada isla, pasando primero por sus puentes y luego de visitar
    # a una entra al bar para repetir el proceso
    visit_island(
      thread_num = thread_num,
      island = island,
      number_of_island = number_of_island,
      info = info,
      files_dict = txt_files_dict,
      join_to_bar = text_join_to_bar,
      join_island_bridges = join_island_bridges
    )

  # Sale del bar
  leave_bar(thread_num = thread_num, files_dict = txt_files_dict, lock_write_leaving_bar = info['Salida']["lock_leaving_bar"])

    