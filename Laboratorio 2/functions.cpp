#include "functions.h"
#include <random>
#include <unistd.h>

using namespace std;

/**
 * @brief Retorna true si se esquiva el ataque, false en caso contrario.
 *
 * @param double probability: Equivale a la probabilidad de evasión.
 * @return bool
 */
bool checkEvasion(double probability)
{
  probability = probability / 100;
  return rand() < probability * ((double)RAND_MAX + 1.0);
}

/**
 * @brief Cierra todos los pipes no utilizados
 *
 * @param int pipes[8][2]: Array de pipes completo
 * @param int pipesUsed[][2]: Array que contiene los extremos usados por pipe utilizado.
 * @param int numPipesUsed: Largo del array pipesUsed[][2]
 */
void closePipesNotUsed(int pipes[8][2], int pipesUsed[][2], int numPipesUsed)
{
  for (int i = 0; i < 8; i++)
  {
    bool readUsed = false;
    bool writeUsed = false;

    // Recorre cada pipe utilizado
    for (int j = 0; j < numPipesUsed; j++)
    {
      // Si es igual al pipe en que se encuentra entonces...
      if (pipesUsed[j][0] == i)
      {
        // Revisa si se utiliza el extremo de lectura o escritura
        if (pipesUsed[j][1] == 0)
        {
          readUsed = true;
        }
        else
        {
          writeUsed = true;
        }
      }
    }

    if (readUsed == true) // Si el extremo de lectura es usado se cierra escritura
    {
      close(pipes[i][1]);
    }
    else if (writeUsed == true) // Si el extremo de escritura es usado se cierra lectura
    {
      close(pipes[i][0]);
    }
    else // Si en pipes utilizados se usa tanto la lectura como escritura se cierra el pipe completo
    {
      close(pipes[i][0]);
      close(pipes[i][1]);
    }
  }
}

/**
 * @brief Cierra todos los signal pipes no utilizados
 *
 * @param int signalPipes[5][2]: Array de signalpipes completo
 * @param int signalPipesUsed[][2]: Array que contiene los extremos usados por signalpipe utilizado.
 * @param int numSignalPipesUsed: Largo del array signalPipesUsed[][2]
 */
void closeSignalPipesNotUsed(int signalPipes[5][2], int signalPipesUsed[][2], int numSignalPipesUsed)
{
  for (int i = 0; i < 5; i++)
  {
    bool readUsed = false;
    bool writeUsed = false;

    // Recorre cada pipe utilizado
    for (int j = 0; j < numSignalPipesUsed; j++)
    {
      // Si es igual al pipe en que se encuentra entonces...
      if (signalPipesUsed[j][0] == i)
      {
        // Revisa si se utiliza el extremo de lectura o escritura
        if (signalPipesUsed[j][1] == 0)
        {
          readUsed = true;
        }
        else
        {
          writeUsed = true;
        }
      }
    }

    if (readUsed == true) // Si el extremo de lectura es usado se cierra escritura
    {
      close(signalPipes[i][1]);
    }
    else if (writeUsed == true) // Si el extremo de escritura es usado se cierra lectura
    {
      close(signalPipes[i][0]);
    }
    else // Si en pipes utilizados se usa tanto la lectura como escritura se cierra el pipe completo
    {
      close(signalPipes[i][0]);
      close(signalPipes[i][1]);
    }
  }
}

/**
 * @brief Calcula un entero aleatorio en un intervalo entregado incluyendo los valores extremos.
 *
 * @param int low: Valor mínimo que se puede obtener.
 * @param int high: Valor máximo que se puede obtener.
 *
 * @return int
 */
int randInt(int low, int high)
{
  random_device rd;
  mt19937 gen(rd());
  uniform_int_distribution<> distr(low, high);

  return distr(gen);
}

/**
 * @brief Revisa si en un array de bools existe un ganador, retorna true si existe un ganador,
 * en caso de que existan más personas vivas se retorna false.
 *
 * @param bool alive[4]: Array que contiene bool en caso de que el luchador esté vivo o muerto.
 * Ej: {1,1,1,1} Si están todos vivos, {1,0,1,1} si el luchador 2 está muerto.
 *
 * @return bool
 */
bool checkWinner(bool alive[4])
{
  int count = alive[0] + alive[1] + alive[2] + alive[3];
  if (count == 0 || count == 1)
  {
    return true;
  }
  return false;
}