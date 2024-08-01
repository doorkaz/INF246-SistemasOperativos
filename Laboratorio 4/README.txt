/------------------------------------------------------------------------------------/

Testeado en Ubuntu 22.04.4 y Python 3.10.12

/------------------------------------------------------------------------------------/

    ¡IMPORTANTE! 
        Posiblemente la mayoría de versiones de Python3.X sea compatible,
        solamente por asegurar que funcione correctamente utilice Python 3.10.12,
        versión en la cual se realizó el laboratorio, de todas formas puede probarlo.

/------------------------------------------------------------------------------------/

Estructura de las carpetas:

    CarpetaPrincipal/
        BarOraculo.txt                    
        Isla_del_Bosque_Encantado.txt
        ...
        
        functions.py    * Archivo de Python que modulariza las funciones en un archivo externo a main.py
        islands.py      * Archivo de Python que almacena las propiedades de las islas, sus capacidades y sus puentes.
        .gitignore      * Archivo que determina que debe ignorar al subir a GitHub.
        Makefile        * Makefile útil para probar el programa, este borra los archivos .txt creados.
        README.txt      * .txt que contiene las instrucciones generales y consideraciones.
        

/------------------------------------------------------------------------------------/

Instrucciones de ejecución:

    1. Debe instalar la librería 'datetime' para ello ingrese 'pip install datetime'
    en la terminal y siga las instrucciones requeridas por Linux, si no tiene el package
    manager 'pip' entonces debe instalarlo.

    2. Ahora que tiene pip y la librería 'datetime', puede ejecutar main.py de la forma
    que prefiera en la terminal, nuestro equipo utilizó una versión standard:

        python3 main.py

    Sin embargo, existen varias opciones compatibles.
    Con la versión standard debería funcionarle correctamente el programa.
    
/------------------------------------------------------------------------------------/

Consideraciones y adicional:

    * Sabemos que para esta entrega no era necesario un Makefile, aun así, para mantener
    la tradición, se realizó un Makefile útil que se encarga de limpiar los archivos .txt
    creados a partir de 'main.py'. 
    
    Para hacer uso de este debe ejecutar 'make clean', con esto se eliminaran todos los
    archivos creados por 'main.py'.

    * Los piratas entran por orden de llegada a la isla, pero realizan la busqueda del tesoro
    al mismo tiempo

    * En el caso de que no hayan suficientes piratas disponibles para iniciar una
    búsqueda del tesoro se resuelve con un timeout en el wait, es decir, que cuando
    espera a que se completen los cupos para entrar a la isla se hará hasta que se 
    cumpla ese timeout, este timeout se ha puesto de 20 segundos ya que así se asegura
    de que se cumpla la espera de la forma tradicional y no por este timeout.

    Cuando pasa el timeout inmediatamente se realiza la búsqueda del tesoro.

    * La duración completa del programa utilizando a 500 piratas demora alrededor de
    5-6 minutos.
    
    * Se considera que la salida de la isla ocurre por orden de salida. 

/------------------------------------------------------------------------------------/
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠤⠴⠶⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠂⠉⡇⠀⠀⠀⢰⣿⣿⣿⣿⣧⠀⠀⢀⣄⣀⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⢠⣶⣶⣷⠀⠀⠀⠸⠟⠁⠀⡇⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠘⠟⢹⣋⣀⡀⢀⣤⣶⣿⣿⣿⣿⣿⡿⠛⣠⣼⣿⡟⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⣴⣾⣿⣿⣿⣿⢁⣾⣿⣿⣿⣿⣿⣿⡿⢁⣾⣿⣿⣿⠁⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⠿⠇⠀⠀⠀⠀
                    ⠀⠀⠀⠳⣤⣙⠟⠛⢻⠿⣿⠸⣿⣿⣿⣿⣿⣿⣿⣇⠘⠉⠀⢸⠀⢀⣠⠀⠀⠀
                    ⠀⠀⠀⠀⠈⠻⣷⣦⣼⠀⠀⠀⢻⣿⣿⠿⢿⡿⠿⣿⡄⠀⠀⣼⣷⣿⣿⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣶⣄⡈⠉⠀⠀⢸⡇⠀⠀⠉⠂⠀⣿⣿⣿⣧⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣷⣤⣀⣸⣧⣠⣤⣴⣶⣾⣿⣿⣿⡿⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠛⠉⠀⠀⠀⠀
                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
/------------------------------------------------------------------------------------/