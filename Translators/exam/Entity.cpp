#include "Entity.h"

Entity::Entity(int posRow, int posCol, Orient orient, string name) {
   position = std::make_pair(posRow, posCol);
   orientation = orient;
   this->name = name;
}

Point Entity::getPosition() {
   return position;
}

Orient Entity::getOrient() {
   return orientation;
}