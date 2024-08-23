#include "Robot.h"
#include <vector>

using namespace std;

class Tile : public Entity {
public:
   Tile();
};

class Brick : public Entity {
public:
   Brick(int posX, int poxY);
};

class Square {
public:
   Square(Entity ent = Tile(), string symb = "⬜");

   Entity entity;
   string symbol;
};

class Maze {
public:
   Maze(int numRows=10, int numCols=14);

   void initMaze();
   void addEntity(Entity ent, string symb);
   void moveEntity(int rOld, int cOld, int rNew, int cNew);
   void printRowCol(int r, int c, string msg);
   void cls();
   void drawMaze();

   int nRows;
   int nCols;
   vector< vector<Square> > floor;
};

class MazeSimulator {
public:
   MazeSimulator();

   Maze labyrinth;
   Robot xolo;

   bool moveRobot();
   void turnRobot(int sentido);
   void drawMaze();
   bool wallAhead();

};