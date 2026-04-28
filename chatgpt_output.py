


'''using this Mermaid UML Diagram, create the skeleton using python code. classDiagram class
UniversalGravity { +float G } class Sun { -string name -float radius -float mass -float temp -float x -float y +get_mass()
 float +get_x_pos() float +get_y_pos() float +__str__() string } class Planet { -string name -float radius -float mass
 -float distance -float x -float y -float vel_x -float vel_y +get_mass() float +get_distance() float +get_x_pos() float +get_x_vel() float +get_y_pos() float +get_y_vel() float +set_x_vel(new_x_vel: float) +set_y_vel(new_y_vel: float) +move_to(new_x: float, new_y: float) +__str__() string } class SolarSystem { -Sun the_sun -list~Planet~ planets +add_planet(new_planet: Planet) +add_sun(the_sun: Sun) +show_planets() +move_planets() } class Simulation { -SolarSystem solar_system -int width -int height -int num_periods +run() } UniversalGravity <-- SolarSystem : uses Sun --* SolarSystem : manages Planet --* SolarSystem : manages SolarSystem <--* Simulation : runs
'''







"""Here’s a clean Python “skeleton” implementation based on your Mermaid UML diagram. It sticks to structure (attributes + method signatures) without adding detailed physics logic yet:"""



class UniversalGravity:
    def __init__(self, G: float = 6.67430e-11):
        self.G = G


class Sun:
    def __init__(self, name: str, radius: float, mass: float, temp: float, x: float, y: float):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__temp = temp
        self.__x = x
        self.__y = y

    def get_mass(self) -> float:
        return self.__mass

    def get_x_pos(self) -> float:
        return self.__x

    def get_y_pos(self) -> float:
        return self.__y

    def __str__(self) -> str:
        return f"Sun(name={self.__name}, mass={self.__mass}, pos=({self.__x}, {self.__y}))"


class Planet:
    def __init__(self, name: str, radius: float, mass: float, distance: float,
                 x: float, y: float, vel_x: float, vel_y: float):
        self.__name = name
        self.__radius = radius
        self.__mass = mass
        self.__distance = distance
        self.__x = x
        self.__y = y
        self.__vel_x = vel_x
        self.__vel_y = vel_y

    def get_mass(self) -> float:
        return self.__mass

    def get_distance(self) -> float:
        return self.__distance

    def get_x_pos(self) -> float:
        return self.__x

    def get_y_pos(self) -> float:
        return self.__y

    def get_x_vel(self) -> float:
        return self.__vel_x

    def get_y_vel(self) -> float:
        return self.__vel_y

    def set_x_vel(self, new_x_vel: float):
        self.__vel_x = new_x_vel

    def set_y_vel(self, new_y_vel: float):
        self.__vel_y = new_y_vel

    def move_to(self, new_x: float, new_y: float):
        self.__x = new_x
        self.__y = new_y

    def __str__(self) -> str:
        return f"Planet(name={self.__name}, mass={self.__mass}, pos=({self.__x}, {self.__y}))"


class SolarSystem:
    def __init__(self):
        self.__the_sun: Sun | None = None
        self.__planets: list[Planet] = []
        self.__gravity = UniversalGravity()

    def add_planet(self, new_planet: Planet):
        self.__planets.append(new_planet)

    def add_sun(self, the_sun: Sun):
        self.__the_sun = the_sun

    def show_planets(self):
        for planet in self.__planets:
            print(planet)

    def move_planets(self):
        # Placeholder for movement logic using gravity
        for planet in self.__planets:
            pass


class Simulation:
    def __init__(self, width: int, height: int, num_periods: int):
        self.__solar_system = SolarSystem()
        self.__width = width
        self.__height = height
        self.__num_periods = num_periods

    def run(self):
        for _ in range(self.__num_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()


'''If you want, I can extend this next with actual orbital physics (gravity force, timestep integration, etc.), or keep it simple for a classroom-style simulation.'''











