from threading import Semaphore, Lock, Condition

# Diccionario para almacenar las características de cada isla.
islands_properties = {
  "Isla_de_las_Sombras": {
    "bridge_capacity": 20, # Capacidad de la cola
    "duration": 9, # Duración de busqueda en segundos
    "island_capacity": 10 # Capacidad de la isla
  },
  "Isla_del_Dragon_Rojo": {
    "bridge_capacity": 8,
    "duration": 5,
    "island_capacity": 2
  },
  "Isla_de_las_Estrellas": {
    "bridge_capacity": 15,
    "duration": 7,
    "island_capacity": 5
  },
  "Isla_del_Bosque_Encantado": {
    "bridge_capacity": 6,
    "duration": 4,
    "island_capacity": 3
  },
  "Isla_de_los_Susurros": {
    "bridge_capacity": 6,
    "duration": 1,
    "island_capacity": 5
  },
  "Isla_del_Trueno": {
    "bridge_capacity": 9,
    "duration": 4,
    "island_capacity": 4
  },
  "Isla_del_Tesoro_Oculto": {
    "bridge_capacity": 7,
    "duration": 5,
    "island_capacity": 2
  }
}

def init_bar_and_islands_dict():
  dict = {"BarOraculo": {"lock_bar": Lock()}, "Salida": {"lock_leaving_bar": Lock()}} # Protege que entren al bar de uno en uno
  
  for island, properties in islands_properties.items():
    dict[island] = {} 

    dict[island]["queue_semaphore"] = Semaphore(properties["bridge_capacity"]) # Inicializa un semáforo con capacidad del puente
    dict[island]["lock_queue"] = Lock() # Es útil para proteger que entren a la fila en orden
    
    dict[island]["island_semaphore"] = Semaphore(properties["island_capacity"]) # Inicializa un semáforo con capacidad de la isla
    dict[island]["island_condition"] = Condition() # Protege que actuen todos los piratas en la isla al mismo tiempo
    dict[island]["lock_island"] = Lock()
  return dict