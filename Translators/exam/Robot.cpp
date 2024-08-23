#include "Robot.h"

Robot::Robot(int posR, int posC, Orient ori) : Entity(posR, posC, ori, "Robot") {}

void Robot::turn(int degrees)
{
   if (degrees > 0)
   { /* A la izquierda */
      switch (orientation)
      {
      case Orient::North:
         orientation = Orient::West;
         break;
      case Orient::East:
         orientation = Orient::North;
         break;
      case Orient::South:
         orientation = Orient::East;
         break;
      case Orient::West:
         orientation = Orient::South;
         break;
      default:
         break;
      }
   }
   else
   {
      turn(90);
      turn(90);
      turn(90);
   }
}

void Robot::forward()
{
   Point delta = nextStep();

   position.first  += delta.first;
   position.second += delta.second;
}

Point Robot::nextStep()
{
   Point delta = {0, 0};

   switch (orientation)
   {
   case Orient::North:
      delta.first = -1;
      break;
   case Orient::East:
      delta.second = +1;
      break;
   case Orient::South:
      delta.first = +1;
      break;
   case Orient::West:
      delta.second = -1;
      break;
   default:
      break;
   }

   return delta;
}