from Attraction.Attraction import Attraction


class RollerCoaster(Attraction):
    def __init__(self,price_of_ticket, max_number_of_visitors, danger_level, speed, height, type_of_material):
        super().__init__(price_of_ticket, max_number_of_visitors,danger_level)
        self.speed = speed
        self.height = height
        self.type_of_material = type_of_material

    def __str__(self):
        return super().__str__()\
               + "\nSpeed:" + str(self.speed)\
               + "\nHeight: " + str(self.height)\
               + "\nType_of_material: " + self.type_of_material

    def __del__(self):
        pass