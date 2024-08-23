#include "Maze.h"

int main()
{
   MazeSimulator sim;
   sim.drawMaze();

   while (sim.wallAhead() == false ) 
   {
      /* Avanzar un cuadro en la dirección actual */
      sim.moveRobot();
      sim.drawMaze();
   }

   return 0;
}
