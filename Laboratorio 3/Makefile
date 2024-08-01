# Nombre del archivo Main
MAIN = Main

# Archivos .java
SRC = $(MAIN).java Multithreading.java FJPSolve.java Maze.java

# Archivos .class generados
CLASSES = $(MAIN).class Multithreading.class FJPSolve.class Maze.class

# Comando para compilar
JAVAC = javac

# Comando para ejecutar
JAVA = java

# Por defecto: compilar y ejecutar el programa
default: $(MAIN)

# Compilar
$(MAIN): $(CLASSES)

# Regla para generar .class
$(CLASSES): $(SRC)
	$(JAVAC) $^

# Run del main
run: $(MAIN)
	$(JAVA) $(MAIN)

# Limpiar archivos compilados
clean:
	$(RM) $(CLASSES)