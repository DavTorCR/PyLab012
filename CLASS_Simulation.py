from CLASS_SolarSystem import SolarSystem
from CLASS_Sun import Sun
from CLASS_Planet import Planet


class Simulation:
    def __init__(self, width: int, height: int, num_periods: int):
        self.__solar_system = SolarSystem()
        self.__width = width
        self.__height = height
        self.__num_periods = num_periods

    def get_solar_system(self):
        return self.__solar_system

    def run(self):
        self.__solar_system.show_planets()
        for _ in range(self.__num_periods):
            self.__solar_system.move_planets()
            self.__solar_system.show_planets()


def main():
    sim = Simulation( width = 500 , height = 500, num_periods = 2000 )
    sol_sys = sim.get_solar_system()
    from CLASS_Sun import Sun
    sol_sys.add_sun(Sun('Sol', 60096340, 10e10, 273, 0, 0 ))
    from CLASS_Planet import Planet
    sol_sys.add_planet(Planet('Earth', 5.972e24, 10e10 ,0, 0 , 29.78e3, 100,100 ))
    sim.run()

if __name__ == '__main__':
    main()



