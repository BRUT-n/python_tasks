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
    total_aliens_created = 0
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


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(coordinates: tuple):
    # aliens_list = []
    # for x_coord, y_coord in coordinates:
    #     aliens_list.append(Alien(x_coord,y_coord))
    
    return [Alien(x_coord, y_coord) for x_coord, y_coord in coordinates]


# output tests:

# task_1
# alien = Alien(coordinates_x=2, coordinates_y=0)
# print(alien.x_coordinate) # 2
# print(alien.y_coordinate) # 0
# print(alien.health) # 3

# task_2
# alien.hit()
# print(alien.health) # 3-1 = 2

# task_3
# print(alien.is_alive())

# task_4
# alien.teleport(5, -4)
# print(alien.x_coordinate)
# print(alien.y_coordinate)

# task_6
# alien_one = Alien(5, 1)
# print(alien_one.total_aliens_created)
# 1
# alien_two = Alien(3, 0)
# print(alien_two.total_aliens_created)
# 2
# print(alien_one.total_aliens_created)
# 2
# print(Alien.total_aliens_created)
# Accessing the variable from the class directly
# 2

# task_7
# alien_start_positions = [(4, 7), (-1, 0)]
# aliens = new_aliens_collection(alien_start_positions)

# for alien in aliens:
#    	print(alien.x_coordinate, alien.y_coordinate)
# (4, 7)
# (-1, 0)