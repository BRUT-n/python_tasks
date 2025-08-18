PLANETS = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1.0,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132,
}


class SpaceAge:
    def __init__(self, seconds):
        self.year_on_earth = 31_557_600
        self.seconds = seconds
        self.converting_seconds = seconds / self.year_on_earth

    def on_planet(self, planet_name): # функция под возврат в зависимости от планеты
        planet = PLANETS[planet_name]  # присваивание значений по ключу из словаря
        return round(self.converting_seconds / planet, 2)  # вычисление

    def on_mercury(self):
        return self.on_planet("Mercury")  #

    def on_venus(self):
        return self.on_planet("Venus")

    def on_earth(self):
        return self.on_planet("Earth")

    def on_mars(self):
        return self.on_planet("Mars")

    def on_jupiter(self):
        return self.on_planet("Jupiter")

    def on_saturn(self):
        return self.on_planet("Saturn")

    def on_uranus(self):
        return self.on_planet("Uranus")

    def on_neptune(self):
        return self.on_planet("Neptune")

    # def on_neptune(self): # старая логика
    #     planet = PLANETS("Neptune"]
    #     return round(self.converting_seconds / planet, 2)
