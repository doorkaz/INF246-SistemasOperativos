/------------------------------------------------------------------------------------/
  
Testeado en Ubuntu 22.04.4

/------------------------------------------------------------------------------------/

    ¡IMPORTANTE!
        ForkJoinPool es una clase reservada de java, por lo que se cambió su nombre a FJPSolve para utilizar
        la clase reservada "ForkJoinPool" dentro de Main.java

/------------------------------------------------------------------------------------/

Estructura de las carpetas:

    CarpetaPrincipal/
        15x15/
            laberinto.txt
        30x30/
            laberinto.txt
        ...

        .gitignore                          * Archivo que determina que debe ignorar al subir a GitHub.
        Analisis.xlsx                       * Excel de análisis entre ambos enfoques.
        FJPSolve.java                       * Clase que resuelve el laberinto con un enfoque de Forks y Join. (ForkJoinPool)
        Main.java                           * Archivo principal que resuelve el laberinto con ambos enfoques usando sus clases.
        Makefile                            * Makefile de compilación.
        Maze.java                           * Archivo que contiene toda la lógica utilizada para resolver el laberinto.
        Multithreading.java                 * Clase que resuelve el laberinto con un enfoque de Threads.
        README.txt                          * .txt que contiene las instrucciones de compilación y consideraciones.
        ...

/------------------------------------------------------------------------------------/

Instrucciones de compilación:

    1. Abrir terminal y ubicarse en la carpeta que contenga el main.cpp que se señala como "CarpetaPrincipal/" en la sección estructura de las carpetas
    por defecto, en el repositorio es llamada "Laboratorio 3" pero podría ser cualquier nombre si lo desea.

    2. Ejecutar Makefile en la terminal escribiendo "make", debe estar situado en la carpeta principal en todo momento.

    3. Ejecutar Makefile con el comando "make run".

    4. Cuando se solicite, ingresar las dimensiones del laberinto que desea resolver en la terminal, de la forma "nxn"
        Por ejemplo:
            Ingrese dimensiones del laberinto (nxn):
            15x15
        Debe tener en cuenta que esto hará búsqueda de la carpeta 15x15/ que se encuentre dentro de "CarpetaPrincipal/"
        y luego intentará resolverlo para el archivo "laberinto.txt" que se encuentre dentro. 
        Si no existe ese archivo lanzará una excepción.

    5. Se observarán los threads ejecutados con "T" y los procesos ejecutados con "P", la salida es especificada.
/------------------------------------------------------------------------------------/

A considerar:
    * El print no es exactamente el mismo pues depende del procesador de como asigna las tareas,
    además, depende de su velocidad si alcanza a resolver más procesos/hilos luego de haber finalizado el laberinto.

    * Se asume que cada laberinto está dentro de una carpeta llamada de la forma "nxn", donde n es la dimensión 
    y dentro de ella se ubica el archivo "laberinto.txt" que contiene los datos del laberinto.

    * Se incluyó solamente el procesador de uno de los integrantes, el cual es donde se hizo el cálculo
    de los tiempos, pues el otro procesador estaba corriendo una máquina virtual de Linux, lo que puede afectar
    considerablemente en los tiempos de ejecución.

    * Se consideró el tiempo de ejecución como un promedio, realizando 5 datos de tiempo por cada enfoque en cada dimensión.

/------------------------------------------------------------------------------------/

Adicional:

    * Puede eliminar los archivos compilados con "make clean" en la terminal, siempre situado en la carpeta principal.
    * Se incluyó el laberinto de ejemplo 15x15 que se muestra en el .pdf del Laboratorio 3, 
    por defecto se ejecuta "laberinto.txt", por lo que debe ajustar su nombre si desea usarlo.

/------------------------------------------------------------------------------------/
                        
             __                                                 __
          __/  \                                               /  \__
         /  \-./                                               \.-/  \
         \_   66\_                                           _/99   _/
           \  ____)o                                       o(____  /
            ) (_                                               _) (
   .-.     /   \\___                                       ___//   \     .-.            
(_/   \   / /   |___)                                     (___|   \ \   /   \_)
       |  \ \   /                                             \   / /  |
        \  \_) (                                               ) (_/  /
         '-'/ \ \  _                                       _  / / \'-'                      
           / / \ \/ )                                     ( \/ / \ \
          (  \  \  /                                       \  /  /  )
           \__)  "`                                         `"  (__/

    Fotografía inedita (blanco y negro): 
        Miembros del equipo tratando de salir del Metro Baquedano durante la hora punta. 9 de Junio, 2024.
/------------------------------------------------------------------------------------/