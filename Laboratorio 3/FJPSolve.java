import java.util.List;
import java.util.concurrent.RecursiveTask;

public class FJPSolve extends RecursiveTask<Integer> {
  private Maze maze;
  private int[] currentCoords;
  private int processNum;

  public FJPSolve(Maze laberinto, int[] coords, int processNum) {
    this.maze = laberinto;
    this.currentCoords = coords;
    this.processNum = processNum;
  }

  protected Integer compute() {
    boolean done = false; // Realiza el camino hasta que no pueda (done = true)

    while (!done) {
      List<int[]> possiblePaths = maze.getPossiblePaths(currentCoords[0], currentCoords[1]);
      int possiblePathsLength = possiblePaths.size();

      // En caso de que el laberinto esté resuelto se cancela el thread.
      if (Main.mazeSolved) {
        done = true;
        return 1;
      }

      if (maze.getCasilla(currentCoords) == 'S') {
        done = true;
        System.out.println("P" + processNum + "- [" + currentCoords[1] + "," + currentCoords[0] + "]- Salida");
        Main.mazeSolved = true;
        return 1;
      }

      maze.markPosition(currentCoords); // Marca posición actual

      // Printea si encuentra un camino sin salida
      if (possiblePathsLength == 0) {
        done = true;
        System.out.println("P" + processNum + "- [" + currentCoords[1] + "," + currentCoords[0] + "]");
        return 0;
      }

      boolean intersection = possiblePathsLength > 1;

      if (intersection) {
        // Printea el punto de intersección
        System.out.println("P" + processNum + "- [" + currentCoords[1] + "," + currentCoords[0] + "]");

        // Hay una intersección, recorre cada posición posible y crea un thread que
        // resuelve ese camino.
        for (int i = 0; i < possiblePathsLength; i++) {
          Main.processNum += 1;
          FJPSolve newPath = new FJPSolve(maze, possiblePaths.get(i), Main.processNum);
          newPath.fork();
          newPath.join();
        }

        // Luego de crear cada thread en la intersección, se termina el hilo en que
        // estaba y continua dentro de los demás threads creados.
        done = true;
        return 0;
      } else {
        // Si no encuentra una intersección avanza a la única posición posible
        this.currentCoords = possiblePaths.get(0);
      }
    }
    return 0;
  }

}