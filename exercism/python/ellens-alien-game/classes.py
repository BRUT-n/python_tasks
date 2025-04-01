"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.
    
    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = int()
    def __init__(self, coordinates_x, coordinates_y):
        self.x_coordinate = coordinates_x
        self.y_coordinate = coordinates_y
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -= 1

    def is_alive(self) -> bool:
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass


# alien = Alien(coordinates_x=1, coordinates_y=1)
# alien.teleport(5, -4)
# print(alien.x_coordinate)
# print(alien.y_coordinate)
# # print(alien.health)

# alien.hit()
# print(alien.health)

# print(alien.is_alive())

alien_one = Alien(5, 1)
print(alien_one.total_aliens_created)
1
alien_two = Alien(3, 0)
print(alien_two.total_aliens_created)
2
print(alien_one.total_aliens_created)
2
print(Alien.total_aliens_created)
# Accessing the variable from the class directly
2


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
