#include "Maze.h"

int main()
{
   MazeSimulator sim;
   sim.labyrinth.drawMaze();

   /* Avanzar un cuadro en la dirección actual */
   sim.moveRobot();
   sim.drawMaze();

   /* Avanzar un cuadro en la dirección actual */
   sim.moveRobot();
   sim.drawMaze();

   sim.turnRobot(-1);

   /* Avanzar un cuadro en la dirección actual */
   sim.moveRobot();
   sim.labyrinth.drawMaze();

   sim.moveRobot();
   sim.drawMaze();

   return 0;
}


