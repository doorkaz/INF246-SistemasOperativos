import java.util.List;

public class Multithreading implements Runnable {
  private Maze maze;
  private int[] currentCoords;
  private int threadNum;

  public Multithreading(Maze laberinto, int[] coords, int threadNum) {
    this.maze = laberinto;
    this.currentCoords = coords;
    this.threadNum = threadNum;
  }

  public void run() {
    boolean done = false; // Realiza el camino hasta que no pueda (done = true)

    while (!done) {
      List<int[]> possiblePaths = maze.getPossiblePaths(currentCoords[0], currentCoords[1]);
      int possiblePathsLength = possiblePaths.size();

      // En caso de que el laberinto esté resuelto se cancela el thread.
      if (Main.mazeSolved) {
        done = true;
        break;
      }

      if (maze.getCasilla(currentCoords) == 'S') {
        done = true;
        System.out.println("T" + threadNum + "- [" + currentCoords[1] + "," + currentCoords[0] + "]- Salida");
        Main.mazeSolved = true;
        break;
      }

      maze.markPosition(currentCoords); // Marca posición actual

      // Printea si encuentra un camino sin salida
      if (possiblePathsLength == 0) {
        done = true;
        System.out.println("T" + threadNum + "- [" + currentCoords[1] + "," + currentCoords[0] + "]");
        break;
      }

      boolean intersection = possiblePathsLength > 1;

      if (intersection) {
        System.out.println("T" + threadNum + "- [" + currentCoords[1] + "," + currentCoords[0] + "]"); // Printea el
                                                                                                       // punto de
                                                                                                       // intersección

        // Hay una intersección, recorre cada posición posible y crea un thread que
        // resuelve ese camino.
        Thread[] threadArr = new Thread[possiblePathsLength];
        for (int i = 0; i < possiblePathsLength; i++) {
          Main.threadNum += 1;
          threadArr[i] = new Thread(new Multithreading(maze, possiblePaths.get(i), Main.threadNum));
          threadArr[i].start();

        }

        for (int i = 0; i < possiblePathsLength; i++) {
          try {
            threadArr[i].join();
          } catch (InterruptedException e) {
            e.printStackTrace();
          }
        }

        // Luego de crear cada thread en la intersección, se termina el hilo en que
        // estaba y continua dentro de los demás threads creados.
        done = true;
        break;
      } else {
        // Si no encuentra una intersección avanza a la única posición posible
        this.currentCoords = possiblePaths.get(0);
      }
    }
  }
}