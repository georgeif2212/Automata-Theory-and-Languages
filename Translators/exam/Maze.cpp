#include <chrono>
#include <thread>
#include <iostream>
#include "Maze.h"

using namespace std;


Tile::Tile() : Entity(1, 1, Orient::None, "Tile") {}

Brick::Brick(int posX, int posY) : Entity(posX, posY, Orient::None, "Brick") {}

Square::Square(Entity ent, string symb) {
   entity = ent;
   symbol = symb;
}

Maze::Maze(int numRows, int numCols) {
   nRows = numRows+2; /* +2 para pared norte y sur */
   nCols = numCols+2; /* +2 para pared este y oeste */
   floor.resize(nRows, vector<Square>(nCols, Square()));

   initMaze();
}

void Maze::initMaze() {

   /* Dibujar pared norte y sur. */
   for (int col = 0; col < nCols; col++) {
      floor[0][col]       = Square(Brick(0,0), "🧱");
      floor[nRows-1][col] = Square(Brick(0,0), "🧱");
   }

   /* Dibujar pared este y oeste. */
   for (int row = 0; row < nRows; row++) {
      floor[row][0]       = Square(Brick(0,0), "🧱");
      floor[row][nCols-1] = Square(Brick(0,0), "🧱");
   }
}

void Maze::addEntity(Entity ent, string symb) {
   int r = ent.position.first;
   int c = ent.position.second;

   floor[r][c] = Square(ent, symb);
}

/* Mueve la visualización de la entidad. */
void Maze::moveEntity(int r, int c, int rNew, int cNew) {
   Square oldSquare = floor[r][c];
   floor[r][c] = Square(); /* Liberar la casilla actual */
   floor[rNew][cNew] = oldSquare;
}

void Maze::printRowCol(int r, int c, string msg) {
   cout << "\033[" << r << ";" << c << "H" << msg << flush;
}

void Maze::cls() {
   cout << "\033[2J" << flush;
}

void Maze::drawMaze() {
   cls();
   for (int r = 0; r < nRows; r++) {
      for (int c = 0; c < nCols; c++) {
         cout << floor[r][c].symbol << flush;
      }
      cout << endl;
   }

   this_thread::sleep_for(chrono::seconds(1));
}


MazeSimulator::MazeSimulator() {
   labyrinth = Maze(8, 12);
   xolo = Robot(1, 5, Orient::South);

   labyrinth.addEntity(xolo, "🤖");
}

bool MazeSimulator::moveRobot() {
   Point oldPos = xolo.getPosition();
   xolo.forward();
   Point newPos = xolo.getPosition();

   bool robotSafe = true;
   Square s = labyrinth.floor[newPos.first][newPos.second];
   if (s.entity.name == "Brick") 
      robotSafe = false;

   labyrinth.moveEntity(oldPos.first, oldPos.second, newPos.first, newPos.second);
   if (!robotSafe) {
      labyrinth.floor[newPos.first][newPos.second].symbol = "☠️";
   }

   return robotSafe;
}

void MazeSimulator::turnRobot(int sentido) {
   xolo.turn(sentido);
}

void MazeSimulator::drawMaze() {
   labyrinth.drawMaze();
}


bool MazeSimulator::wallAhead() {
   Point pos = xolo.getPosition();
   Point delta = xolo.nextStep();

   pos.first += delta.first;
   pos.second += delta.second;

   Square s = labyrinth.floor[pos.first][pos.second];
   if (s.entity.name == "Brick") {
      return true;
   }

   return false;
}
