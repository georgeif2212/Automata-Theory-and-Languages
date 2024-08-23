#include <tuple>
#include <string>

using namespace std;

enum class Orient {North, South, East, West, None};

using Point = std::pair<int, int>;

class Entity {
public:
   Entity(int posRow = 1, int posCol=1, Orient orientation = Orient::North, string name = "nada");

   Point getPosition();
   Orient getOrient();

   string name;
   Point position;
   Orient orientation;
};

