import java.io.FileNotFoundException;
import java.time.Duration;
import java.time.Instant;
import java.util.Scanner;
import java.util.concurrent.ForkJoinPool;

public class Main {

  private static String fileName = "/laberinto.txt";

  public static int threadNum = 1;
  public static int processNum = 1;
  public static boolean mazeSolved = false;

  public static void main(String[] args) throws FileNotFoundException {
    Scanner input = new Scanner(System.in);
    System.out.println("Ingrese dimensiones del laberinto (nxn): ");
    String dimStr = input.nextLine();
    int choice;

    while (true) {
      System.out.println(
          "¿Qué tipo de proceso desea usar para solucionar el laberinto?\n\t1)MultiThreading\n\t2)ForkJoinPool");
      choice = input.nextInt();
      if (choice == 1 || choice == 2) {
        break;
      } else {
        System.out.println("Ingrese una opción válida.");
      }
    }

    Maze laberinto = new Maze("./" + dimStr + fileName);

    laberinto.printMaze();
    laberinto.printInitialCoords();

    Instant start = Instant.now();
    if (choice == 1) {
      Thread solveThread = new Thread(new Multithreading(laberinto,
          laberinto.getInitialCoords(), threadNum));
      solveThread.start();

      try {
        solveThread.join();
      } catch (InterruptedException e) {
        e.printStackTrace();
      }

    } else if (choice == 2) {
      ForkJoinPool pool = new ForkJoinPool();

      FJPSolve FJP = new FJPSolve(laberinto, laberinto.getInitialCoords(), threadNum);
      pool.invoke(FJP);
    }
    Instant finish = Instant.now();

    long execTime = Duration.between(start, finish).toMillis();

    System.out.println("Tiempo de Ejecución: " + execTime + "ms");

    input.close();
  }
}
