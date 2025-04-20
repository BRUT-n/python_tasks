class Some:

    def __init__(self, field):
        # self.health = 100
        self._health = 100
    
    
    # @property
    # def get_health(self):
    #     return self._health
    

    # @health.setter
    def health(self, value):
        if not isinstance(value, int):
            raise TypeError("health must be int")
        self._health = value if value >= 0 else 0
    

my_obj = Some(1)

