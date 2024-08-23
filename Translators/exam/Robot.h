#include "Entity.h"

class Robot : public Entity {
public:
   Robot(int posR=1, int posC=4, Orient ori= Orient::North);

public:
   void turn(int degrees);
   void forward();
   Point nextStep();
};