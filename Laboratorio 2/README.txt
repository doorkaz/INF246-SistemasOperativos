/------------------------------------------------------------------------------------/

Testeado en Ubuntu 22.04.4

/------------------------------------------------------------------------------------/

Estructura de las carpetas:

    CarpetaPrincipal/
        functions.cpp           * Archivo donde se implementan las funciones.
        functions.h             * Archivo donde se declaran las funciones.
        main.cpp                * Archivo principal que contiene la lógica del juego.
        Makefile                * Makefile de compilación
        README.txt              * .txt que contiene las instrucciones de compilación y consideraciones.
        ...

/------------------------------------------------------------------------------------/

Instrucciones de compilación:

    1. Abrir terminal y ubicarse en la carpeta que contenga el main.cpp que se señala como "CarpetaPrincipal/" en la sección estructura de las carpetas
    por defecto, en el repositorio es llamada "Laboratorio 2" pero podría ser cualquier nombre si lo desea.

    2. Ejecutar Makefile en la terminal escribiendo "make", debe estar situado en la carpeta principal en todo momento.

    3. Ejecutar main en la terminal con "./main".

/------------------------------------------------------------------------------------/

A considerar:
    1. Solamente se imprime la salud de los luchadores por cada ronda, 
    pues se considera que es demasiado texto para la terminal agregar
    todas las estadísticas.

    2. El ganador por empate es escogido por preferencia del índice, 
    si empata el luchador 3 con el luchador 4, gana el 4, es decir, el índice más grande.

/------------------------------------------------------------------------------------/

Adicional del Makefile:

    * Puede eliminar los archivos compilados con "make clean" en la terminal, siempre situado en la carpeta principal.

/------------------------------------------------------------------------------------/

                                 |\    /|
                              ___| \,,/_/
                           ---__/ \/    \
                          __--/     (D)  \
                          _ -/    (_      \ 
                         // /       \_ /  -\
   __-------_____--___--/           / \_ O o)
  /                                 /   \__/
 /                                 /
||          )                   \_/\
||         /              _      /  |
| |      /--______      ___\    /\  :
| /   __-  - _/   ------    |  |   \ \
 |   -  -   /                | |     \ )
 |  |   -  |                 | )     | |
  | |    | |                 | |    | |
  | |    < |                 | |   |_/
  < |    /__\                <  \
  /__\                       /___\

/------------------------------------------------------------------------------------/