import java.io.FileNotFoundException;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;
import java.io.File;

public class Maze {
  private char[][] mazeArray;
  private int mazeDim;
  private int[] initialCoords;

  public int[] getInitialCoords() {
    return initialCoords;
  }

  public int mazeDim() {
    return mazeDim;
  }

  public List<int[]> getPossiblePaths(int row, int column) {
    List<int[]> possiblePaths = new ArrayList<int[]>();
    
    if ((row-1) >= 0 && (mazeArray[row-1][column] == '1' || mazeArray[row-1][column] == 'S')){ // ir arriba
      possiblePaths.add(new int[]{row-1, column});
    }

    if ((row+1) < mazeDim && (mazeArray[row + 1][column] == '1' || mazeArray[row+1][column] == 'S')){ // ir abajo
      possiblePaths.add(new int[]{row+1, column});
    }

    if ((column-1) >= 0 && (mazeArray[row][column - 1] == '1' || mazeArray[row][column-1] == 'S')){ // ir izquierda
      possiblePaths.add(new int[]{row, column-1});
    }

    if ((column+1) < mazeDim && (mazeArray[row][column + 1] == '1' || mazeArray[row][column+1] == 'S')){ // ir derecha
      possiblePaths.add(new int[]{row, column+1});
    }

    return possiblePaths;
  }

  public void markPosition(int[] coords) {
    this.mazeArray[coords[0]][coords[1]] = 'X';
  }

  public char getCasilla(int[] coords){
    return mazeArray[coords[0]][coords[1]];
  }
  
  public void printInitialCoords() {
    System.out.println("Coordenadas de entrada: [" + initialCoords[0] + ", " + initialCoords[1] + "]");
  }

  public void printMaze() {
    System.out.println("Dimensión del laberinto: " + this.mazeDim + "x" + this.mazeDim);
    System.out.println("Laberinto: ");

    for (int i = 0; i < this.mazeDim; i++) {
      for (int j = 0; j < this.mazeDim; j++) {
        System.out.print(mazeArray[i][j] + " ");
      }
      System.out.print("\n");
    }
  }

  public char[][] getMazeArray(){
    return mazeArray;
  }

  public Maze(String filePath) throws FileNotFoundException {
    Scanner fileScan = new Scanner(new File(filePath));

    this.mazeDim = Integer.parseInt((fileScan.nextLine().split("x", 0))[0]);

    // Remueve primer y último caracter de linea 2 ([ y ])
    String tempStr = fileScan.nextLine().substring(1);
    tempStr = tempStr.substring(0, tempStr.length() - 1);

    // Guarda las coordenadas de la entrada
    this.initialCoords = Arrays.stream(tempStr.split(",", 0)).mapToInt(Integer::parseInt).toArray();

    this.mazeArray = new char[this.mazeDim][this.mazeDim];

    String[] temp = new String[this.mazeDim];

    // Guarda matriz en arrays
    for (int i = 0; i < this.mazeDim; i++) {
      if (fileScan.hasNextLine()) {
        temp = fileScan.nextLine().split(" ", 0);
        for (int j = 0; j < this.mazeDim; j++) {
          this.mazeArray[i][j] = temp[j].charAt(0);
        }
      }
    }

    fileScan.close();
  }

}
